from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.property24.com/houses-to-rent/johannesburg/gauteng/100#SortOrder').text

soup = BeautifulSoup(source, 'lxml')

for all_content in soup.find_all('span', class_='p24_content'):
    title = all_content.find('span', class_='p24_title')
    price = all_content.find('span', class_='p24_price')
    features = all_content.find('span', class_='p24_features')
    excerpt = all_content.find('span', class_='p24_excerpt')
    area = all_content.find('span', class_='p24_bold')
    print(title.text)
    print(price.text)
    print(features.text)
    print(excerpt.text)
    print(area.text)
    print('****************************')