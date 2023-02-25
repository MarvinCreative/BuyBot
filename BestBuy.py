import time
import winsound
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

website = 'https://www.bestbuy.ca/en-ca/product/playstation-5-digital-edition-god-of-war-ragnarok-bundle/16552734'
cartURL = 'https://www.bestbuy.ca/checkout/?qit=1#/en-ca/review'

cvvNum = "cvvNumberHere"

driver = webdriver.Edge('D:\BuyBot\msedgedriver.exe')  # Optional argument, if not specified will search path.
driver.get(website)

breaker = 1

currentPage = driver.current_url

while breaker == 1:

    if currentPage == website:
        print("page found")
        buyBtn = driver.find_elements_by_class_name('addToCartButtonContainer_2ZF35')
        cartCount = driver.find_elements_by_class_name('counter')

        buyBtn[0].click()
        print("clicked")
        time.sleep(5)
        cartCount = driver.find_elements_by_class_name('counter')

        if len(cartCount) == 1:
            breaker = 0
            driver.get(cartURL)
            element = WebDriverWait(driver, 10000).until(lambda x: x.find_element_by_id("cvv"))
            cvvEnter = driver.find_element_by_id("cvv")
            cvvEnter.click()
            cvvEnter.send_keys(cvvNum)
            print("cvv enter")
            #plcOrdBtn = WebDriverWait(driver, 10000).until(lambda x: x.find_element_by_class_name('button_2Xgu4 primary_oeAKs order-now regular_cDhX6'))
            plcOrdBtn = driver.find_element_by_xpath("//button[@class='button_2Xgu4 primary_oeAKs order-now regular_cDhX6']")
            print("place order")
            plcOrdBtn.click()

            frequency = 2500
            duration = 1000

            winsound.Beep(frequency, duration)

        elif len(cartCount) < 1:
            print("refresh")
            driver.refresh()
            time.sleep(15)
            currentPage = driver.current_url

    else:
        currentPage = driver.current_url
        time.sleep(20)