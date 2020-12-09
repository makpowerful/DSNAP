from selenium.webdriver.support.ui import Select

class DC_CertPO():
    tab_VR_xpath = "//a[contains(text(),'Voter Registration')]"
    drp_VRQ1_xpath = "//select"
    drp_VRQ2_xpath = "//div[5]/div/div/div/select"
    p_UnderVRQ2_xpath = "//textarea"
    btn_VRSave_xpath = "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/one-record-home-flexipage2/forcegenerated-adgrollup_component___forcegenerated__flexipage_recordpage___dsnap_program_record_page_single_col___dsnap_case__c___view/forcegenerated-flexipage_dsnap_program_record_page_single_col_dsnap_case__c__view_js/record_flexipage-record-page-decorator/div[1]/slot/flexipage-record-home-single-col-template-desktop2/div/div[2]/div/slot/slot/flexipage-component2/slot/flexipage-tabset2/div/lightning-tabset/div/slot/slot/slot/flexipage-tab2[2]/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/div/div[5]/button[1]"
    tab_DID_xpath = "//a[contains(text(),'Disaster Impact Details')]"
    drp_DIDQ1_xpath = "//div[2]/div/div/div/select"
    drp_DIDQ2_xpath = "//div[4]/div/div/div/select"
    drp_DIDQ3_xpath = "//div[6]/div/div/div/select"
    drp_DIDQ4_xpath = "//div[8]/div/div/div/select"
    drp_DIDQ5_xpath = "//div[10]/div/div/div/select"
    drp_DIDQ6_xpath = "//div[12]/div/div/div/select"
    txt_DIDQ7_xpath = "//textarea"
    txt_DIDQ8_xpath = "//div[16]/lightning-textarea/div/textarea"
    txt_DIDQ9_xpath = "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div[5]/div/one-record-home-flexipage2/forcegenerated-adgrollup_component___forcegenerated__flexipage_recordpage___dsnap_program_record_page_single_col___dsnap_case__c___view/forcegenerated-flexipage_dsnap_program_record_page_single_col_dsnap_case__c__view_js/record_flexipage-record-page-decorator/div[1]/slot/flexipage-record-home-single-col-template-desktop2/div/div[2]/div/slot/slot/flexipage-component2/slot/flexipage-tabset2/div/lightning-tabset/div/slot/slot/slot/flexipage-tab2[3]/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/div/div[2]/div[18]/lightning-input/div/input"
    btn_DIDSave_xpath = "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/one-record-home-flexipage2/forcegenerated-adgrollup_component___forcegenerated__flexipage_recordpage___dsnap_program_record_page_single_col___dsnap_case__c___view/forcegenerated-flexipage_dsnap_program_record_page_single_col_dsnap_case__c__view_js/record_flexipage-record-page-decorator/div[1]/slot/flexipage-record-home-single-col-template-desktop2/div/div[2]/div/slot/slot/flexipage-component2/slot/flexipage-tabset2/div/lightning-tabset/div/slot/slot/slot/flexipage-tab2[3]/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/div/div[3]/button[1]"
    tab_RR_xpath = "//a[contains(text(),'Rights & Responsibilities')]"
    chk_RRQ1_xpath = "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div[5]/div/one-record-home-flexipage2/forcegenerated-adgrollup_component___forcegenerated__flexipage_recordpage___dsnap_program_record_page_single_col___dsnap_case__c___view/forcegenerated-flexipage_dsnap_program_record_page_single_col_dsnap_case__c__view_js/record_flexipage-record-page-decorator/div[1]/slot/flexipage-record-home-single-col-template-desktop2/div/div[2]/div/slot/slot/flexipage-component2/slot/flexipage-tabset2/div/lightning-tabset/div/slot/slot/slot/flexipage-tab2[4]/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/article[2]/div[2]/article/div[2]/div[2]/div[8]/div/div/div/input"
    chk_RRQ2_xpath = "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div[5]/div/one-record-home-flexipage2/forcegenerated-adgrollup_component___forcegenerated__flexipage_recordpage___dsnap_program_record_page_single_col___dsnap_case__c___view/forcegenerated-flexipage_dsnap_program_record_page_single_col_dsnap_case__c__view_js/record_flexipage-record-page-decorator/div[1]/slot/flexipage-record-home-single-col-template-desktop2/div/div[2]/div/slot/slot/flexipage-component2/slot/flexipage-tabset2/div/lightning-tabset/div/slot/slot/slot/flexipage-tab2[4]/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/article[2]/div[2]/article/div[2]/div[2]/div[13]/div/div/div/input"
    chk_RRQ2_Sign_xpath = "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div[5]/div/one-record-home-flexipage2/forcegenerated-adgrollup_component___forcegenerated__flexipage_recordpage___dsnap_program_record_page_single_col___dsnap_case__c___view/forcegenerated-flexipage_dsnap_program_record_page_single_col_dsnap_case__c__view_js/record_flexipage-record-page-decorator/div[1]/slot/flexipage-record-home-single-col-template-desktop2/div/div[2]/div/slot/slot/flexipage-component2/slot/flexipage-tabset2/div/lightning-tabset/div/slot/slot/slot/flexipage-tab2[4]/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/article[2]/div[2]/article/div[2]/div[2]/div[15]/div/div/div/input"
    chk_RRQ3_xpath = "//article[3]/div[2]/div[2]/div[2]/div/input"
    btn_RRSave_css = ".slds-grid_align-center > .slds-button"
    btn_MenuOptn_xpath = "//div[@id='brandBand_2']/div/div/div/div/one-record-home-flexipage2/forcegenerated-adgrollup_component___forcegenerated__flexipage_recordpage___dsnap_program_record_page_single_col___dsnap_case__c___view/forcegenerated-flexipage_dsnap_program_record_page_single_col_dsnap_case__c__view_js/record_flexipage-record-page-decorator/div/slot/flexipage-record-home-single-col-template-desktop2/div/div/slot/slot/flexipage-component2/slot/records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_dsnap_case__c___012r00000008q1iaae___compact___view___recordlayout2/force-highlights2/div/div/div[3]/div/runtime_platform_actions-actions-ribbon/ul/li[4]/lightning-button-menu/button/lightning-primitive-icon"
    Optn_AddVer_xpath = "//div[@id='brandBand_2']/div/div/div/div/one-record-home-flexipage2/forcegenerated-adgrollup_component___forcegenerated__flexipage_recordpage___dsnap_program_record_page_single_col___dsnap_case__c___view/forcegenerated-flexipage_dsnap_program_record_page_single_col_dsnap_case__c__view_js/record_flexipage-record-page-decorator/div/slot/flexipage-record-home-single-col-template-desktop2/div/div/slot/slot/flexipage-component2/slot/records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_dsnap_case__c___012r00000008q1iaae___compact___view___recordlayout2/force-highlights2/div/div/div[3]/div/runtime_platform_actions-actions-ribbon/ul/li[4]/lightning-button-menu/div/div/slot/runtime_platform_actions-action-renderer[2]/runtime_platform_actions-custom-quick-action/slot/slot/runtime_platform_actions-ribbon-menu-item/a"
    btn_Sub_AddVer_xpath = "//button[@type='submit']"
    Optn_Certify_xpath = "//div[@id='brandBand_2']/div/div/div/div/one-record-home-flexipage2/forcegenerated-adgrollup_component___forcegenerated__flexipage_recordpage___dsnap_program_record_page_single_col___dsnap_case__c___view/forcegenerated-flexipage_dsnap_program_record_page_single_col_dsnap_case__c__view_js/record_flexipage-record-page-decorator/div/slot/flexipage-record-home-single-col-template-desktop2/div/div/slot/slot/flexipage-component2/slot/records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_dsnap_case__c___012r00000008q1iaae___compact___view___recordlayout2/force-highlights2/div/div/div[3]/div/runtime_platform_actions-actions-ribbon/ul/li[4]/lightning-button-menu/div/div/slot/runtime_platform_actions-action-renderer[4]/runtime_platform_actions-custom-quick-action/slot/slot/runtime_platform_actions-ribbon-menu-item/a/span"

    def __init__(self,driver):
        self.driver = driver

    def Click_VR(self):
        self.driver.find_element_by_xpath(self.tab_VR_xpath).click()

    def Sel_VRQ1(self,value):
        VRQ1 = Select(self.driver.find_element_by_xpath(self.drp_VRQ1_xpath))
        VRQ1.select_by_visible_text(value)

    def Sel_VRQ2(self,value):
        VRQ1 = Select(self.driver.find_element_by_xpath(self.drp_VRQ2_xpath))
        VRQ1.select_by_visible_text(value)

    def Click_PunderVRQ2(self):
        self.driver.find_element_by_xpath(self.p_UnderVRQ2_xpath).click()

    def Click_VRSave(self):
        self.driver.find_element_by_xpath(self.btn_VRSave_xpath).click()

    def Click_DID(self):
        self.driver.find_element_by_xpath(self.tab_DID_xpath).click()

    def Sel_DIDQ1(self,value):
        DIDQ1 = Select(self.driver.find_element_by_xpath(self.drp_DIDQ1_xpath))
        DIDQ1.select_by_visible_text(value)

    def Sel_DIDQ2(self,value):
        DIDQ2 = Select(self.driver.find_element_by_xpath(self.drp_DIDQ2_xpath))
        DIDQ2.select_by_visible_text(value)

    def Sel_DIDQ3(self,value):
        DIDQ3 = Select(self.driver.find_element_by_xpath(self.drp_DIDQ3_xpath))
        DIDQ3.select_by_visible_text(value)

    def Sel_DIDQ4(self,value):
        DIDQ4 = Select(self.driver.find_element_by_xpath(self.drp_DIDQ4_xpath))
        DIDQ4.select_by_visible_text(value)

    def Sel_DIDQ5(self,value):
        DIDQ5 = Select(self.driver.find_element_by_xpath(self.drp_DIDQ5_xpath))
        DIDQ5.select_by_visible_text(value)

    def Sel_DIDQ6(self,value):
        DIDQ6 = Select(self.driver.find_element_by_xpath(self.drp_DIDQ6_xpath))
        DIDQ6.select_by_visible_text(value)

    def Ent_DIDQ7(self,DIDQ7):
        self.driver.find_element_by_xpath(self.txt_DIDQ7_xpath).send_keys(DIDQ7)

    def Ent_DIDQ8(self,DIDQ8):
        self.driver.find_element_by_xpath(self.txt_DIDQ8_xpath).send_keys(DIDQ8)

    def Ent_DIDQ9(self,DIDQ9):
        self.driver.find_element_by_xpath(self.txt_DIDQ9_xpath).send_keys(DIDQ9)

    def Click_DIDSave(self):
        self.driver.find_element_by_xpath(self.btn_DIDSave_xpath).click()

    def Click_RR(self):
        self.driver.find_element_by_xpath(self.tab_RR_xpath).click()

    def Click_RRQ1(self,FN):
        self.driver.find_element_by_xpath(self.chk_RRQ1_xpath).send_keys(FN)

    def Click_RRQ2(self,LN):
        self.driver.find_element_by_xpath(self.chk_RRQ2_xpath).send_keys(LN)

    def Click_RRQ2_Sign(self,Sign):
        self.driver.find_element_by_xpath(self.chk_RRQ2_Sign_xpath).send_keys(Sign)

    def Click_RRQ3(self):
        self.driver.find_element_by_xpath(self.chk_RRQ3_xpath).click()

    def Click_RRSave(self):
        self.driver.find_element_by_css_selector(self.btn_RRSave_css).click()

    def Click_MenuOptn(self):
        self.driver.find_element_by_xpath(self.btn_MenuOptn_xpath).click()

    def Click_AddVer_Optn(self):
        self.driver.find_element_by_xpath(self.Optn_AddVer_xpath).click()

    def Click_Save_AddVer(self):
        self.driver.find_element_by_xpath(self.btn_Sub_AddVer_xpath).click()

    def Click_Certify(self):
        self.driver.find_element_by_xpath(self.Optn_Certify_xpath).click()

