from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#User city input.
city = input("Insert City: ")

#Saving a variable to  use in Chrome.
concat = city + " " + "Current Weather "

#Calling the driver and google.
driver = webdriver.Chrome()
driver.get("https://www.google.com/")

#Finding the search bar, sending the concatenated string and pushing ENTER.
search = driver.find_element(By.NAME, "q")
search.send_keys(concat, Keys.ENTER)

#Capturing the temperature and condition.
temp = driver.find_element(By.ID, "wob_tm").text
condition = driver.find_element(By.ID, "wob_dc").text

#Closing the browser.
driver.quit()

#Printing the results in the console.
print("In"+" " + city + " the weather is:")
print("Temperature: " + temp + " °C")
print("Condition: " + condition)

