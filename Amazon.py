import time
import winsound
import sys
from selenium import webdriver

driver = webdriver.Edge('D:\BuyBot\msedgedriver.exe')

driver.get('https://www.amazon.ca/')

trgtPg = 'https://www.amazon.ca/PlayStation-5-Console/dp/B08GSC5D9G/ref=sr_1_2?dchild=1&keywords=playstation+5&qid=1606527056&sr=8-2'
checkoutPg = 'https://www.amazon.ca/gp/cart/view.html?ref_=nav_cart'

breaker = 1

currentPage = driver.current_url

print("Website --> https://www.amazon.ca/PlayStation-5-Console/dp/B08GSC5D9G/ref=sr_1_2?dchild=1&keywords=playstation+5&qid=1606527056&sr=8-2")

while breaker == 1:

    if currentPage == trgtPg:
        print("page found")

        add2Cart = driver.find_elements_by_xpath("//input[@id='add-to-cart-button']")

        if len(add2Cart) == 1:
            print("Buy Button Seen")
            add2Cart[0].click()

            driver.get(checkoutPg)

            #plceOrderConfirm = WebDriverWait(driver, 10000).until(lambda x: x.find_element_by_class_name("a-button-text place-your-order-button"))

            plceOrder = driver.find_element_by_xpath("//input[@class='a-button-text place-your-order-button']")

            plceOrder.click()
            print("ORDER PLACED")

            frequency = 2500
            duration = 1000

            winsound.Beep(frequency, duration)

            time.sleep(5)

            sys.exit()

        else:
            print("refresh")
            driver.refresh()
            time.sleep(15)
            currentPage = driver.current_url

    else:
        currentPage = driver.current_url
        time.sleep(20)
