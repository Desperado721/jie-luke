import wikipedia
import pandas as pd
import collections

def determine_gender(sents):
    for sent in sents:
        sent = sent.lower()
        gender_cnt = collections.default(int)
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
for name in names:
    name = name.split('\t')[0]
    bio = wikipedia.page(name)
    first_2_sentence = bio.content.split('\t')[0:2]
    gender_out = determine_gender(first_2_sentence)
    res.append((name,gender_out))

# save gender info






