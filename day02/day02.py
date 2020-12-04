import re


with open('day02/input.data') as input:
    lines = input.read().splitlines()

split_lines = [re.split('[- :]+', line) for line in lines]

solution_one = len(
    [password for [low, high, char, password] in split_lines
     if int(low) <= password.count(char) <= int(high)]
)
print(f'first solution: {solution_one}')

solution_two = len(
    [password for [low, high, char, password] in split_lines
     if ((password[int(low)-1] == char) ^
         (password[int(high)-1] == char))]
)
print(f'second solution: {solution_two}')
