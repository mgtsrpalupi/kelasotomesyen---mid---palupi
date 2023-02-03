from selenium import webdriver
import time

url =["https://tiket.com","https://tokopedia.com","https://orangsiber.com",
    "https://demoqa.com","https://automathetheboringstuff.com"]
for i in url:
    driver = webdriver.Chrome()
    driver.minimize_window()
    driver.get(url)
    time.sleep(1)
    print(driver.title)

    driver.close()


