#!/usr/bin/env python3

with open('./rules.txt','r') as f:
    data = f.read().split('\n')[:-1]

class bag_type:
    def __init__(colour, fits_in_inital, can_fit_initial):
        if fits_in_inital is not None:
            self.fits_in = fits_in_inital
        else:
            self.fits_in = []
        if can_fit_initial is not None:
            self.can_fit = can_fit_initial
        else:
            self.can_fit = []

#def format_rule(rule):
#    rule = rule.split('contain')
#    rule = [rule[0], [rule[1].split(',')]]
#    return rule
#
#rules = [format_rule(rule) for rule in data]

rules = [rule.split('contain') for rule in data]

rules = [[rule[0], rule[1].split(',')] for rule in rules]

print(rules)

def search_for(bag_type):
    new_outers = []
    for rule in rules:
        for fits in rule[1]:
            if bag_type in fits:
                print(rule[0])
                new_outers.append(rule[0][:-1])
    return new_outers
#bags = []
#
#for rule in rules:
#    if rule[0] not in bags:
#        bags.append(bag_type(rule[0], None, rule[1])
needs_searching = ['shiny gold']
can_contain_gold = []
while len(needs_searching) > 0:
    new_outers = search_for(needs_searching.pop())
    needs_searching.extend(new_outers)
    can_contain_gold.extend(new_outers)
    print(needs_searching)

print(can_contain_gold)
print(len(can_contain_gold))
print(len(set(can_contain_gold)))






