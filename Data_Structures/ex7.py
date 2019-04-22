# Assume you have a method isSubstring which checks if one word is a substring of another.
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one 
# call to isSubstring (i.e., “waterbottle” is a rotation of “erbottlewat”).


def check_if_substring(s1, s2):
    temp = s2 + s2
    return temp.find(s1) >= 0


try:
    s1=input()
    s2=input()
    print(check_if_substring(s1, s2))
except EOFError:
    print("EOFError:empty string")