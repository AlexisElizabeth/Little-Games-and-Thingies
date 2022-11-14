from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"
driver_service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=driver_service)

url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)

article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")


print(article_count.text)
