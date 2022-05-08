from selenium.webdriver.support.select import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add(self, contact):
        wd = self.app.wd
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
        self.get_birthday(contact)
        self.get_anniversary(contact)
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        self.open_contact_page()
        # submit deletion
        wd.find_element_by_css_selector("input[value='Delete']").click()
        self.return_to_home_page()

    def modify_first_contact(self, name, lastname):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # edit contact
        self.open_contact_page()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(lastname)
        # update contact firstname and lastname
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def get_birthday(self, contact):
        wd = self.app.wd
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").send_keys(contact.byear)

    def get_anniversary(self, contact):
        wd = self.app.wd
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wd.find_element_by_name("ayear").send_keys(contact.ayear)

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('img[alt="Edit"]:first-of-type').click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
