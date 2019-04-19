# Write a method to replace all spaces in a string with ‘%20’.

def     replace_with_nll(lst):
    i = 0
    while i < len(lst):
        if lst[i] == ' ':
            lst.pop(i)
            lst.insert(i, "%20")
        i += 1
    return lst

try:
    lst=list(input())
    print(''.join(replace_with_nll(lst)))
except EOFError:
    print("EOFError:empty string")

