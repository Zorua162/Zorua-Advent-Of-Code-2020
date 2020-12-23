#!/usr/bin/env python3

with open('./seat_data.txt','r') as f:
    data = f.read().splitlines()

#rows range from 0 - 127
#colums range from 0 - 8



def next_position(current_row, curent_column, ,row_pointer, column_pointer,
                  next_letter):
    if next_letter = 'B':
        current_row = curent_column/2
    elif next_letter = 'F':
        current_row =
    return current_row, curent_column

def main():
    for seat in data:
        current_row = range(127)
        curent_column = range(7)
        row_pointer = [0, 127]
        column_pointer = [0, 7]
        for pos in list(seat):
            current_row, current_row = next_position(current_row,
                                                     curent_column,
                                                     row_pointer,
                                                     column_pointer,
                                                     next_letter)



main()
