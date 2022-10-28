def insertion_sort(a):
    for i in range(len(a)):
        v = a[i]
        j = i
        while a[j - 1] > v and j > 0:
            a[j] = a[j - 1]
            j -= 1
        a[j] = v
        print(a)
    return a


array = [54, 8, 3, 7, 52, 3, 1, 2, 3, 5, 3, 67, 3, 2, 543]

print(insertion_sort(array))
