import xml.dom.minidom

def main():
    # use the parse() function to load and parse an XML file
    doc = xml.dom.minidom.parse("Data_Pulling_125w.xml");

    print (doc.nodeName)
    print (doc.firstChild.tagName)

if __name__ == "__main__":
    main();