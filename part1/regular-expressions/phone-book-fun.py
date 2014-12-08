from phone_list import data as persons
import re

for person in persons:
    try:
        result = re.search(r'D.* Hardy' , person['name'])
        print "{} {}".format(result.group(), person['phone'])
    except AttributeError:
        pass
        
