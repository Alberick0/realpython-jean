from bs4 import BeautifulSoup
from urllib2 import urlopen

url = 'https://realpython.com/practice/profiles.html'
html_page = urlopen(url)
page_code = html_page.read()
parser = BeautifulSoup(page_code)

print('\n-->Exercise 2<--\n')

for tag in parser.find_all('a'):
    print tag['href']
    

print('\n--->Exercise 3<---\n')

for tag in parser.find_all('a'):
    new_url = url.replace('profiles.html', tag['href'])
    new_parser = BeautifulSoup(urlopen(new_url).read())
    print new_parser.getText()
