#Write a method to decide if two strings are anagrams or not.

l1=list(''.join(input()))
l2=list(''.join(input()))

def check_if_anagrams(l1, l2):
    if len(l1) != len(l2):
        return (False)
    i = 0
    while len(l1) != 0 and len(l2) != 0:
        j = 0
        flag = 0
        while j < len(l2) and i < len(l1):
            if l1[i] == l2[j]:
                l1.pop(i)
                flag = 1
                l2.pop(j)
                break
            j += 1
        if flag == 0:
            return False
    if len(l1) == 0 and len(l2) == 0:
        return True
    return False
    
print(check_if_anagrams(l1, l2))