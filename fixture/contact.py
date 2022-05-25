from selenium.webdriver.support.select import Select

from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # select contact by index
        self.select_contact_by_index(index)
        self.open_contact_page()
        # submit deletion
        wd.find_element_by_css_selector("input[value='Delete']").click()
        self.open_home_page()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # edit contact
        self.open_contact_page()
        self.fill_contact_form(new_group_data)
        wd.find_element_by_name("update").click()
        self.open_home_page()
        self.contact_cache = None

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('img[alt="Edit"]:first-of-type').click()

    def open_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/"):
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

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def changed_date(self, day, month, year, field_day, field_month, field_year):
        wd = self.app.wd
        if year is not None:
            Select(wd.find_element_by_name(field_day)).select_by_visible_text(str(day))
            Select(wd.find_element_by_name(field_month)).select_by_visible_text(str(month))
            wd.find_element_by_name(field_year).clear()
            wd.find_element_by_name(field_year).send_keys(year)

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tbody tr[name='entry']"):
                last_name = element.find_element_by_css_selector("td:nth-of-type(2)").text
                first_name = element.find_element_by_css_selector("td:nth-of-type(3)").text
                id = element.find_element_by_name('selected[]').get_attribute("value")
                self.contact_cache.append(Contact(last_name=last_name, first_name=first_name, id=id))
        return list(self.contact_cache)
