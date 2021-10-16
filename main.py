from bs4 import BeautifulSoup
import requests


html_text = requests.get('https://www.indianyellowpages.com/ahmedabad/digital-marketing-services.htm')
result = []
soup = BeautifulSoup(html_text.content, "html.parser")
# print(soup)
for item in soup.find_all('div', attrs={'class': 'classified fo iyp-list'}):
    name = item.find('h3', attrs={'class': 'name'}).get_text(strip=True)
    address_b = item.find('p', attrs={'class': 'gray large sub-title'})
    address_a = address_b.find('a', attrs={'class': 'add-tooltip'})
    address = address_a.get('title', 'No title attribute')
    # print(name, address)
    result.append([name, address])
print(result)
