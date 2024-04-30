# Created by: Landon Walker
# 30/4/2024
# Student Program
# Version = '0.1'
# Program Description: User searchs for a last name, First Name, Last Name, and Average are provided if student found


# Reads a text files and saves the data to a variable as a tuple
# @return - returns the data from the text file
def read_file():
    directory = 'C:/Users/walkerl407/Downloads/Student Marks.txt'  # file location
    with open(directory, 'r') as f:  # sets a variable to open the file
        data = [tuple(map(str, i.split())) for i in f]  # adds the text file data to a list as tuples
    #print(data[4])
    return data  # returns the text file data to the main


# Selection sort to sort the list of tuples by last name
# @param list - the list of tuples read from the text file
# @return - returns the sorted list to the main
def sorter(list):
    for i in range(len(list)-1, 0, -1):
        value = 0
        for j in range(1, i+1):
            if list[j][1] > list[value][1]:
                value = j
        list[j], list[value] = list[value], list[j]
    return list

#
# @param list -
# @param low -
# @param high -
# @param name -
# @return -
def binary_search(list, low, high, name):
    if high >= low:
        mid = (high + low) // 2
        if list[mid][1] == name:
            return mid
        elif list[mid][1] > name:
            return binary_search(list, low, mid-1, name)
        else:
            return binary_search(list, mid+1, high, name)
    else:
        return -1


def search(list):
    while True:
        try:
            name = str(input("Type a name: "))
            break
        except:
            print("Invalid input!")
    return binary_search(list, 0, len(list)-1, name)



# main

data = read_file()
#print(data)
s_list = sorter(data)
print(s_list)
while True:
    result = search(s_list)

    if result == -1:
        print('No Result')
    else:
        print(f'First Name: {s_list[result][0]}\nLast Name: {s_list[result][1]}\nAverage: {s_list[result][2]}')