from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# My university uses a platform called LMS - OLAT (Learning Management System - Online Learning And Training) for sharing 
# files and video podcasts and for communication. OLAT does not offer an option to stay signed in. Every time I open OLAT 
# which I do multiple times daily, I have to sign in. Signing in requires me to navigate through multiple webpages before 
# reaching the site. This script opens OLAT automatically.

# Youtube video where I show the script in action: https://youtu.be/WrvqXk3x9cw
# Documentation for Selenium: https://selenium-python.readthedocs.io/navigating.html?highlight=enter%20form#filling-in-forms

PATH = "/Applications/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://lms.uzh.ch/")

# handle drop-down menu
ddelement = Select(driver.find_element(By.ID, 'user_idp'))
ddelement.select_by_value('https://aai-idp.uzh.ch/idp/shibboleth')
# click the button "submit"
driver.find_element(By.ID, "wayf_submit_button").click()

# enter login information
uzhshortname_tf = driver.find_element(By.ID, "username")
uzhshortname_tf.send_keys("femerz")
password_tf = driver.find_element(By.ID, "password")
password_tf.send_keys("password")   # for the script to function, I'd have to enter my password here
# finish the login by clicking the button "login"
driver.find_element(By.CLASS_NAME, "aai_login_button").click()
