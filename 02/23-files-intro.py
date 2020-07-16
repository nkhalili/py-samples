def main():
    # 'r':read, 'w':write, 'a':append
    # by default is in 'r' mode
    # + sign after file mode adds extra access e.g. r+ means read/write
    # b after + sign means binary, t means text mode (t is default)
    f = open('02/23-lines.txt', 'r+b')
    for line in f:
        # .rstrip() removes file ending characters e.g. \t\n
        print(line.rstrip())

if __name__ == "__main__":
    main()