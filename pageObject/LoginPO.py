from selenium.webdriver.support.ui import Select

class LoginPage():
    textbox_username_id = "username"
    textbox_password_id = "password"
    btn_login_id = "Login"
    drp_Dis_id = "thepage:j_id3:disSel"
    drp_DisSite_id = "thepage:j_id3:siteSelect"
    btn_goto_id = "goto"
    btn_accpet_css = "#modalCon2 .slds-button_brand"

    def __init__(self,driver):
        self.driver = driver

    def EnterUsername(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def EnterPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def ClickLogin(self):
        self.driver.find_element_by_id(self.btn_login_id).click()

    def SelectDis(self,value):
        Disaster = Select(self.driver.find_element_by_id(self.drp_Dis_id))
        Disaster.select_by_visible_text(value)

    def SelectDisSite(self,value):
        Site = Select(self.driver.find_element_by_id(self.drp_DisSite_id))
        Site.select_by_visible_text(value)

    def ClickGoto(self):
        self.driver.find_element_by_id(self.btn_goto_id).click()

    def ClickAccept(self):
        self.driver.find_element_by_css_selector(self.btn_accpet_css).click()
