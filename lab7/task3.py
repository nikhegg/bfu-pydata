import json

with open("ex_3.json", "r") as file, open("ex_3_result.json", "w") as res:
    data = json.load(file)

    invoice = {"id": 3, "total": 0.0, "items": [{"name":" item 4", "quantity": 1, "price": 10.0}]}

    for item in invoice["items"]:
        invoice["total"] += item["price"] * item["quantity"]

    data["invoices"].append(invoice)
    json.dump(data, res, indent=2)