from unicodedata import name
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get("https://www.instagram.com")
time.sleep(5)

# kayit_ol= browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/article/div[2]/div[2]/div/p/a/span""")
# kayit_ol.click()
username=browser.find_element(By.NAME,"username")
password=browser.find_element(By.NAME,"password")
username.send_keys('kullanıcı adınız')
password.send_keys('şifreniz')
login_button = browser.find_element_by_xpath("""//*[@id="loginForm"]/div/div[3]""")
login_button.click()
time.sleep(5)
#tebrikler instagrama giriş yaptınız...
browser.close()