# Implement an algorithm to determine if a string has all unique characters What if you can not use additional data structures?

def compare_numbers(i, number):
    if (i & number) != 0:
            return -1
    else:
        number = number | i
        return number

def check_if_only_unique_chars(a):
    first = 0
    second = 0
    third = 0
    forth = 0
    ln = len(a)
    for j in range(ln):
        n = ord(a[j]) % 64
        i = (1 << n) if n > 0 else 1
        if ord(a[j]) // 64 == 0:
            first = compare_numbers(i, first)
        elif ord(a[j]) // 64 == 1:
            second = compare_numbers(i, second)
        elif ord(a[j]) // 64 == 2:
            third = compare_numbers(i, third)
        else:
            forth = compare_numbers(i, forth)
        if (first < 0 or second < 0 or third < 0 or forth < 0):
            return False
    return True
a = input()
print(check_if_only_unique_chars(a))