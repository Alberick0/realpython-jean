import mechanize
from bs4 import BeautifulSoup
import time
from time import sleep

print "This will check yahoo stock price"
times = int(raw_input('How many times do you want to check:\n'))
interval = int(raw_input("Introduce the interval in seconds:\n"))

def check_stock_price(times, interval):
    browser = mechanize.Browser()

    for i in range(times):
        browser.open("http://finance.yahoo.com/q?s=yhoo")
        response = browser.response()
        parser = BeautifulSoup(response.get_data())
        result = parser.find_all("span", id="yfs_l84_yhoo")

        print "The price stock is {} on {} ".format(result[0].string, time.ctime())

        if i < times - 1:
            sleep(interval)

check_stock_price(times, interval)

