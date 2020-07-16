def main():
    infile = open('02/23-lines.txt', 'rt')
    outfile = open('02/23-lines-copy.txt', 'wt')
    for line in infile:
        # two ways to write in the outfile 1. writelines() 2. print
        outfile.writelines(line)
        # the only difference using print is you can use default file ending of os by using rstrip()
        # print(line.rstrip(), file=outfile)
        print('.', end='', flush=True)
    outfile.close()
    # for infile it is not really important to close it
    # because we are reading from it, when main exits it will happen automatically
    # infile.close()
    print('\ndone.')


if __name__ == "__main__":
    main()
