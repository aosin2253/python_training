# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(
        first_name="Anna",
        middle_name="Magda",
        last_name="J",
        nickname="aosin",
        title="test",
        company="Test",
        address="Polna 1/244",
        telephone_home="221231212",
        telephone_mobile="123123123",
        telephone_work="111111111",
        email="test@test.test",
        email2="testowy@test.com",
        email3="test123@test.pl",
        homepage="test",
        bday="2",
        bmonth="February",
        byear="1999",
        aday="3",
        amonth="January",
        ayear="2000",
        address2="Lesna 2"
    )
    app.contact.add(contact=contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)

    assert sorted(old_contacts, key=lambda x: x.last_name) == new_contacts
