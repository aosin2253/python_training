import re

from model.contact import Contact


def test_contact_on_home_page(app, db):
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()

    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)


def test_phones_on_contact_view_page(app):
    contact_from_home_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.telephone_home == contact_from_edit_page.telephone_home
    assert contact_from_home_page.telephone_mobile == contact_from_edit_page.telephone_mobile
    assert contact_from_home_page.telephone_work == contact_from_edit_page.telephone_work
    assert contact_from_home_page.secondary_phone == contact_from_edit_page.secondary_phone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x),
                                                   filter(lambda x: x is not None,
                                                          [contact.telephone_home, contact.telephone_mobile,
                                                           contact.telephone_work, contact.secondary_phone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",  map(lambda x: x.replace(" ", ""), filter(lambda x: x is not None,
                                                      [contact.email, contact.email2,
                                                       contact.email3]))))
