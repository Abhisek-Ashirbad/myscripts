#Program to count the number of times the code is executed.
# !pip install atexit

import atexit
from os import path
import os
from json import dumps, loads

def read_counter():
    return loads(open("counter.json", "r").read()) + 1 if path.exists("counter.json") else 1

def write_counter():
    with open("counter.json", "w") as f:
        f.write(dumps(counter))

counter = read_counter()
atexit.register(write_counter)

def main():
    # Create the directory if it doesn't already exist
    if not os.path.exists(str(counter)):
        os.makedirs(str(counter))
    
    filename = str(counter)+"log.txt"
    full_filename = os.path.join(str(counter), filename)
    with open(full_filename, "a") as file:
        file.write("Code has been run {} times".format(counter))

    print("Code has been run {} times".format(counter))

if __name__ == "__main__":
    main()
