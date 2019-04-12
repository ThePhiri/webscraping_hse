from bs4 import BeautifulSoup
import requests
import csv
import os

#set website
source = requests.get('https://www.property24.com/houses-to-rent/johannesburg/gauteng/100#SortOrder').text
soup = BeautifulSoup(source, 'lxml')

#csv to be written to
hse_data = open('p24.csv', 'a')
csv_writer = csv.writer(hse_data)

exists = os.path.isfile('p24.csv')

if exists != True:
    csv_writer.writerow(['title', 'price', 'excerpt', 'area'])


#extract content
for all_content in soup.find_all('span', class_='p24_content'):
    try:
        title = all_content.find('span', class_='p24_title').text
        price = all_content.find('span', class_='p24_price').text
        excerpt = all_content.find('span', class_='p24_excerpt').text
        area = all_content.find('span', class_='p24_bold')

        if area == None:
            area = Nan
        else:
            area = area.text
    except:
        pass
    csv_writer.writerow([title, price, excerpt, area])
hse_data.close()