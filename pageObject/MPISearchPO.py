from selenium.webdriver.common.action_chains import ActionChains

class MPISearch():
    lnk_HOH_xpath = "//slot/slot/force-lookup/div/force-hoverable-link/div/a/span"
    btn_LocalS_xpath = "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/one-record-home-flexipage2/forcegenerated-adgrollup_component___forcegenerated__flexipage_recordpage___dsnap_household_member1___dsnap_household_member__c___view/forcegenerated-flexipage_dsnap_household_member1_dsnap_household_member__c__view_js/record_flexipage-record-page-decorator/div[1]/slot/flexipage-record-home-single-col-template-desktop2/div/div[1]/slot/slot/flexipage-component2/slot/records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_dsnap_household_member__c___012r00000008q1naae___compact___view___recordlayout2/force-highlights2/div[1]/div[1]/div[3]/div/runtime_platform_actions-actions-ribbon/ul/li[2]/runtime_platform_actions-action-renderer/runtime_platform_actions-custom-quick-action/slot/slot/lightning-button/button"
    btn_LocalS_M_xpath = "//button[@name='DSNAP_Household_Member__c.Local_Search']"
    btn_LocalS_Cancel_css = ".windowViewMode-normal .slds-align_absolute-center > .slds-button"
    btn_MPIS_xpath = "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div[4]/div/one-record-home-flexipage2/forcegenerated-adgrollup_component___forcegenerated__flexipage_recordpage___dsnap_household_member1___dsnap_household_member__c___view/forcegenerated-flexipage_dsnap_household_member1_dsnap_household_member__c__view_js/record_flexipage-record-page-decorator/div[1]/slot/flexipage-record-home-single-col-template-desktop2/div/div[1]/slot/slot/flexipage-component2/slot/records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_dsnap_household_member__c___012r00000008q1naae___compact___view___recordlayout2/force-highlights2/div[1]/div[1]/div[3]/div/runtime_platform_actions-actions-ribbon/ul/li[3]/runtime_platform_actions-action-renderer/runtime_platform_actions-custom-quick-action/slot/slot/lightning-button/button"
    btn_MPIS_M_xpath = "//button[@name='DSNAP_Household_Member__c.MPI_Search']"
    btn_MPIS_Cancel_css = ".windowViewMode-normal .slds-align_absolute-center > .slds-button"
    mess_MPI_succ_css = ".toastMessage"
    lnk_Back2HoH_xpath = "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div[4]/div/one-record-home-flexipage2/forcegenerated-adgrollup_component___forcegenerated__flexipage_recordpage___dsnap_household_member1___dsnap_household_member__c___view/forcegenerated-flexipage_dsnap_household_member1_dsnap_household_member__c__view_js/record_flexipage-record-page-decorator/div[1]/slot/flexipage-record-home-single-col-template-desktop2/div/div[2]/div/slot/slot/flexipage-component2/slot/records-lwc-detail-panel/records-base-record-form/div/div/div/div/records-record-layout-event-broker/slot/records-lwc-record-layout/forcegenerated-detailpanel_dsnap_household_member__c___012r00000008q1naae___full___view___recordlayout2/force-record-layout-block/slot/force-record-layout-section[1]/div/div/div/slot/force-record-layout-row[1]/slot/force-record-layout-item[1]/div/div/div[2]/span/slot[1]/slot/force-lookup/div/force-hoverable-link/div/a/span"
    lnk_Back2M_xpath = "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div[1]/div/one-record-home-flexipage2/forcegenerated-adgrollup_component___forcegenerated__flexipage_recordpage___dsnap_household_member1___dsnap_household_member__c___view/forcegenerated-flexipage_dsnap_household_member1_dsnap_household_member__c__view_js/record_flexipage-record-page-decorator/div[1]/slot/flexipage-record-home-single-col-template-desktop2/div/div[2]/div/slot/slot/flexipage-component2/slot/records-lwc-detail-panel/records-base-record-form/div/div/div/div/records-record-layout-event-broker/slot/records-lwc-record-layout/forcegenerated-detailpanel_dsnap_household_member__c___012r00000008q1naae___full___view___recordlayout2/force-record-layout-block/slot/force-record-layout-section[1]/div/div/div/slot/force-record-layout-row[1]/slot/force-record-layout-item[1]/div/div/div[2]/span/slot[1]/slot/force-lookup/div/force-hoverable-link/div/a/span"
    lnk_Member_xpath = "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div[5]/div/one-record-home-flexipage2/forcegenerated-adgrollup_component___forcegenerated__flexipage_recordpage___household_record_page_single_col___dsnap_household__c___view/forcegenerated-flexipage_household_record_page_single_col_dsnap_household__c__view_js/record_flexipage-record-page-decorator/div[1]/slot/flexipage-record-home-single-col-template-desktop2/div/div[2]/div/slot/slot/flexipage-component2[2]/slot/lst-related-list-single-container/laf-progressive-container/slot/lst-related-list-single-app-builder-mapper/article/lst-related-list-view-manager/lst-common-list/div/div/lst-primary-display-manager/div/lst-primary-display/lst-primary-display-grid/lst-customized-datatable/div[2]/div/div/div/table/tbody/tr[2]/th/lightning-primitive-cell-factory/span/div/lightning-primitive-custom-cell/force-lookup/div/force-hoverable-link/div/a/span"

    def __init__(self,driver):
        self.driver = driver

    def ClickHOH(self):
        self.driver.find_element_by_xpath(self.lnk_HOH_xpath).click()

    def ClickLS(self):
        self.driver.find_element_by_xpath(self.btn_LocalS_xpath).click()

    def ClickLS_M(self):
        #self.driver.find_element_by_xpath(self.btn_LocalS_M_xpath).click()
        button = self.driver.find_element_by_xpath(self.btn_LocalS_M_xpath)
        self.driver.implicitly_wait(10)
        ActionChains(self.driver).move_to_element(button).click(button).perform()

    def ClickLS_Cancl(self):
        self.driver.find_element_by_css_selector(self.btn_LocalS_Cancel_css).click()

    def ClickMPIS(self):
        self.driver.find_element_by_xpath(self.btn_MPIS_xpath).click()

    def ClickMPIS_M(self):
        #self.driver.find_element_by_xpath(self.btn_MPIS_M_xpath).click()
        button = self.driver.find_element_by_xpath(self.btn_MPIS_M_xpath)
        self.driver.implicitly_wait(10)
        ActionChains(self.driver).move_to_element(button).click(button).perform()

    def ClickMPIS_Cancl(self):
        self.driver.find_element_by_css_selector(self.btn_MPIS_Cancel_css).click()

    def ToastMess(self):
        value = self.driver.find_element_by_css_selector(self.mess_MPI_succ_css).text
        return value

    def ClickHOHBck(self):
        self.driver.find_element_by_xpath(self.lnk_Back2HoH_xpath).click()

    def ClickMBck(self):
        #self.driver.find_element_by_xpath(self.lnk_Back2M_xpath).click()
        button = self.driver.find_element_by_xpath(self.lnk_Back2M_xpath)
        self.driver.implicitly_wait(10)
        ActionChains(self.driver).move_to_element(button).click(button).perform()

    def ClickMem(self):
        self.driver.find_element_by_xpath(self.lnk_Member_xpath).click()

    def Click_Excep_Cncl_LS(self):
        button = self.driver.find_element_by_css_selector(self.btn_LocalS_Cancel_css)
        self.driver.implicitly_wait(10)
        ActionChains(self.driver).move_to_element(button).click(button).perform()