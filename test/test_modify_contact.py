from model.contact import Contact


def test_modify_first_name_contact(app):
    contact = Contact(first_name="Katarzyna", last_name="Nowak")
    if app.contact.count() == 0:
        app.contact.add(contact)
    old_contacts = app.contact.get_contact_list()
    contact.first_name = "Paulina"
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert len(old_contacts) == app.contact.count()
    old_contacts[0] = contact

    assert sorted(old_contacts, key=lambda x: x.last_name) == sorted(new_contacts, key=lambda x: x.last_name)


def test_modify_last_name_contact(app):
    contact = Contact(first_name="Karolina", last_name="Kowalska")
    if app.contact.count() == 0:
        app.contact.add(contact)
    old_contacts = app.contact.get_contact_list()
    contact.last_name = "Nowak"
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[0] = contact

    assert sorted(old_contacts, key=lambda x: x.last_name) == sorted(new_contacts, key=lambda x: x.last_name)


def test_modify_day_of_birth_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(first_name="Bartek", last_name="Os", bday="2", bmonth="January", byear="2000"))
    app.contact.modify_first_contact(Contact(bday="1", bmonth="April", byear="1988"))
