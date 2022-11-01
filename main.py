import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


city = input("Insert City: ")
concat = city + " " + "Current Weather "
driver = webdriver.Chrome()

while True:
    driver.get("https://www.google.com/")
    search = driver.find_element(By.NAME, "q")
    search.send_keys(concat, Keys.ENTER)
    temp = driver.find_element(By.ID, "wob_tm").text
    condition = driver.find_element(By.ID, "wob_dc").text
    driver.quit()
    print("In"+" " + city + " the weather is:")
    print("Temperature: " + temp + " °C")
    print("Condition: " + condition)
    time.sleep(300)
