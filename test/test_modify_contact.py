from model.contact import Contact


def test_modify_first_name_contact(app):
    app.contact.modify_first_contact(Contact(first_name="Test"))


def test_modify_last_name_contact(app):
    app.contact.modify_first_contact(Contact(last_name="Test2"))


def test_modify_day_of_birth_contact(app):
    app.contact.modify_first_contact(Contact(bday="1", bmonth="April", byear="1988"))
