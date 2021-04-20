from selenium import webdriver
import time
import logininfo
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from pynput.keyboard import Key, Controller
isimler = []
def takeAllNames() :

    list1 = []
    
    #network = browser.find_element_by_id("mynetwork-tab-icon")
    #network.click()
    #time.sleep(1)
    #contacts = browser.find_element_by_class_name("mn-community-summary__sub-section")
    #contacts.click()
    #time.sleep(1)

    browser.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
    

    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount == lenOfPage:
            match=True
    time.sleep(5)
    
    kisiler = browser.find_elements_by_xpath("//span[contains(@class, 'mn-connection-card__name')]") 
    for e in kisiler:
        isimler.append(e.text)
    print(isimler)
    anasayfa = browser.find_element_by_id("feed-tab-icon")
    anasayfa.click()
    



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
time.sleep(3)

takeAllNames()

for i in range(len(isimler)):

    keyboard2 = Controller()
    keyboard2.press(Key.esc)
    keyboard2.release(Key.esc)

    
    messaging = browser.find_element_by_id("messaging-tab-icon")
    messaging.click()

    time.sleep(3)

    newmessage = browser.find_element_by_class_name("ember-view.artdeco-button.artdeco-button--tertiary.artdeco-button--circle.mr1")
    newmessage.click()
    time.sleep(3)

    search = browser.find_element_by_class_name("msg-connections-typeahead__search-field.msg-connections-typeahead__search-field--no-recipients.ml1.mv1")
    search.send_keys(isimler[i])

    time.sleep(2)
    keyboard = Controller()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    messagebox = browser.find_element_by_class_name("msg-form__contenteditable.t-14.t-black--light.t-normal.flex-grow-1.notranslate")
    messagebox.send_keys("Hi " + isimler[i] + "\nI have a good suggestion for you\n\nDo you need to keep your memories alive ?"+
                         "\nDo you wanna receive notifications to remind anything ?\nDo you need to make a plan for tomorrow ?\n"+
                         "\nIf your answer is YES, I have good news for you.\nWe pieced together all of these !\n"+
                         "You can use NORP for adding IMPORTANT Notes, Reminders and useful Planners.\n\nIt easy to use.\n"+
                         "You can just Register for FREE and begin to use Now ! \n"+
                         "You can download from here : \n" +
                         "https://play.google.com/store/apps/details?id=com.hasancagli.newapplication")

    time.sleep(2)
    try :
        sendbutton = browser.find_element_by_class_name("msg-form__send-button.artdeco-button.artdeco-button--1")
        sendbutton.click()
    except :
        print("Gönderilemedi")
        i+= 1
        continue

    time.sleep(2)
    keyboard1 = Controller()
    keyboard1.press(Key.esc)
    keyboard1.release(Key.esc)

    anasayfa = browser.find_element_by_id("feed-tab-icon")
    anasayfa.click()

    i += 1 




time.sleep(7)

browser.close()
