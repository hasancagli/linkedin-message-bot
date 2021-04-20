from selenium import webdriver
import time
import logininfo

browser = webdriver.Firefox()
browser.get("https://www.linkedin.com/")

time.sleep(1)

girisYap = browser.find_element_by_xpath("/html/body/nav/a[3]")
girisYap.click()
time.sleep(1)

username = browser.find_element_by_xpath("//*[@id='username']")
password = browser.find_element_by_xpath("//*[@id='password']")

username.send_keys(logininfo.username)
password.send_keys(logininfo.password)



loginButton = browser.find_element_by_xpath("/html/body/div/main/div[2]/form/div[3]/button")

loginButton.click()
time.sleep(1)

network = browser.find_element_by_id("mynetwork-tab-icon")
network.click()

time.sleep(4)

connections = browser.find_element_by_class_name("mn-community-summary__entity-info")
connections.click()

time.sleep(4)

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True
time.sleep(5)

elements = browser.find_element_by_css_selector("mn-connection-card__details")

browser.close()












