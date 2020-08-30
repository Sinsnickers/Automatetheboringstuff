#!python3
#commandLineEmailer.py - takes a email address and a text as
#command line arguemnt, logs in into email account and sends
#email to the provide address

import sys, bs4, pyinputplus, time
from selenium import webdriver

#open webbrowser with email site
browser = webdriver.Chrome()
browser.get("https://gmx.net")
browser.maximize_window()

#login into own email address
userName = "bero81mail@gmx.de"
userAccountField = browser.find_element_by_css_selector("#freemailLoginUsername")
userAccountField.send_keys(f"{userName}")
userPassword = ""
userPasswordField = browser.find_element_by_css_selector("#freemailLoginPassword")
userPasswordField.send_keys(f"{userPassword}")
userPasswordField.submit()

#open new email

#emailButton = browser.find_element_by_link_text("Barrierefreies Postfach")
frames = browser.find_elements_by_tag_name("iframe")
print("No of frames that are present on this page ", len(frames))
print(browser.page_source)

#get email address from command line argument


#get text from command line argument

#enter both informations into the email form

#use selenium to submit the email

#logout email account and close webbrowser

