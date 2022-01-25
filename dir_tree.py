import os
import sys

def print_directory(dir_path,depth:int):
    '''Question 9'''
    for directory in os.listdir(dir_path):
        if os.path.isdir(dir_path + directory):
            starting_string = ''
            for _ in range(depth):
                starting_string += '|--'
            print(starting_string +"|--",directory)
            print_directory(dir_path + directory + '/',depth + 1)
        else:
            starting_string = ''
            for _ in range(depth):
                starting_string += '|--'
            print(starting_string +"|--",directory)

if __name__ == "__main__":
    dir_path = sys.argv[1]
    print_directory(dir_path,0)