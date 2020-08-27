#! python3
#2048.py - open website and just sends
#up, right, down, left to the game

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

browser = webdriver.Chrome()
browser.get("https://play2048.co/")
htmlElem = browser.find_element_by_tag_name("html")
game_status = browser.find_element_by_css_selector('.game-container')
#htmlElem = browser.find_element_by_css_selector("div.grid-row:nth-child(3) > div:nth-child(2)")
KEY_INPUTS = (Keys.LEFT,Keys.UP,Keys.RIGHT,Keys.DOWN)
while game_status.text != 'Game over!':
    keyInput = KEY_INPUTS
    htmlElem.send_keys(keyInput)
    game_status = browser.find_element_by_css_selector('.game-container')   
    