from bs4 import BeautifulSoup
from requests import get
from openpyxl import load_workbook


def find_data(url):
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    ean = soup.find('div', class_="product attribute content_technicalfact_3")
    price = soup.find('div', class_="price-box").find('span', class_='price')
    ean = ean.text.replace(' ', '').replace('\n', '')[4:]
    price = price.text[:-2]
    return ean, price


url = 'https://www.baustoffshop.de/catalog/product/view/id/'
urls = ['']
for i in range(1, 6):
    urls.append(url + str(390114+i))
    urls.append(url + str(482287+i))

workbook = load_workbook('test_task_output_format.xlsx')
worksheet = workbook.active
for i in range(2, len(urls)+1):
    worksheet['A' + str(i)].value = find_data(urls[i-1])[0]
    worksheet['B' + str(i)].value = find_data(urls[i-1])[1]
workbook.save('test_task_output_format.xlsx')
