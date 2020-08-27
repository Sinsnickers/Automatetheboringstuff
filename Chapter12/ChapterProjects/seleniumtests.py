from selenium import webdriver
import pyinputplus

browser = webdriver.Firefox()
browser.get("https://gmx.net")
userElem = browser.find_element_by_id("freemailLoginUsername")
userElem.send_keys("bero81@gmx.de")
passwordElem = browser.find_element_by_id("freemailLoginPassword")
password = pyinputplus.inputPassword("Please enter your password\n")
passwordElem.send_keys(password)
userElem.submit()