import xml.dom.minidom


def main():
    doc = xml.dom.minidom.parse("sample.xml")

    print(doc.nodeName)
    print(doc.firstChild.tagName)

    read(doc)

    # add data into xml in memory
    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name", "jQuery")
    doc.firstChild.appendChild(newSkill)

    read(doc)

def read(doc):
    skills = doc.getElementsByTagName("skill")
    print("%d skills:" % skills.length)
    for skill in skills:
        print("\t", skill.getAttribute("name"))

if __name__ == "__main__":
    main()
