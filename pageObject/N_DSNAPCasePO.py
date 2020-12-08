class N_DSNAPCase():

    btn_MenuOptn_xpath = "//div[@id='brandBand_2']/div/div/div/div/one-record-home-flexipage2/forcegenerated-adgrollup_component___forcegenerated__flexipage_recordpage___household_record_page_single_col___dsnap_household__c___view/forcegenerated-flexipage_household_record_page_single_col_dsnap_household__c__view_js/record_flexipage-record-page-decorator/div/slot/flexipage-record-home-single-col-template-desktop2/div/div/slot/slot/flexipage-component2/slot/records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_dsnap_household__c___012000000000000aaa___compact___view___recordlayout2/force-highlights2/div/div/div[3]/div/runtime_platform_actions-actions-ribbon/ul/li[4]/lightning-button-menu/button"
    Optn_New_DSNAPC_xpath = "//div[@id='brandBand_2']/div/div/div/div/one-record-home-flexipage2/forcegenerated-adgrollup_component___forcegenerated__flexipage_recordpage___household_record_page_single_col___dsnap_household__c___view/forcegenerated-flexipage_household_record_page_single_col_dsnap_household__c__view_js/record_flexipage-record-page-decorator/div/slot/flexipage-record-home-single-col-template-desktop2/div/div/slot/slot/flexipage-component2/slot/records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_dsnap_household__c___012000000000000aaa___compact___view___recordlayout2/force-highlights2/div/div/div[3]/div/runtime_platform_actions-actions-ribbon/ul/li[4]/lightning-button-menu/div/div/slot/runtime_platform_actions-action-renderer[3]/runtime_platform_actions-custom-quick-action/slot/slot/runtime_platform_actions-ribbon-menu-item/a/span"
    txt_DisName_xpath = "//div[@id='modal-content-id-1']/div[2]/div/div[2]/div/div/div/div/div/div[2]/input"
    Optn_DisSel_xpath = "//span[2]/span"
    txt_InterName_xpath = "//div[@id='modal-content-id-1']/div[2]/div/div[3]/div/div/div/div/div/div[2]/input"
    Optn_InterSel_xpath = "//div[3]/div/div/div/div[2]/ul/li/span/span[2]/span"

    def __init__(self,driver):
        self.driver = driver

    def Click_MenuOptn(self):
        self.driver.find_element_by_xpath(self.btn_MenuOptn_xpath).click()

    def Click_New_DSNAPC(self):
        self.driver.find_element_by_xpath(self.Optn_New_DSNAPC_xpath).click()

    def Click_DisName(self,DisName):
        self.driver.find_element_by_xpath(self.txt_DisName_xpath).send_keys(DisName)

    def Sel_DisName(self):
        self.driver.find_element_by_xpath(self.Optn_DisSel_xpath).click()

    def Click_IntSel(self):
        self.driver.find_element_by_xpath(self.txt_InterName_xpath).click()

    def Click_OptnIntSel(self):
        self.driver.find_element_by_xpath(self.Optn_InterSel_xpath).click()
