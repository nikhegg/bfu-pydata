from jsonschema import validate
import json

with open("ex_1_err.json") as file, open("ex_1.schema.json") as schema:
    try:
        validate(json.load(file), json.load(schema))
        print("Файл прошёл валидацию")
    except:
        print("Файл не прошёл валидацию")