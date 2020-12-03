import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

class CreateHOH():

    btn_NewHHMem_xpath = "//runtime_platform_actions-custom-quick-action/slot/slot/lightning-button/button"
    txt_FN_xpath = "//div[@id='modal-content-id-1']/div[2]/div/div[3]/div/lightning-input/div/input"
    txt_LN_xpath = "//div[@id='modal-content-id-1']/div[2]/div/div[5]/div/lightning-input/div/input"
    txt_DOB_xpath = "//div[@id='dateF1']/div/div/input"
    drp_Gender_xpath = "//div[@id='modal-content-id-1']/div[2]/div/div[8]/div/div/div/div/select"
    txt_SSN_xpath = "//div[@id='modal-content-id-1']/div[2]/div/div[9]/div/lightning-input/div/input"
    btn_Save_xpath = "//button[3]"
    mess_HOH_Succ_css = ".toastMessage"

    def __init__(self,driver):
        self.driver = driver

    def ClickNewHHMem(self):
        self.driver.find_element_by_xpath(self.btn_NewHHMem_xpath).click()

    def EnterFN(self,FN):
        self.driver.find_element_by_xpath(self.txt_FN_xpath).send_keys(FN)

    def EnterLN(self,LN):
        self.driver.find_element_by_xpath(self.txt_LN_xpath).send_keys(LN)

    def EnterDOB(self,DOB):
        self.driver.find_element_by_xpath(self.txt_DOB_xpath).send_keys(DOB)

    def SelectGender(self,value):
        Gender = Select(self.driver.find_element_by_xpath(self.drp_Gender_xpath))
        Gender.select_by_visible_text(value)

    def EnterSSN(self,SSN):
        self.driver.find_element_by_xpath(self.txt_SSN_xpath).send_keys(SSN)

    def Click_Save(self):
        self.driver.find_element_by_xpath(self.btn_Save_xpath).click()

    def ToastMess(self):
        value = self.driver.find_element_by_css_selector(".toastMessage").text
        return value


