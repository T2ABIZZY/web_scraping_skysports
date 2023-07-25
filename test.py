
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.skysports.com/premier-league-results/2022-23")
time. sleep(4)
accept_button = driver.find_element(By.LINK_TEXT, "Home")
accept_button.click()

