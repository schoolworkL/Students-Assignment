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
    for i in range(len(list)-1, 0, -1):  # iterates through the list backwards
        value = 0  # variable to the second value
        for j in range(1, i+1):  # iterates through the list using i+1 as the end range
            if list[j][1] > list[value][1]:  # checks if the second value in the tuple is greater than the second value in the second tuple
                value = j # sets value to equal j
        list[j], list[value] = list[value], list[j]  # switches the values of list[j] and list[value]
    return list  # returns the sorted list to the main

# User inputs a last name, then the search function is returned to the main
# @param list - holds the data in tuples within a list
# @return binary_search(list, 0, len(list)-1, name) - runs the binary_search function with the list of data, range of data, and input value
def search(list):
    while True: # loops for catching bad inputs
        try:
            name = str(input("Type a name: "))
            break  # breaks the loop after a good input
        except:
            print("Invalid input!")  # error message
    return Search.binary_search(list, 0, len(list)-1, name)  # runs the function to search through the data

# class for searching for user input in data
class Search:
    # Search for an last name input in the data from the file
    # @param list - holds the data in tuples in a list
    # @param low - the bottom extent of the data to be analyzed
    # @param high - the top extent of the data to be analyzed
    # @param name - the input value(last name)
    # @return binary_search(list, mid+1, high, name) - runs the binary_search function with a new low value
    # @return binary_search(list, low, mid-1, name) - runs the binary_search function with a new high value
    # @return -1 - returns the value of -1 to the main. Tells the main that the input was not found in the data
    def binary_search(list, low, high, name):
        if high >= low:  # checks if the ceiling of the list is greater than or equal to the floor of the list
            mid = (high + low) // 2  # gets the middle value using floor division
            if list[mid][1] == name:  # checks if the middle value is the input value
                return mid  # returns the tuple to the search function
            elif list[mid][1] > name:  # checks if the input value is below the middle value
                return Search.binary_search(list, low, mid-1, name)  # runs the binary_search function with a new range for the list of data
            else:  # the input value must be above the middle value
                return Search.binary_search(list, mid+1, high, name)  # runs the binary_search function with a new range for the list of data
        else:
            return -1  # returns the not present value

# main

data = read_file() # gets the data from the file
s_list = sorter(data)  # sorts the data
print(*[' '.join(i) for i in s_list], sep='\n')  # prints each tuple on an individual line
while True:
    result = search(s_list)  # stores the result of searching for a name

    if result == -1:  # if result == -1, then the name was not in the data
        print('No Result')
    else:
        print(f'First Name: {s_list[result][0]}\nLast Name: {s_list[result][1]}\nAverage: {s_list[result][2]}')  # prints the data