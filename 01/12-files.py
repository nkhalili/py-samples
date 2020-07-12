def main():
    # Open a file for writing, create it if doesn't exist
    # f = open("textfile.txt", "w+")

    # Open a file for appendding text to the end
    # f = open("textfile.txt", "a")

    f = open("textfile.txt", "r")

    # write some data into it
    # for i in range(10):
    #    f.write("This is line " + str(i) + "\n")

    # Open the file and read its content
    # Check f.mode to make sure the file has successfully opened
    if f.mode == 'r':
        ## read all lines
        #contents = f.read() 
        #print(contents)
        ## read line by line
        fl = f.readlines()
        for l in fl:
            print(l)

    # close the file when done
    f.close()


if __name__ == "__main__":
    main()
