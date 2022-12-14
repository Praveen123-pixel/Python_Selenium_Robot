from  selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class Test_generic():

    url ="https://www.actitime.com/"
    driver = webdriver.Chrome()
    Application_Title = "actiTIME - Time Tracking Software for Smart Teams"
    Expected_main_menu_options = ['Features\nClients\nPricing\nHelp Center\nResources']

    def do_click(self, By_locater):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(By_locater)).click()
        #WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(By_locater)).click()

    def do_send_key(self, By_locater, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(By_locater)).send_keys(text)

    def get_element_text(self, By_locater):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(By_locater)).text
        return element

    def is_visible(self, By_locater):
        element = WebDriverWait(self.driver,5).until(EC.visibility_of_any_elements_located(By_locater))
        return bool(element)

    def select_the_element(self, By_locater):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(By_locater)).click()