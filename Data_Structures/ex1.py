# Implement an algorithm to determine if a string has all unique characters What if you can not use additional data structures?

def compare_numbers(i, number):
    if (i & number) != 0:
            return -1
    else:
        number = number | i
        return number
        print("result:",  number)

def check_if_only_unique_chars(a):
    first = 0
    second = 0
    third = 0
    forth = 0
    ln = len(a)
    if ln == 0:
        return True
    for j in range(ln):
        i = 1
        i = 1 << (ord(a[j]) % 64 - 1)
        print(i, ord(a[j]))
        if ord(a[j]) // 64 == 0:
            first = compare_numbers(i, first)
        elif ord(a[j]) // 64 == 1:
            second = compare_numbers(i, second)
        elif ord(a[j]) // 64 == 2:
            third = compare_numbers(i, third)
        else:
            forth = compare_numbers(i, forth)
        if (first < 0 or second < 0 or third < 0 or forth < 0):
            return Falss
    return True
a = input()
print(check_if_only_unique_chars(a))