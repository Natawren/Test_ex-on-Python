# Write code to reverse a C-Style String (C-String means that “abcd” is represented as  ve characters, including the null character )

def     reverse_str(s):
    return s[::-1]

try:
    string = input()
    print(reverse_str(string))
except EOFError:
    print("EOFError:empty string")
