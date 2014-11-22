import mechanize
from bs4 import BeautifulSoup

browser = mechanize.Browser()
browser.open('https://realpython.com/practice/login.php')

browser.select_form('login')
browser['user'] = 'zeus'
browser['pwd'] = 'ThunderDude'
browser.submit()

my_soup = BeautifulSoup(browser.response().get_data())
print my_soup.title.string

browser.back()


browser.select_form('login')
browser['user'] = 'ZEUS'
browser['pwd'] = 'tHUNDERdUDE'
browser.submit()

html_code = browser.response().get_data()
if html_code.find('Wrong username or password!') > 0:
    print "Login process failed"
