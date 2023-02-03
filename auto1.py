from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.minimize_window()

url =["https://tiket.com","https://tokopedia.com","https://orangsiber.com","https://demoqa.com","https://automatetheboringstuff.com"]
for i in url:
    driver.get(i)
    print(driver.title)
    time.sleep(1)
driver.close()


