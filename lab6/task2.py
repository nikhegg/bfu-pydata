import xml.etree.ElementTree as ETree

tree = ETree.parse("ex_2.xml")
root = tree.getroot()


item = ETree.Element("Item")
ETree.SubElement(item, "ArtName").text = "Сыр Чеддер"
ETree.SubElement(item, "Barcode").text = "2000000000152"
ETree.SubElement(item, "QNT").text = "236,9"
ETree.SubElement(item, "QNTPack").text = "236,9"
ETree.SubElement(item, "Unit").text = "шт"
ETree.SubElement(item, "SN1").text = "00000015"
ETree.SubElement(item, "SN2").text = "22.05.2021"
ETree.SubElement(item, "QNTRows").text = "17"
root.find("Detail").append(item)

summ = 0
summ_rows = 0
for item in root.findall("Detail/Item"):
    item_qnt = item.find("QNT").text.replace(",", ".")
    item_rows = item.find("QNTRows").text

    summ += float(item_qnt)
    summ_rows = int(item_rows)
root.find("Summary/Summ").text = str(summ).replace(".", ",")
root.find("Summary/SummRows").text = str(summ_rows)

ETree.indent(tree, '    ')
tree.write("ex_2_upd.xml", encoding="UTF-8", xml_declaration=True)