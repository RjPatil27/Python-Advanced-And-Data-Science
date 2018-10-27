'''
This program is about automating the browser.
here, we are opening facebook autmatically just sending our username and password as input to code.
Its really intersting code which directly redirect to facebook.com and automatically enter username and pwd, then login

'''

from selenium import webdriver
from getpass import getpass
from time import sleep

username = input("Enter User name of FB:- ")
pwd = input("Enter PWD of FB:-  ")
#alternative: pwd = getpass("Enter PWD of FB:-  ")

driver = webdriver.Firefox(executable_path='//home/sai//Music//Rajat//geckodriver-v0.23.0-linux64//geckodriver')
driver.get('https://www.facebook.com')
print("Opened Facebook")
sleep(1)

username_box = driver.find_element_by_id('email')
username_box.send_keys(username)
print("Email ID entered")
sleep(1)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print("Password Entered")
sleep(1)

login_box = driver.find_element_by_id('loginbutton')
login_box.click()

print("Done")
input("Press anything to quit")
driver.quit()
