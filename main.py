from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import time

driver = webdriver.Chrome(executable_path="C:/SeleniumDrivers/chromedriver.exe")
  
driver.get("https://www.indianyellowpages.com/ahmedabad/digital-marketing-services.htm")
  
# Maximize the window and let code stall 
# for 10s to properly maximise the window.
driver.maximize_window()
time.sleep(5)

# Obtain button by link text and click.
for i in range(5):
    button = driver.find_element_by_id("load_more_a_id")
    button.click()
    time.sleep(5)

header =['Company Name', 'Address']
result = []

html_text = driver.page_source
# html_text = requests.get('https://www.indianyellowpages.com/ahmedabad/digital-marketing-services.htm')
soup = BeautifulSoup(html_text, "html.parser")
# print(soup)
for item in soup.find_all('div', attrs={'class': 'classified fo iyp-list'}):
    name = item.find('h3', attrs={'class': 'name'}).get_text(strip=True)
    address_c = item.find('p', attrs={'class': 'gray large sub-title'})
    address = address_c.find('a', attrs={'class': 'add-tooltip'})
    f = address.get('title', 'No title attribute')
    result.append[[name, f]]
with open('companydetails.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(result)