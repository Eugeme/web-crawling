from bs4 import BeautifulSoup
from requests import get
from openpyxl import load_workbook


url = 'https://www.baustoffshop.de/catalogsearch/result/?q=1040bs'
result = get(url)
soup = BeautifulSoup(result.text, 'html.parser')
urls = soup.find_all('a', class_="product-thumb-link")
for i in range(len(urls)):
    urls[i] = urls[i]['href']

    
def find_data(url):
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    ean = soup.find('div', class_="product attribute content_technicalfact_3")
    price = soup.find('div', class_="price-box").find('span', class_='price')
    ean = ean.text.strip()[5:]
    price = price.text[:-2]
    return ean, price


workbook = load_workbook('test_task_output_format.xlsx')
worksheet = workbook.active
for i in range(len(urls)):
    worksheet['A' + str(i)].value = find_data(urls[i])[0]
    worksheet['B' + str(i)].value = find_data(urls[i])[1]
workbook.save('test_task_output_format.xlsx')
