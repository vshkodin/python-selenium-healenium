from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import os
import codecs

class Driver:
    def __init__(self,driver):
        self.driver=driver

    def find(self,LOCATOR):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, LOCATOR)))
        elem = self.driver.find_element_by_css_selector(LOCATOR)
        return elem

    def get(self, URL):
        self.driver.get(f'{self.driver.base_url}{URL}')
        self.page_saver()

    def click(self,LOCATOR):
        elem = self.find(LOCATOR)
        elem.click()

    def page_source(self):
        return self.driver.page_source

    def title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def page_saver(self):
        url = self.get_url()
        url = url.replace(self.driver.base_url,'').replace(r'/','_').replace(r'?','_').replace(r'=','_').replace(r'.','_')
        n = os.path.join("pages\\", f"{url}.html")
        f = codecs.open(n, "w", "utf−8")
        h = self.page_source()
        f.write(h)

    def quit(self):
        self.driver.quit()