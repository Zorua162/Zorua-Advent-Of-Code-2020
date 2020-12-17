'''
Day 2
'''

with open('./password_db.txt', 'r') as f:
    data = f.read()

data = data.split('\n')[:-1]

data = [i.split(':') for i in data]

data = [[i[0].split(' '), i[1]] for i in data]

data = [[i[0][0].split('-'), i[0][1], i[1]] for i in data]

def count_letter(word, letter):
    '''
    Count the number of letters in the password of the given letter
    word: the password that is having its rule checked
    letter: the letter that is part of the rule
    '''
    return list(word).count(letter)

def check_word_rule_1(lengths, letter, word):
    '''
    Checks whether the given password meets its requirements
    '''
    count = count_letter(word, letter)
    return (int(lengths[0]) <= count  and count <= int(lengths[1]))

def check_word_rule_2(positions, letter, word):
    '''
    Checks whether the given password meets its requirements
    '''
    word = list(word)
    print(positions, letter,  word)
    if (word[int(positions[0])] == letter and
            word[int(positions[1])] == letter):
        return False
    elif word[int(positions[0])] == letter:
        return True
    elif word[int(positions[1])] == letter:
        return True
    return False

rule1_valid = 0
rule2_valid = 0
for password in data:
    #lengths = password[0]
    #letter = password[1]
    #word = password[2]
    if check_word_rule_1(*password):
        rule1_valid += 1
    if check_word_rule_2(*password):
        rule2_valid += 1

print(f"The number of strings that meet the first rule is: {rule1_valid}")


print(f"The number of strings that meet the second rule is: {rule2_valid}")

