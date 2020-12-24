#!/usr/bin/env python3
import itertools

with open('./customs_form_input.txt','r') as f:
    data = f.read()

data = [i.split('\n') for i in data.split('\n\n')]

data[len(data)-1].remove('')

data = [set(list("".join(i))) for i in data]

data_lens = [len(i) for i in data]

print(data)

print(sum(data_lens))
