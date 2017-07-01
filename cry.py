import requests, json
from bs4 import BeautifulSoup

url = 'http://www.cry.org/careers/current-openings'

def get_page_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    blocks = soup.find_all(class_='panel-body')
    return blocks

#required_info = blocks[0].select('b')

#block = blocks[0]
#for i, v in enumerate(list(block.children)):
#    print i, ' = ', v

def parse_page_data(data):
    all_listings = []
    required_info = data[0].find_all(['b', 'strong'])

    for block in data:
        all_data = list(block.children)
        data = all_data[2::4]
        details = {}
        details[required_info[0].get_text().encode('utf-8')] = str(data[0].encode('utf-8')).split(':')[1]
        details[required_info[1].get_text().encode('utf-8')] = str(data[1].encode('utf-8')).split(':')[1]
        details[required_info[2].get_text().encode('utf-8')] = str(data[2].encode('utf-8')).split(':')[1]
        details[required_info[3].get_text().encode('utf-8')] = str(data[3].encode('utf-8')).split(':')[1]
        details[required_info[4].get_text().encode('utf-8')] = str(all_data[19].encode('utf-8'))
        all_listings.append(details)
        break
    return all_listings

def start():
    relevant_data = get_page_data(url)
    parsed_data = parse_page_data(relevant_data)
    display_parsed_data(parsed_data)

def display_parsed_data(data):
    for detail in data:
        for key in detail:
            print key, type(key), ' : ', detail[key], type(detail[key])

start()
