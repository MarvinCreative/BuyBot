# BuyBot
Automated webcraller that watches websites for desired products and when product is in stock automatically adds to cart and checks out. Upon successful checkout program will play notification sound before closing.

Originally made to purchase PS5 during console shortages. However can be used for other products by simply changing target URLs.

## Supported Sites
- Amazon
- Best Buy

## Requirements
1. Will require Microsoft Edge WebDriver to be installed. Download can be found [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).

2. Only tested on Windows. Will likely not work on other operating systems due to use of *winsound* package. This package was only used to play the notification sound upon successful checkout. So you can likely simply remove that part of the code and then it should run on other operating systems.

## Usage Notes
- Make sure that you are logged in on the target websites and have a purchase method saved to your account. The program works under the assumption that your credit card details are already loaded on the site. And all that's required is to confirm the purchase, or in the case of BestBuy, enter your credit card's CVV number.

- If using the BestBuy program make sure to replace the value for the variable *cvvNum* with your credit card's CVV.


## Developer Notes
This was my first foray into automated webcralling and browser automation using Python so there may be some stability and reliability issues.
