#!/usr/bin/env python3
ALL_POSSIBLE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

EXAMPLE_DICT = {i:0 for i in ALL_POSSIBLE}

with open('./customs_form_input.txt','r') as f:
    data = f.read()

def create_answer_dict(family):
    family_dict = EXAMPLE_DICT.copy()
    for person in family:
        for answer in list(person):
            family_dict[answer] += 1
    return family_dict

def count_all(running_total, family, family_number):
    print(family, family_number)
    for answer, number in family.items():
        if number == family_number:
            running_total += 1
    return running_total

data = [i.split('\n') for i in data.split('\n\n')]

data[len(data)-1].remove('')

dicts = [create_answer_dict(i) for i in data]

number_people = [len(i) for i in data]

running_total = 0

for i, family in enumerate(dicts):
    running_total = count_all(running_total, family, number_people[i])

print(running_total)



#data = [set(list("".join(i))) for i in data]

#data_lens = [len(i) for i in data]





