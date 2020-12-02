from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class CreateHHPO():

    btn_New_Link_text = "New"
    drp_Ishomeless_xpath = "//lightning-combobox/div/lightning-base-combobox/div/div/input"
    drp_Ishomeless_N_xpath = "//lightning-base-combobox-item[3]/span[2]"
    txt_ResiAdd_Str1_xpath = "//force-record-layout-base-input/lightning-input/div/input"
    txt_ResiAdd_Str2_xpath = "//force-record-layout-item[2]/div/span/slot/slot/force-record-layout-base-input/lightning-input/div/input"
    txt_ResiAdd_City_xpath = "//force-record-layout-row[3]/slot/force-record-layout-item/div/span/slot/slot/force-record-layout-base-input/lightning-input/div/input"
    txt_ResiAdd_ZipCode_xpath  = "//force-record-layout-row[3]/slot/force-record-layout-item[2]/div/span/slot/slot/force-record-layout-base-input/lightning-input/div/input"
    drp_POO_xpath = "//force-record-layout-item[2]/div/span/slot/slot/force-record-picklist/force-form-picklist/lightning-picklist/lightning-combobox/div/lightning-base-combobox/div/div/input"
    drp_POO_Acdia_xpath = "//force-record-layout-item[2]/div/span/slot/slot/force-record-picklist/force-form-picklist/lightning-picklist/lightning-combobox/div/lightning-base-combobox/div/div[2]/lightning-base-combobox-item[2]/span[2]"
    drp_MailAdd_Same_ResiAdd_xpath = "//force-record-layout-row[5]/slot/force-record-layout-item/div/span/slot/slot/force-record-picklist/force-form-picklist/lightning-picklist/lightning-combobox/div/lightning-base-combobox/div/div/input"
    drp_MailAdd_Same_ResiAdd_Y_xpath = "//force-record-layout-row[5]/slot/force-record-layout-item/div/span/slot/slot/force-record-picklist/force-form-picklist/lightning-picklist/lightning-combobox/div/lightning-base-combobox/div/div[2]/lightning-base-combobox-item[2]/span[2]"
    lbl_MailAdd_Str1_xpath = "/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/records-lwc-detail-panel/records-base-record-form/div/div/div/div/records-record-layout-event-broker/slot/records-lwc-record-layout/forcegenerated-detailpanel_dsnap_household__c___012000000000000aaa___full___create___recordlayout2/force-record-layout-block/slot/force-record-layout-section[2]/div/div/div/slot/force-record-layout-row[6]/slot/force-record-layout-item[2]/div/span/slot/slot/force-record-layout-base-input/lightning-input/label"
    drp_Rec_SNAP_xpath = "//force-record-layout-section[3]/div/div/div/slot/force-record-layout-row/slot/force-record-layout-item/div/span/slot/slot/force-record-picklist/force-form-picklist/lightning-picklist/lightning-combobox/div/lightning-base-combobox/div/div/input"
    drp_Rec_SNAP_N_xpath = "//force-record-layout-section[3]/div/div/div/slot/force-record-layout-row/slot/force-record-layout-item/div/span/slot/slot/force-record-picklist/force-form-picklist/lightning-picklist/lightning-combobox/div/lightning-base-combobox/div/div[2]/lightning-base-combobox-item[3]"
    drp_Mem_DCFSEmp_xpath = "//force-record-layout-section[3]/div/div/div/slot/force-record-layout-row/slot/force-record-layout-item[2]/div/span/slot/slot/force-record-picklist/force-form-picklist/lightning-picklist/lightning-combobox/div/lightning-base-combobox/div/div/input"
    drp_Mem_DCFSEmp_N_xpath = "//force-record-layout-section[3]/div/div/div/slot/force-record-layout-row/slot/force-record-layout-item[2]/div/span/slot/slot/force-record-picklist/force-form-picklist/lightning-picklist/lightning-combobox/div/lightning-base-combobox/div/div[2]/lightning-base-combobox-item[3]/span[2]"
    lbl_SNAPState_xpath = "/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/records-lwc-detail-panel/records-base-record-form/div/div/div/div/records-record-layout-event-broker/slot/records-lwc-record-layout/forcegenerated-detailpanel_dsnap_household__c___012000000000000aaa___full___create___recordlayout2/force-record-layout-block/slot/force-record-layout-section[3]/div/div/div/slot/force-record-layout-row[2]/slot/force-record-layout-item[1]/div/span/slot/slot/force-record-picklist/force-form-picklist/lightning-picklist/lightning-combobox/label"
    drp_Auth_Rep_xpath = "//force-record-layout-row[3]/slot/force-record-layout-item/div/span/slot/slot/force-record-picklist/force-form-picklist/lightning-picklist/lightning-combobox/div/lightning-base-combobox/div/div/input"
    drp_Auth_Rep_N_xpath = "//force-record-layout-row[3]/slot/force-record-layout-item/div/span/slot/slot/force-record-picklist/force-form-picklist/lightning-picklist/lightning-combobox/div/lightning-base-combobox/div/div/lightning-base-combobox-item[3]/span[2]"
    btn_Save_xpath = "/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/records-lwc-detail-panel/records-base-record-form/div/div/div/force-form-footer/div/lightning-button[3]/button"

    def __init__(self,driver):
        self.driver = driver

    def Click_New(self):
        self.driver.find_element_by_link_text(self.btn_New_Link_text).click()

    def Click_IsHomless(self):
        self.driver.find_element_by_xpath(self.drp_Ishomeless_xpath).click()

    def Click_IsHomless_N(self):
        self.driver.find_element_by_xpath(self.drp_Ishomeless_N_xpath).click()

    def Enter_ResAdd_Str1(self,ResAddstr1):
        self.driver.find_element_by_xpath(self.txt_ResiAdd_Str1_xpath).send_keys(ResAddstr1)

    def Enter_ResAdd_Str2(self,ResAddstr2):
        self.driver.find_element_by_xpath(self.txt_ResiAdd_Str2_xpath).send_keys(ResAddstr2)

    def Enter_ResAdd_City(self,ResAddCity):
        self.driver.find_element_by_xpath(self.txt_ResiAdd_City_xpath).send_keys(ResAddCity)

    def Enter_ResAdd_ZipC(self,ResAddZip):
        self.driver.find_element_by_xpath(self.txt_ResiAdd_ZipCode_xpath).send_keys(ResAddZip)

    def Click_POO(self):
        self.driver.find_element_by_xpath(self.drp_POO_xpath).click()

    def Click_POO_Acadia(self):
        self.driver.find_element_by_xpath(self.drp_POO_Acdia_xpath).click()

    def Click_MailAdd_Same(self):
        self.driver.find_element_by_xpath(self.drp_MailAdd_Same_ResiAdd_xpath).click()

    def Click_MailAdd_Same_Y(self):
        self.driver.find_element_by_xpath(self.drp_MailAdd_Same_ResiAdd_Y_xpath).click()

    def Click_MailAdd_Str2(self):
        self.driver.find_element_by_xpath(self.lbl_MailAdd_Str1_xpath).click()

    def Click_Rec_SNAP(self):
        self.driver.find_element_by_xpath(self.drp_Rec_SNAP_xpath).click()

    def Click_Rec_SNAP_N(self):
        self.driver.find_element_by_xpath(self.drp_Rec_SNAP_N_xpath).click()

    def Click_Mem_DCFS(self):
        self.driver.find_element_by_xpath(self.drp_Mem_DCFSEmp_xpath).click()

    def Click_Mem_DCFS_N(self):
        self.driver.find_element_by_xpath(self.drp_Mem_DCFSEmp_N_xpath).click()

    def Click_SNAPState(self):
        self.driver.find_element_by_xpath(self.lbl_SNAPState_xpath).click()

    def Click_AuthRep(self):
        self.driver.find_element_by_xpath(self.drp_Auth_Rep_xpath).click()

    def Click_AuthRep_N(self):
        self.driver.find_element_by_xpath(self.drp_Auth_Rep_N_xpath).click()

    def Click_Save(self):
        self.driver.find_element_by_xpath(self.btn_Save_xpath).click()
