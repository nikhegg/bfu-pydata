from xmlschema import XMLSchema

schema = XMLSchema("ex_1.xsd")
if schema.is_valid("ex_1_err.xml"):
    print("Файл прошёл валидацию")
else:
    print("Файл не прошёл валидацию")