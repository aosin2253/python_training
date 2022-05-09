from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(first_name="Bartek", last_name="Os"))
    app.contact.delete_first_contact()


