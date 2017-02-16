#!/usr/bin/env python2

from selenium import webdriver
import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import re


ran = random.randrange(0, 20, 5)
ran2 = random.randrange(0, 50, 5)

numero = []
numero.append("21")
numero.append("22")
numero.append("23")
numero.append("24")
numero.append("25")
numero.append("26")
numero.append("27")
numero.append("28")
numero.append("29")
numero.append("30")

for numero in numero:
    print (numero)
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--no-startup-window')
    driver = webdriver.Chrome(
        executable_path="/Users/super/chromedriver", chrome_options=chrome_options)

    url = "https://github.com/join"
    driver.get(url)
    username = driver.find_element_by_id("user_login")
    username.send_keys("botbotbot"+str(numero)+str(ran))
    email = driver.find_element_by_id("user_email")
    email.send_keys("bot"+str(numero)+"@pandb-software.com")
    driver.execute_script("window.scrollTo(0, 500);")
    password = driver.find_element_by_css_selector("#user_password")
    password.send_keys("Agus.789")
    driver.find_element_by_css_selector("#signup_button").click()
    driver.find_element_by_css_selector(
        "#js-pjax-container > div > div.setup-main > div > form > button").click()
    driver.execute_script("window.scrollTo(0, 200);")
    driver.find_element_by_css_selector(
        "#js-pjax-container > div > div.setup-main.user-identification-questions > div > form > input").click()
    driver.close()
