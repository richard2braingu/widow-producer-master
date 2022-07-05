from uci import XMLParser
with open("amtiExample.xml", "rb") as f:
    root = XMLParser().parse_object(f.read())
print(root)