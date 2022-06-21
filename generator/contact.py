import random
import string
import os.path
import jsonpickle
import getopt
import sys

from faker import Faker

from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
        print(n)
    elif o == "-f":
        f = a

fake = Faker(locale="pl_PL")


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_data(prefix, index):
    data_list = []
    first_name = fake.first_name()
    last_name = fake.last_name()
    address = fake.address()
    phone = fake.phone_number()
    email = fake.email()
    data_list.extend((first_name, last_name, address, phone, email))
    return prefix + "" + data_list[index]


testdata = [
    Contact(first_name=random_data('name', 0), middle_name=random_data('middle_name', 0),
            last_name=random_data('last_name', 1), nickname=random_string("nick_name", 10),
            company=random_string("company", 10), title=random_string("title", 10), address=random_data("address", 2),
            telephone_home=random_data("home", 3), telephone_mobile=random_data("mobile", 3),
            telephone_work=random_data("work", 3),
            email=random_data("email", 4), email2=random_data("email2", 4), email3=random_data("email3", 4),
            address2=random_data("address2", 2), secondary_phone=random_data("phone2", 3))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
