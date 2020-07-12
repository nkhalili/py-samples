import urllib.request


def main():
    webUrl = urllib.request.urlopen("http://www.google.com")

    code = webUrl.getcode()
    print("Result code:", code)

    data = webUrl.read()
    print(data)


if __name__ == "__main__":
    main()
