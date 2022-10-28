def recursion(a, b):  # основное условие задачи
    if a > b:
        # Шаг рекурсии / рекурсивное условие
        return str(a) + ">" + recursion(a - 1, b)
    else:
        # Базовый случай
        if a == b:
            return str(a)

        # Шаг рекурсии / рекурсивное условие
        return str(a) + "<" + recursion(a + 1, b)


# Out: 20 > 15 vs 20 > 15 19 > 15 18 > 15 17 > 15 16 > 15 15 vs 20 > 19 > 18 > 17 > 16
# Out: 20 > 19 > 18 > 17 > 16 > 15
print(recursion(20, 15))

# Out -> 10 < 15 vs ??
print(recursion(10, 15))
