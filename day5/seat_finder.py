#!/usr/bin/env python3
from math import ceil
from math import floor

with open('./seat_data.txt','r') as f:
    data = f.read().splitlines()

#rows range from 0 - 127
#colums range from 0 - 8



def next_position(current_row, curent_column,
                  next_letter):
    print(next_letter)
    if next_letter == 'F':
        current_row = current_row[:ceil(len(current_row)/2)]
    elif next_letter == 'B':
        current_row = current_row[int(len(current_row)/2):]
    elif next_letter == 'L':
        current_column = curent_column[:int(len(curent_column)/2)]
    elif next_letter == 'R':
        current_column = curent_column[int(len(curent_column)/2):]
    return current_row, curent_column

def get_seat_pos(seat):
    current_row = [i for i in range(127)]
    curent_column = [i for i in range(7)]
    for pos in list(seat):
        current_row, current_column = next_position(current_row, curent_column,
                                                    pos)
        print(min(current_row), max(current_row),   min(curent_column), max(curent_column))
    return current_row, curent_column

def main():
    for seat in data:
        row, column = get_seat_pos(seat)

test_seat = "BFFFBBFRRR"

print(get_seat_pos(test_seat))
print('------------------first seven below -------------------')
print(get_seat_pos('FBFBBFFRLR'))
#main()
