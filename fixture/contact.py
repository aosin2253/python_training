from selenium.webdriver.support.select import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        self.open_contact_page()
        # submit deletion
        wd.find_element_by_css_selector("input[value='Delete']").click()
        self.return_to_home_page()

    def modify_first_contact(self, new_group_data):
        wd = self.app.wd
        self.select_first_contact()
        # edit contact
        self.open_contact_page()
        self.fill_contact_form(new_group_data)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('img[alt="Edit"]:first-of-type').click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def fill_contact_form(self, contact):
        self.change_field_value(field_name="firstname", text=contact.first_name)
        self.change_field_value(field_name="middlename", text=contact.middle_name)
        self.change_field_value(field_name="lastname", text=contact.last_name)
        self.change_field_value(field_name="nickname", text=contact.nickname)
        self.change_field_value(field_name="title", text=contact.title)
        self.change_field_value(field_name="company", text=contact.company)
        self.change_field_value(field_name="address", text=contact.address)
        self.change_field_value(field_name="home", text=contact.telephone_home)
        self.change_field_value(field_name="mobile", text=contact.telephone_mobile)
        self.change_field_value(field_name="work", text=contact.telephone_work)
        self.change_field_value(field_name="email", text=contact.email)
        self.change_field_value(field_name="email2", text=contact.email2)
        self.change_field_value(field_name="email3", text=contact.email3)
        self.change_field_value(field_name="homepage", text=contact.homepage)
        self.changed_date(field_day="bday", field_month="bmonth", field_year="byear",
                          day=contact.bday, month=contact.bmonth, year=contact.byear)
        self.changed_date(field_day="aday", field_month="amonth", field_year="ayear",
                          day=contact.aday, month=contact.amonth, year=contact.ayear)
        self.change_field_value(field_name="address2", text=contact.address2)

    def change_field_value(self, text, field_name):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def changed_date(self, day, month, year, field_day, field_month, field_year):
        wd = self.app.wd
        if year is not None:
            Select(wd.find_element_by_name(field_day)).select_by_visible_text(str(day))
            Select(wd.find_element_by_name(field_month)).select_by_visible_text(str(month))
            wd.find_element_by_name(field_year).clear()
            wd.find_element_by_name(field_year).send_keys(year)
