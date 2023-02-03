from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

url =["https://tiket.com","https://tokopedia.com","https://orangsiber.com",
    "https://demoqa.com","https://automathetheboringstuff.com"]
for i in url:
    driver.get(url)
    time.sleep(1)
    print(x)

driver.close()


