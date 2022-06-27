import mysql.connector

from model.contact import Contact
from model.group import Group


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))

        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work,"
                           " email, email2, email3, address2, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work,
                 email, email2, email3, address2, phone2) = row
                list.append(Contact(id=str(id),first_name=firstname.strip(), middle_name=middlename,last_name=lastname,nickname=nickname,
                                    company=company,title=title,address=address, telephone_home=home, telephone_mobile=mobile,
                                    telephone_work=work, email=email, email2=email2, email3=email3, address2=address2,
                                    secondary_phone=phone2))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
