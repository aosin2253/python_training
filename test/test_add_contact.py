# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):

    app.contact.add(Contact(
        first_name="Anna",
        middle_name="Magda",
        last_name="Os",
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
    ))
