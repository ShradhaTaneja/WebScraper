import requests, json
from bs4 import BeautifulSoup

url = 'http://www.cry.org/careers/current-openings'

def get_page_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    blocks = soup.find_all(class_='panel-body')
    heading = soup.find_all(class_='panel-title')
#    for a in heading :
#        print type(a), a.get_text(), '_______________'

    for a in blocks:
        print '--------------------------------------\n', a
#    print soup.select('h4 .panel-title')
    return blocks

#required_info = blocks[0].select('b')

#block = blocks[0]
#for i, v in enumerate(list(block.children)):
#    print i, ' = ', v

def parse_page_data(data):
    all_listings = []
    required_info = data[0].find_all(['b', 'strong'])

    for block in data:
#        print '____'*30, '\n', block, '__\n'
        all_data = list(block.children)
        data = all_data[2::4]
#        print data, '<<<<<<<<<<<<<<<<<<'
        details = {}
#        details[required_info[0].get_text().encode('utf-8')] = str(data[0].encode('utf-8')).split(':')[1]
#        details[required_info[1].get_text().encode('utf-8')] = str(data[1].encode('utf-8')).split(':')[1]
#        details[required_info[2].get_text().encode('utf-8')] = str(data[2].encode('utf-8')).split(':')[1]
#        details[required_info[3].get_text().encode('utf-8')] = str(data[3].encode('utf-8')).split(':')[1]
#        details[required_info[4].get_text().encode('utf-8')] = str(all_data[19].encode('utf-8')).lstrip()
#        all_listings.append(details)
    return all_listings

def start():
    print '-'*100
    print '\t \t Scraping CRY website (%s)' % url
    print '-'*100
    relevant_data = get_page_data(url)
    parsed_data = parse_page_data(relevant_data)
    display_parsed_data(parsed_data)

def display_parsed_data(data):
    print '\n \t \t Openings Found : '
    for idx, detail in enumerate(data):
        print '_' * 10
        print '  ', idx+1
        print '_' * 10
#        for key in detail:
#            print '\t ', key, ' : ', detail[key]

start()
