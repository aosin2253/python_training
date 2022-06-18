# -*- coding: utf-8 -*-
import random
import string
from faker import Faker
import pytest

from model.contact import Contact

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
    for i in range(5)
]


@pytest.mark.parametrize('contact', testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add(contact=contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
