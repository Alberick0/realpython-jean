from urllib2 import urlopen
import re

url = 'https://realpython.com/practice/dionysus.html'

html_page = urlopen(url)
source_code = html_page.read()

name_start_tag = '<h2>Name: '
name_end_tag = '</h2>'
favorite_start_tag = 'Favorite Color: '
favorite_end_tag = '\n</center>'

name_start_index = source_code.find(name_start_tag) + len(name_start_tag)
name_end_index = source_code.find(name_end_tag)
favorite_start_index = source_code.find(favorite_start_tag) + len(favorite_start_tag)
favorite_end_index = source_code.find(favorite_end_tag)

print source_code[name_start_index:name_end_index]
print source_code[favorite_start_index:favorite_end_index]


name =  re.search('<h2>.*</h2>', source_code, re.IGNORECASE).group()
favorite = re.search('<br>\nFavorite.*<br>', source_code, re.IGNORECASE).group()

output_name = re.sub("<.*?>.*? ", '', name)
output_favorite = re.sub("<.*?>\n.*?: ", "", favorite)
print output_name.strip('</h2>'),'\n', output_favorite.strip('<br>') 
