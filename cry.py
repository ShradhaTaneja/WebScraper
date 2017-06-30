import requests
from bs4 import BeautifulSoup

url = 'http://www.cry.org/careers/current-openings'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
blocks = soup.find_all(class_='panel-body')

required_info = blocks[0].select('b')
print required_info

#block = blocks[0]
#for i, v in enumerate(list(block.children)):
#    print i, ' = ', v


for block in blocks:
    print block.prettify(), '\n=========================\n'
    print list(block.children)[2::4]
    print block.select('b')
    print block.select('strong')
    print block.find_all('br')

    break
