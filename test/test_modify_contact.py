import random
import time


from model.contact import Contact


def test_modify_first_name_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(first_name="Katarzyna"))
    old_contacts = db.get_contact_list()
    contact_data = Contact(first_name="Marta")
    contact = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact.id, contact_data)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_last_name_contact(app, db, check_ui):
    contact = Contact(first_name="Karolina", last_name="Kowalska")
    if len(db.get_contact_list()) == 0:
        app.contact.add(contact)
    old_contacts = db.get_contact_list()
    contact_data = Contact(last_name="Nowak")
    contact = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact.id, contact_data)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

