def takeAllNames() :

    isimler =  []

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

takeAllNames()
