"""
Напишите генератор letters(some_str), выдает только буквы из 
входящей строки(остальные игнорируются).
"""
def letters(some_str):
	pass


output = letters('A!sdf 09 _ w')
print(next(output))  # Out: 'A'
print(next(output))  # Out: 's'