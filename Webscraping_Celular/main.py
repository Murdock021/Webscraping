import pandas as pd 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(r'C:/Users/Diogo Machado/Downloads/chromedriver-win64/chromedriver.exe')

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.google.com")

assert "Google" in driver.title

elem = driver.find_element(By.NAME, "q")

elem.clear()
elem.send_keys("Celular")
elem.send_keys(Keys.RETURN)