## gcd - НОД(наибольший общий делитель)
def gcd(a, b):
    while a != b:
        print(f'{a = }')
        print(f'{b = }')
        if a > b:
            a = a - b
        else:
            b = b - a
    print(a)

gcd(18, 42)
# 
# 
def gcd1(a, b):
    print('*' * 30)
    print(f'{a = }')
    print(f'{b = }')
    if b == 0:
        return a
    else:
        return gcd1(b, a % b)

print(gcd1(52, 84))
# 
# # 
def gcd_while(a, b):
    while b:
       a, b = b, a % b
    return a
# # # 
print(gcd_while(52, 84))
# # #
## НОК (Наименьшее общее кратное)
def mcd(n, m):
    return n * m / gcd_while(n, m)
# 
print(mcd(33, 99))