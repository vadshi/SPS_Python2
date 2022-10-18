# Check 1
a = 5
b = 5
print(a == b)  # Out: True
print(a is b)  # Out: True

# Check 2
c = 300
d = 300
print(c == d)  # Out: True
print(c is d)  # Out: False

# Check 3
s1 = 'hello$%^'
s2 = 'hello$%^'
print(s1 == s2)  # Out: True
print(s1 is s2)  # Out: True

# Check 4
lst1 = [45, 3]
lst2 = lst1[:]
print(lst1 is lst2)  # Out: Вспомнить и проверить

tup1 = (45, 3)
tup2 = tup1[:]
print(tup1 is tup2)  # Out: Вспомнить и проверить


# Контрольный вопрос
s3 = 'hello!@Ж'
s4 = s3[:]
print(s3 is s4)   # Out: Вспомнить и проверить
