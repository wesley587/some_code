from bs4 import BeautifulSoup
import requests
import csv
url = 'https://github.com/BC-SECURITY/Empire/blob/a58e0a5e608b1ebed5f81d8018105d020735db89/data/module_source/situational_awareness/network/powerview.ps1'
resp = requests.get(url)
soup = BeautifulSoup(resp.content, 'html.parser')

func_names = list()
rows = list()

for x in range(1, 21480):
    parser = soup.find('td', {'id': f'LC{x}'})
    func = parser.find('span', {'class': 'pl-en'})
    if func:
        func_names.append(func.text)
        rows.append(x)

with open('my_file.csv', 'w', newline='') as f:
    row = csv.writer(f)
    row.writerow('row, function')
    for x in zip(rows, func_names):
        row.writerow([x[0], x[1]])
