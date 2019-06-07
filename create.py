from selenium import webdriver
import sys
import time
import pyautogui

browser = webdriver.Chrome(executable_path="/home/piyush/Downloads/chromedriver_linux64/chromedriver")

URL = "https://github.com/login"

browser.get(URL)

username = "usermame"
password = "password"

user = browser.find_element_by_xpath("//input[@id='login_field']")
user.send_keys(username)

passwd = browser.find_element_by_xpath("//input[@id='password']")
passwd.send_keys(password)

browser.find_element_by_xpath("//input[@type='submit']").click()

print("login successful")

URL = "https://github.com/new"
browser.get(URL)

print("about to create new repository")

browser.find_element_by_xpath("//input[@id='repository_visibility_private']").click()

new_repo = browser.find_element_by_xpath("//input[@id='repository_name']")
new_repo.send_keys(sys.argv[1])

time.sleep(2)

pyautogui.press('enter')

print("New repository created")

browser.close()
