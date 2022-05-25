from random import randrange

from model.contact import Contact


def test_modify_first_name_contact(app):
    contact = Contact(first_name="Katarzyna", last_name="Nowak")
    if app.contact.count() == 0:
        app.contact.add(contact)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    contact.first_name = "Paulina"
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_last_name_contact(app):
    contact = Contact(first_name="Karolina", last_name="Kowalska")
    if app.contact.count() == 0:
        app.contact.add(contact)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.last_name = 'Nowak'
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_modify_day_of_birth_contact(app):
#     if app.contact.count() == 0:
#         app.contact.add(Contact(first_name="Bartek", last_name="Os", bday="2", bmonth="January", byear="2000"))
#     app.contact.modify_first_contact(Contact(bday="1", bmonth="April", byear="1988"))
