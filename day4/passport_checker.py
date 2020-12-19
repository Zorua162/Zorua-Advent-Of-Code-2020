'''
Check passports to see if they are valid and sneak north pole ones through
'''
REQUIRED_FIELDS = [
'byr',
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
    n = 0
    valid_count = 0
    for passport in passports:
        n += 1
        print(passport)
        #print(list(passport.keys()))
        #if required_set.issubset(passport.keys()):
        if all(elem in list(passport.keys()) for elem in REQUIRED_FIELDS):
        #if set(passport.keys()).issubset(required_set):
            valid_count += 1
    print(f'The number of valid passports is {valid_count}')


def format_passports():
    '''
    Format the messy input passports.txt into dictionaries
    '''
    passports = []
    with open('./test_passports.txt', 'r') as f:
        data = f.read()
    data = data.split('\n\n')
    data = [i.split('\n') for i in data]
    for passport in data:
        passport_full = []
        passport_dict = {}
        print(passport)
        for item in passport:
            print('item', item)
            passport_full.extend(item.split(' '))
        passport_full = passport_full[:-1]
        for i in passport_full:
            print(i)
            key_value = i.split(':')
            passport_dict[key_value[0]] = key_value[1]
        passports.append(passport_dict)
    return passports

if __name__ == '__main__':
    main()
