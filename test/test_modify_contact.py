from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(
        first_name="Paulina",
        middle_name="Magda",
        last_name="Koziel",
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
    app.session.logout()
