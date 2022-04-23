# -*- coding: utf-8 -*-

from selenium.webdriver.support.ui import Select
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import Firefox
from contact import Contact
from test_add_group import TestAddGroup
import unittest


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = Firefox(executable_path=GeckoDriverManager().install())
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        test_add_group = TestAddGroup()
        wd = self.wd
        test_add_group.open_home_page(wd)
        test_add_group.login(self.wd, username="admin", password="secret")

        self.add_new_contact(wd, Contact(
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
        test_add_group.logout(wd)

    def add_new_contact(self, wd, contact):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").send_keys(contact.telephone_home)
        wd.find_element_by_name("mobile").send_keys(contact.telephone_mobile)
        wd.find_element_by_name("work").send_keys(contact.telephone_work)
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        self.get_birthday(wd, contact)
        self.get_anniversary(wd, contact)
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    @staticmethod
    def get_birthday(wd, contact):
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").send_keys(contact.byear)

    @staticmethod
    def get_anniversary(wd, contact):
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wd.find_element_by_name("ayear").send_keys(contact.ayear)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
