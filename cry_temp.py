import requests
from bs4 import BeautifulSoup

url = 'http://www.cry.org/careers/current-openings'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
blocks = soup.find_all(class_='panel-body')

required_info = blocks[0].select('b')
print required_info

all_listings = []

listing_data = []

#block = blocks[0]
#for i, v in enumerate(list(block.children)):
#    print i, ' = ', v


print list(blocks[0].children)[2::4][0].encode("utf-8")
#print list(block.children)[19]

for block in blocks:
    listing_data.append(list(block.children[::4]))
#    details = '|'.join(list(block.children[::4]))
#    listing_data.append(details)
#    print block
#    details = {}
#    print list(block.children[::4])
#    details['Job Title'], details['Function / Division'], details['Location'], details['Reporting To'] = (val for val in list(block.children)[::4])
#
#    print details, '...........>>>>>>>>>>'
#    break
#
#    print block.prettify(), '\n=========================\n'
#    print list(block.children)[::4]
#    print block.select('b')
#    print block.select('strong')
#    print block.find_all('br')
#
#    break
#    print block.find_all(class_='panel-body')

#print soup.prettify()

print listing_data
