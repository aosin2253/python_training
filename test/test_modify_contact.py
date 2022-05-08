

def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(name="Test", lastname="Test")
    app.session.logout()
