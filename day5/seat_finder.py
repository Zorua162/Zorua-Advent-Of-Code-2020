#!/usr/bin/env python3
from math import ceil
from math import floor

with open('./seat_data.txt','r') as f:
    data = f.read().splitlines()

#rows range from 0 - 127
#colums range from 0 - 8



def next_position(current_row, current_column, next_letter):
    print(next_letter)
    if next_letter == 'F':
        current_row = current_row[:ceil(len(current_row)/2)]
    elif next_letter == 'B':
        current_row = current_row[int(len(current_row)/2):]
    elif next_letter == 'L':
        current_column = current_column[:ceil(len(current_column)/2)]
    elif next_letter == 'R':
        current_column = current_column[int(len(current_column)/2):]
    return current_row, current_column

def get_seat_pos(seat):
    current_row = [i for i in range(128)]
    current_column = [i for i in range(8)]
    print(min(current_row), max(current_row),   min(current_column), max(current_column))
    for pos in list(seat):
        current_row, current_column = next_position(current_row, current_column,
                                                    pos)
        print(min(current_row), max(current_row),   min(current_column), max(current_column))
    return current_row[0], current_column[0]

def calc_id(row, column):
    return row * 8 + column

def find_missing(seat_ids):
    i_start = 12
    index = 0

    while True:
        if i_start != seat_ids[index]:
            print(f'Missing seat is id: {i_start}')
            break
        elif i_start > 1000:
            print("Couldn't find the missing seat")
            break
        i_start += 1
        index += 1

def main():
    seat_ids = []
    for seat in data:
        row, column = get_seat_pos(seat)
        seat_id = calc_id(row, column)
        seat_ids.append(seat_id)
    print(max(seat_ids))
    seat_ids.sort()
    print(seat_ids)
    find_missing(seat_ids)


if __name__ == '__main__':
    main()
