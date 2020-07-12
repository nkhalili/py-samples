import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # print the name of os
    print(os.name)

    # check if file exists and check its type
    print("Item exists: " + str(path.exists("textfile.txt")))
    print("Item is a file: " + str(path.isfile("textfile.txt")))
    print("Item is a directory: " + str(path.isdir("textfile.txt")))

    # work with file paths
    print("Item path: " + str(path.realpath("textfile.txt")))
    print("Item path and name: " + str(path.split(path.realpath("textfile.txt"))))

    # Get the modification time of the file
    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    # calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It's been " + str(td) + " since the file was modified")
    print("Or, " + str(td.total_seconds()) + " seconds")


if __name__ == "__main__":
    main()
