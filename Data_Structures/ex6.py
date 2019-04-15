#Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0.
import sys

data = []

def check_len_row(data, line):
    if len(data) > 0 and len(data[0]) != len(line):
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
    return True
if reading_data(data) == True:
    print(data)