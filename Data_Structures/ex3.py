#Write a method to decide if two strings are anagrams or not.

# def check_if_anagrams(l1, l2):
#     if len(l1) != len(l2):
#         return (False)
#     i = 0
#     while len(l1) != 0 and len(l2) != 0:
#         j = 0
#         flag = 0
#         while j < len(l2) and i < len(l1):
#             if l1[i] == l2[j]:
#                 l1.pop(i)
#                 flag = 1
#                 l2.pop(j)
#                 break
#             j += 1
#         if flag == 0:
#             return False
#     if len(l1) == 0 and len(l2) == 0:
#         return True
#     return False

def check_if_anagrams(l1, l2):
    return sorted(l1) == sorted(l2)


try:
    l1=list(''.join(input()))
    l2=list(''.join(input()))
    print(check_if_anagrams(l1, l2))
except EOFError:
    print("EOFError:empty string")
