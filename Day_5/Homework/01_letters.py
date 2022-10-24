"""
Напишите генератор letters(some_str), выдает только буквы из
входящей строки(остальные игнорируются).
"""
import re

def letters(some_str):
    for letter in some_str:
        if re.match(r'[a-zA-Z]', letter):
            yield(letter)

output = letters('A!sdf 09 _ w')
print(next(output))  # Out: 'A'
print(next(output))  # Out: 's'
