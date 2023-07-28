from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://www.skysports.com/premier-league-results/2022-23")
WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[id^=sp_message_iframe_758392]")))
try:
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".message-component.message-button.no-children.focusable.sp_message-accept-button.sp_choice_type_11"))).click()
except:
    print("Could not click")
    pass

driver.find_element(By.CLASS_NAME,"plus-more").click()
page_source = driver.page_source
driver.quit()


soup= BeautifulSoup(page_source,'lxml')
print(soup)