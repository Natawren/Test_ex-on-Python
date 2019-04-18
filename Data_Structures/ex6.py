#Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0.
import sys

data = []
zerros = [[],[]]
def check_len_row(data, line):
    if len(data) > 0 and len(data[0]) != len(line.split()):
        print("Wrong number of ints in row\n")
        return False
    return True

def     reading_data(data):
    for line in sys.stdin:
        try:
            i = 0
            for i in line.split():
                int(i)
            if check_len_row(data, line) == False:
                return False
            data.append(line.split())
            continue
        except ValueError:
            print("That's not an int!\n")
            return False
    len_x = len(data)
    if  len_x == 0:
        return False
    return True

def     check_null(data, zerros):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '0':
                if (i not in zerros[0]):
                    zerros[0].append(i)
                if (j not in zerros[1]):
                    zerros[1].append(j)
    print(zerros)
    return zerros

def     set_null(data):
    for i in zerros[0]:
        for j in range(len(data[i])):
            data[i][j] = 0
    for j in zerros[1]:
        for i in range(len(data)):
            data[i][j] = 0
    return data

if reading_data(data) == True:
    zerros = check_null(data, zerros)
    data = set_null(data)
    print(data)
else:
    print(False)

