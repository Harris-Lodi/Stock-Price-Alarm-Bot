from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

# open the url in the web driver
url = 'https://stockanalysis.com/stocks/amd/'
driver = webdriver.Firefox()
driver.get(url)

# click on a button to open the conversation tab
# button = driver.find_element(By.CSS_SELECTOR, 'li.svelte-1ubpy4e:nth-child(4) > button:nth-child(1)')
# button.click()

# find the comments
try:
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'li.svelte-1ubpy4e:nth-child(4) > button:nth-child(1)'))
    )
    button.click()

    comments = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "messages"))
    )
    print(comments)
finally:
    driver.quit()