from datetime import datetime


def main():
    now = datetime.now()

    # %y/%Y - Year, %a/%A - Weekday, %b/%B - month, %d - day of month
    print(now.strftime("%a, %d %B, %y"))
    
    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("Locale date and time: %c"))
    print(now.strftime("Locale date: %x"))
    print(now.strftime("Locale time: %X"))

    ## Time formatting
    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("Current time: %I:%M:%S %p"))

if __name__ == "__main__":
    main()
