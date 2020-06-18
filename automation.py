from selenium import webdriver
import time

insta = webdriver.Firefox()

insta.get('https://www.instagram.com/accounts/login/?hl=en')
time.sleep(2)

# instagram
username = insta.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")
username.send_keys('username')


password=insta.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
password.send_keys('password/')
time.sleep(1)

login = insta.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
login.click()
time.sleep(5)








#facebook

face = webdriver.Firefox()

face.get('https://www.facebook.com/')


f_name = face.find_element_by_id('email')
f_name.send_keys('user name')

f_password = face.find_element_by_id('pass')
f_password.send_keys('password')

f_login= face.find_element_by_xpath('//*[@id="u_0_b"]')
f_login.click()


