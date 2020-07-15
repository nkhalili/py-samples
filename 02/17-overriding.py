class RevStr(str):
    def __str__(self):
        return self[::-1]


def main():
    # print(str('Hello'[::-1]))
    hello = RevStr('Hello')
    print(hello)


if __name__ == "__main__":
    main()
