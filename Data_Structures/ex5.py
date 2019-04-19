#Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, 
# write a method to rotate the image by 90 degrees. Can you do this in place?
import sys

data = []
def check_len_row(data, line):
    if len(data) > 0 and len(data[0]) != len(line):
        print("Wrong number of ints in row\n")
        return False
    return True

def check_len_col(data):
    return len(data) == len(data[0])
    
def     reading_data(data):
    for line in sys.stdin:
        temp = []
        try:
            for i in line.split():
                temp.append(int(i))
        except ValueError:
            print("That's not an int!\n")
            return False
        if check_len_row(data, temp) == False:
            return False
        data.append(temp)
    len_x = len(data)
    if  len_x == 0:
        return False
    return True

if reading_data(data) == True and check_len_col(data) == True:
    print(data)
else:
    print(False)