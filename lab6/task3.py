import xml.etree.ElementTree as ETree

tree = ETree.parse("ex_3.xml")
root = tree.getroot()

for item in root.findall("Документ/ТаблСчФакт/СведТов"):
    print(f"Наименование: {item.get('НаимТов')}\nКоличество: {item.get('КолТов')}\nЦена: {item.get('ЦенаТов')}\n")