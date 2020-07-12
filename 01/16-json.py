import urllib.request
import json


def printResults(data):
    theJSON = json.loads(data)

    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    count = theJSON["metadata"]["count"]
    print(count, "events recorded")
    print("---------------\n")

    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
    print("---------------\n")

    print("Events that were felt: ")
    for i in theJSON["features"]:
        feltReport = i["properties"]["felt"]
        if feltReport != None:
            if feltReport > 0:
                print("%2.1f" % i["properties"]["mag"], i["properties"]
                      ["place"], "reported", feltReport, "times")


def main():
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    webUrl = urllib.request.urlopen(urlData)
    print("Result code:", webUrl.getcode())

    if(webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("Cannot parse results")


if __name__ == "__main__":
    main()
