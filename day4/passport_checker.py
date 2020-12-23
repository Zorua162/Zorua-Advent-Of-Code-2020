#!/usr/bin/env python3
'''
Check passports to see if they are valid and sneak north pole ones through
'''
import re
REQUIRED_FIELDS = ['byr',
'iyr',
'eyr',
'hgt',
'hcl',
'ecl',
'pid']

def main():
    '''
    count number of valid passports in the file
    '''
    passports = format_passports()
    required_set = set(REQUIRED_FIELDS)
    print(f'There are {len(passports)} passports')
    n = 0
    valid_count = 0
    for passport in passports:
        n += 1
        ##print(passport)
        #print(list(passport.keys()))
        #if required_set.issubset(passport.keys()):
        #if all(elem in list(passport.keys()) for elem in REQUIRED_FIELDS):
        #print(passport.keys())


        #if set(passport.keys()).issubset(required_set):
        #if len(passport) >= 7:
        if valid_passport(passport):
            valid_count += 1
        else:
            print('Invalid')
    print(f'The number of valid passports is {valid_count}')

def check_hgt(hgt):
    #print(hgt)
    match = re.match(r"([0-9]+)([a-z]+)", hgt)
    if match == None:
        print('Match was None')
        return False
    num, unit = match.groups()
    if unit == 'cm':
        if int(num) < 150 or int(num) > 193:
            print('Invalid cm height')
            return False
    elif unit == 'in':
        if int(num) < 59 or int(num) > 76:
            print('Invalid in height')
            return False
    return True
NUMBERS_AND_LETTERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a',
                       'b', 'c', 'd', 'e', 'f']
def check_hcl(hcl):
    hcl = list(hcl)

    if hcl.pop(0) != '#':
        #print('Hair colour no #')
        return False
    for char in hcl:
        if char not in NUMBERS_AND_LETTERS:
            return False
    print('Hair colour valid')
    return True
EYE_COLOURS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
def check_ecl(ecl):
    if ecl not in EYE_COLOURS:
        return False
    #print('Eye colour valid')
    return True

NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def check_pid(pid):
    pid = list(pid)
    if len(pid) != 9:
        return False
    for n in pid:
        if n not in NUMBERS:
            return False
    print('Pid valid')
    return True

def valid_passport(passport):
    for requirement in REQUIRED_FIELDS:
        if requirement not in passport.keys():
            print('DOESNT HAVE ALL REQUIREMENTS')
            return False
    if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
        print('INVALID BYR')
        return False
    elif int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
        print('INVALID IYR')
        return False
    elif int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
        print('INVALID EYR')
        return False
    elif not check_hgt(passport['hgt']):
        print('INVALID HGT')
        return False
    elif not check_hcl(passport['hcl']):
        print('INVALID HCL')
        return False
    elif not check_ecl(passport['ecl']):
        print('INVALD ICL' )
        return False
    elif not check_pid(passport['pid']):
        print('INVALID PID')
        return False
    return True


def format_passports():
    '''
    Format the messy input passports.txt into dictionaries
    '''
    passports = []
    with open('./passports.txt', 'r') as f:
        data = f.read()
    data = data.split('\n\n')
    data = [i.split('\n') for i in data]
    for passport in data:
        passport_full = []
        passport_dict = {}
        ##print(passport)
        for item in passport:
            #print('item', item)
            passport_full.extend(item.split(' '))
        #print(passport_full)
        #passport_full = passport_full[:-1]
        #print(passport_full)
        for i in passport_full:
            ##print(i)
            key_value = i.split(':')
            if len(key_value) > 1:
                passport_dict[key_value[0]] = key_value[1]
        passports.append(passport_dict)
    return passports

if __name__ == '__main__':
    main()
