from peewee import *
from datetime import date, time

# couriers, sender, recipients

db = SqliteDatabase("file.db")

class Couriers(Model):
    courier_id = PrimaryKeyField()
    surname = TextField()
    name = TextField()
    patronymic = TextField()
    passport = TextField()
    birth_date = DateField()
    hire_date = DateField()
    working_day_start = TimeField()
    working_day_end = TimeField()
    city = TextField()
    street = TextField()
    house_number = IntegerField()
    flat_number = IntegerField()
    phone_number = TextField()

    class Meta:
        database = db
        table_name = "couriers"

class Senders(Model):
    sender_id = PrimaryKeyField()
    surname = TextField()
    name = TextField()
    patronymic = TextField()
    birth_date = DateField()
    post_index = IntegerField()
    city = TextField()
    street = TextField()
    house_number = IntegerField()
    flat_number = IntegerField()
    phone_number = IntegerField()

    class Meta:
        database = db
        table_name = "senders"


class Recipients(Model):
    recipient_id = PrimaryKeyField()
    surname = TextField()
    name = TextField()
    patronymic = TextField()
    birth_date = DateField()
    post_index = IntegerField()
    city = TextField()
    street = TextField()
    house_number = IntegerField()
    flat_number = IntegerField()
    phone_number = IntegerField()

    class Meta:
        database = db
        table_name = "recipients"


db.connect()
db.create_tables([Couriers, Senders, Recipients])

Couriers.get_or_create(
    surname = "Ivanov",
    name = "Ivan",
    patronymic = "Ivanovich",
    passport=2210505032,
    birth_date=date(1989,5,10),
    hire_date=date(2010,9,28),
    working_day_start=time(10),
    working_day_end=time(22),
    city="New York",
    street="Main Street",
    house_number=21,
    flat_number=2,
    phone_number="88005553535"
)
Couriers.get_or_create(
    surname = "Nevers",
    name = "Alicia",
    patronymic = "",
    passport=99543198,
    birth_date=date(1999,7,1),
    hire_date=date(2018,10,5),
    working_day_start=time(18),
    working_day_end=time(2),
    city="New York",
    street="Copy Street",
    house_number=95,
    flat_number=23,
    phone_number="99116664646"
)

Senders.get_or_create(
    surname = "Ivanov",
    name = "Ivan",
    patronymic = "Ivanovich",
    birth_date=date(1989,5,10),
    post_index=880232,
    city="New York",
    street="Main Street",
    house_number=21,
    flat_number=2,
    phone_number="88005553535"
)
Senders.get_or_create(
    surname = "Nevers",
    name = "Alicia",
    patronymic = "",
    birth_date=date(1999,7,1),
    post_index=881023,
    city="New York",
    street="Copy Street",
    house_number=95,
    flat_number=23,
    phone_number="99116664646"
)

Recipients.get_or_create(
    surname = "Petrov",
    name = "Petr",
    patronymic = "Petrovich",
    birth_date=date(2001,2,16),
    post_index=882200,
    city="New York",
    street="End Street",
    house_number=1,
    flat_number=65,
    phone_number="43821605449"
)
Recipients.get_or_create(
    surname = "Evers",
    name = "Michael",
    patronymic = "Jordan",
    birth_date=date(1965,2,19),
    post_index=879789   ,
    city="New York",
    street="Third Table Street",
    house_number=3,
    flat_number=3,
    phone_number="76574345235"
)

db.close()