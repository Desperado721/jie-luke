import wikipediaapi
import collections
from tqdm import tqdm

def determine_gender(sents):
    for sent in sents:
        sent = sent.lower()
        gender_cnt = collections.defaultdict(int)
        if 'his' in sent or 'him' in sent or 'he' in sent:
            gender_cnt['his']+=1
        elif 'her' in sent or 'she' in sent:
            gender_cnt['her']+=1
    
    if gender_cnt['her'] > gender_cnt['his']:
        return 1
    else:
        return 0

with open ('./entity_disambiguation/persons.txt', 'r') as f:
    names = f.readlines()


res = []
error = []
for i in tqdm(range(len(names))):
    name = names[i].split('\t\n')[0]
    wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)
    try:
        bio = wiki.page(name)
        first_2_sentence = bio.text.split('\n')[0:2]
        gender_out = determine_gender(first_2_sentence)
        res.append((name,gender_out))
    except:
        print(name)

# save gender info
with open('./entity_disambiguation/persons_with_gender.txt', 'w') as f:
    for record in res:
        f.write(record +'\n')

with open('./entity_disambiguation/persons_with_gender_error.txt', 'w') as f:
    for record in error:
        f.write(record +'\n')





