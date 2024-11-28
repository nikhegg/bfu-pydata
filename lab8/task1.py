import sqlite3

connection = sqlite3.connect("file.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS orders (
        order_code INTEGER PRIMARY KEY AUTOINCREMENT,
        recipient_id INTEGER NOT NULL,
        sender_id INTEGER NOT NULL,
        order_date DATE NOT NULL,
        order_delivery_date DATE,
        price FLOAT NOT NULL,
        carrier_id INTEGER,
        vehicle_id INTEGER
    );
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS vehicles (
        vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
        made TINYTEXT NOT NULL,
        register_date DATE NOT NULL,
        color TINYTEXT NOT NULL
    );
""")
connection.commit()

order = (21321, 1025, "21.10.2023", "27.10.2023", 3500, 102, 1)
cursor.execute("INSERT INTO orders(recipient_id, sender_id, order_date, order_delivery_date, price, carrier_id, vehicle_id) VALUES (?, ?, ?, ?, ?, ?, ?)", order)
car = ("Skoda", "23.11.2024", "Grey")
cursor.execute("INSERT INTO vehicles(made, register_date, color) VALUES (?, ?, ?)", car)
connection.commit()

cursor.execute("UPDATE orders SET price=3500.99 WHERE order_code=1")
cursor.execute("UPDATE vehicles SET color='Yellow' WHERE vehicle_id=1")
connection.commit()

connection.close()