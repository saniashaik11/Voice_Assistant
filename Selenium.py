from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class infow():
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        
        # ✅ Set path to Chrome browser binary
        chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"

        # ✅ Set path to chromedriver.exe
        service = Service("C:/Users/USER/OneDrive/Desktop/Voice_Assistant/chromedriver-win64/chromedriver.exe")
        
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
            
    def get_info(self, query):
        self.query = query
        self.driver.get("https://www.wikipedia.org")
        # Find the search input element using the updated method
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        # Find the search button using the updated method
        enter = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
        enter.click()

