from selenium.webdriver.support.ui import Select

class Interviewee():
    btn_MenuOptn_xpath = "//div[@id='brandBand_2']/div/div/div/div/one-record-home-flexipage2/forcegenerated-adgrollup_component___forcegenerated__flexipage_recordpage___household_record_page_single_col___dsnap_household__c___view/forcegenerated-flexipage_household_record_page_single_col_dsnap_household__c__view_js/record_flexipage-record-page-decorator/div/slot/flexipage-record-home-single-col-template-desktop2/div/div/slot/slot/flexipage-component2/slot/records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_dsnap_household__c___012000000000000aaa___compact___view___recordlayout2/force-highlights2/div/div/div[3]/div/runtime_platform_actions-actions-ribbon/ul/li[4]/lightning-button-menu/button"
    Optn_New_Inter_xpath = "//div[@id='brandBand_2']/div/div/div/div/one-record-home-flexipage2/forcegenerated-adgrollup_component___forcegenerated__flexipage_recordpage___household_record_page_single_col___dsnap_household__c___view/forcegenerated-flexipage_household_record_page_single_col_dsnap_household__c__view_js/record_flexipage-record-page-decorator/div/slot/flexipage-record-home-single-col-template-desktop2/div/div/slot/slot/flexipage-component2/slot/records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_dsnap_household__c___012000000000000aaa___compact___view___recordlayout2/force-highlights2/div/div/div[3]/div/runtime_platform_actions-actions-ribbon/ul/li[4]/lightning-button-menu/div/div/slot/runtime_platform_actions-action-renderer[2]/runtime_platform_actions-custom-quick-action/slot/slot/runtime_platform_actions-ribbon-menu-item/a/span"
    txt_SearchMem_xpath = "//div[@id='modal-content-id-1']/div[2]/div/div/div/div/div/div/div/div[2]/input"
    Optn_Mem_xpath = "//span[2]/span"
    drp_DocumentID_xpath = "//div[@id='modal-content-id-1']/div[2]/div/div[11]/div/div/div/div/select"
    btn_Save_xpath = "/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/div[2]/section/div/footer/button[3]"

    def __init__(self,driver):
        self.driver = driver

    def Click_MenuOptn(self):
        self.driver.find_element_by_xpath(self.btn_MenuOptn_xpath).click()

    def Click_New_Inter(self):
        self.driver.find_element_by_xpath(self.Optn_New_Inter_xpath).click()

    def Click_SearchMem(self):
        self.driver.find_element_by_xpath(self.txt_SearchMem_xpath).click()

    def Click_Mem(self):
        self.driver.find_element_by_xpath(self.Optn_Mem_xpath).click()

    def Select_DocID(self,value):
        Document = Select(self.driver.find_element_by_xpath(self.drp_DocumentID_xpath))
        Document.select_by_visible_text(value)

    def Click_Save(self):
        self.driver.find_element_by_xpath(self.btn_Save_xpath).click()