import wikipediaapi
import collections
from tqdm import tqdm

def determine_gender(sents):
    gender_cnt = {"male": 0, "female": 0}
    for sent in sents:
        words = sent.lower().split(' ')
        words_cnt = collections.Counter(words)
        male_cnt = words_cnt.get('his',0)+words_cnt.get('him',0)+words_cnt.get('he',0)+words_cnt.get('man',0)
        gender_cnt['male'] += male_cnt
        female_cnt = words_cnt.get('her',0)+words_cnt.get('she',0)+words_cnt.get('women',0)+words_cnt.get('woman',0)
        gender_cnt['female'] += female_cnt
    if gender_cnt['female'] > gender_cnt['male']:
        return 1
    else:
        return 0

with open ('./entity_disambiguation/mentions_name_v1.txt', 'r') as f:
    names = f.readlines()


res = []
error = []
female, male = [], []
for i in tqdm(range(len(names))):
    name = names[i].split('\n')[0]
    # name = names[i].split('\t\n')[0]
    wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)
    try:
        bio = wiki.page(name)
        first_3_sentence = bio.text.split('\n')
        gender_out = determine_gender(first_3_sentence)
        res.append((name,gender_out))
        if gender_out == 1:
            female.append((name,gender_out))
        else:
            male.append((name,gender_out))
    except:
        print(name)
        error.append(name)
        break

# save gender info
with open('./entity_disambiguation/mentions_persons_with_gender_new.txt', 'w') as f:
    f.write('\n'.join('%s %s' % x for x in res))

with open('./entity_disambiguation/mentions_persons_with_gender_error.txt', 'w') as f:
    for record in error:
        f.write(record +'\n')

# save male and female seperately

with open('./entity_disambiguation/female_mentions_persons_with_gender.txt', 'w') as f:
    f.write('\n'.join('%s' % x[0] for x in female))

with open('./entity_disambiguation/male_mentions_persons_with_gender.txt', 'w') as f:
    f.write('\n'.join('%s' % x[0] for x in male))




