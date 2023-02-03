from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.minimize_window()

driver.get('https://tiket.com')
time.sleep(1)
print(driver.title)
driver.get('https://tokopedia.com')
time.sleep(1)
print(driver.title)
driver.get('https://orangsiber.com')
time.sleep(1)
print(driver.title)
driver.get('https://demoqa.com')
time.sleep(1)
print(driver.title)
driver.get('https://automatetheboringstuff.com')
time.sleep(1)
print(driver.title)

driver.close()
