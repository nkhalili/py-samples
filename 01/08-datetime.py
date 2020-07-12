from datetime import date
from datetime import time
from datetime import datetime


def main():
    # date object
    today = date.today()
    print("Today's date is: ", today)

    # print individual components
    print("Date components: ", today.day, today.month, today.year)

    print("Today's weekday # is ", today.weekday())

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    print("Which is: ", days[today.weekday()])

    # datetime object
    today = datetime.now()
    print("The current date/time is :", today)

    # get the current time
    t = datetime.time(datetime.now())
    print(t)


if __name__ == "__main__":
    main()
