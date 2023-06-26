from selenium.webdriver.common.by import By


class KontaktHelper:
    def __init__(self, app):
        self.app = app

    def create(self, kontakt):
        wd = self.app.wd
        # init kontakt creation
        wd.find_element(By.LINK_TEXT, "add new").click()
        # fill kontakt firm
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(kontakt.first_name)
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(kontakt.mid_name)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(kontakt.last_name)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(kontakt.nick_name)
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys(kontakt.title)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(kontakt.company_name)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys(kontakt.address)
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys(kontakt.home_number)
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys(kontakt.e_mail)

        # submit kontakt creation
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()

    def modification(self, kontakt):
        wd = self.app.wd
        self.app.open_home_page()
        # # select first group
        wd.find_element(By.NAME, "selected[]").click()
        # click on Edit button
        wd.find_element(By.XPATH, "//img[@alt='Edit']").click()
        #  modification kontakt
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(kontakt.first_name)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(kontakt.last_name)
        wd.find_element(By.NAME, "update").click()




    def delete(self):
        wd = self.app.wd
        self.app.open_home_page()
        # # select first group
        wd.find_element(By.NAME, "selected[]").click()
        # # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        alert_obj = wd.switch_to.alert
        alert_obj.accept()
