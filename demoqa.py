from selenium.webdriver.common.keys import Keys
from BaseApp import BasePage
from selenium.webdriver.common.by import By


class Demoqa(BasePage):

    def click_elements_button(self):
        button = self.find_element((By.CSS_SELECTOR, '.card.mt-4.top-card'))
        button.click()

    def click_check_box_menu_item(self):
        item = self.find_element((By.CSS_SELECTOR, '#item-1'))
        item.click()

    def click_toggle_button(self):
        button = self.find_element((By.CSS_SELECTOR, '.rct-collapse.rct-collapse-btn'))
        button.click()

    def click_toggle_button_download(self):
        button = self.find_element((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/ol/li/ol/li[3]/span/button'))
        button.click()

    def click_word_file(self):
        button = self.find_element((By.CSS_SELECTOR, '.rct-node.rct-node-leaf label'))
        button.click()

    def success_text(self):
        text = self.get_element_text((By.ID, 'result'))
        return text









