lst = [3, 9, 9, 23, 1]
print(lst.pop())  # O(1)
print(max(lst))   # O(n)

for item in lst:  # 3n -> O(n)
    foo = item + 2
    print(foo)

lst = [[23, 23, 8, 3],
       [45, 9, 6, 4],
       [7, 78, 3, 9],
       'hell']

for item in lst:           # n^2 + 4n + 4 -> O(n) -> n^2
    for inner_item in item:
        bar = str(inner_item) * 2
    print(bar)