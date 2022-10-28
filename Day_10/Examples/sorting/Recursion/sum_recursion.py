"""
add(5)
    5 + add(4)
        4 + add(3)
            3 + add(2)
                2 + add(1)
                Базовый случай == 1 -> 1

"""

def add(n):
    if n == 1:
        return 1
    else:
        print(n)
        return n + add(n - 1)

print(add(5))

def fib(n):
    if n > 2:
        return fib(n - 1) + fib(n - 2)
    else:
        return 1

print(fib(6))