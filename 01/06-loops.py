def main():
    x = 0

    # in python we have two loops. while, for
    # both supports break, continue statements

    # define a while loop
    while(x < 5):
        print(x)
        x += 1

    # define a for loop, similar to foreach, you can add Index
    for x in range(5, 10):
        print(x)

    # break
    for x in range(5, 10):
        if(x == 7):
            break
        print(x)

    # continue
    for i, x in enumerate(range(5, 10)):
        if(x % 2 == 0):
            continue
        print(i, x)

    # use a for loop over a collection
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for day in days:
        print(day)

    # add Index, using enumerate()
    for i, day in enumerate(days):
        print(i, day)


if __name__ == "__main__":
    main()
