from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def fill_group_form(self, group):

        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element(By.NAME, "selected[]").click()
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()

    def modification_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # modification
        wd.find_element(By.NAME, "edit").click()
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys("monkey")
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys("cats")
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys("dogs")
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def modify_first_group(self, new_group_date):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()

        #     open modification form
        wd.find_element(By.NAME, "edit").click()
        # fill group form
        self.fill_group_form(new_group_date)
        # submit modification
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()
