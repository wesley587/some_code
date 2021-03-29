from selenium import webdriver
from bs4 import BeautifulSoup
import csv
driver = webdriver.Firefox(executable_path='C:/geckodriver.exe')
count = 0
lines = list()
functions = list()
driver.get('https://github.com/BC-SECURITY/Empire/blob/a58e0a5e608b1ebed5f81d8018105d020735db89/data/module_source/situational_awareness/network/powerview.ps1')
for x in range(15, 21484):
    value = driver.find_element_by_xpath(f'//td[@id="LC{x}"]')
    parser = value.get_attribute('innerHTML')
    soup = BeautifulSoup(parser, 'html.parser')
    name = soup.find('span', {'class': 'pl-en'})
    if name:
        print(x, name)
        lines.append(x)
        count += 1
        functions.append(name.text)

print(count)

with open('my_file.csv', 'w', newline='') as f:
    row = csv.writer(f)
    row.writerow(['row', 'function'])
    for x in zip(lines, functions):
        row.writerow([x[0], x[1]])
