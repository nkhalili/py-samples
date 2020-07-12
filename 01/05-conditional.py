def main():
    x, y = 100, 100

    # conditional flow, uses if, elif, else. python DOES NOT have switch/case statement
    if(x < y):
        st = "x is less than y"
    elif(x == y):
        st = "x is equal to y"
    else:
        st = "x is greater than y"
    print(st)

    # conditional statement (like ternary operator) python DOES NOT have ? :
    st = "x is less than y" if (
        x < y) else "x is greater than or the same as y"

    print(st)


if __name__ == "__main__":
    main()
