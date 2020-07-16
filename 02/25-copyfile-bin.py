def main():
    infile = open('02/bin.jpg', 'rb')
    outfile = open('02/bin-copy.jpg', 'wb')

    while True:
        # buffer size is 10KB
        buf = infile.read(10240)
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else:
            break
        
    outfile.close()
    print('\ndone.')

if __name__ == "__main__":
    main()
