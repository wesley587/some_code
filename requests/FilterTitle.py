import requests
from bs4 import BeautifulSoup

resp = requests.get('http://pythonclub.com.br')
soup = BeautifulSoup(resp.content, 'html.parser')
parser = soup.find_all('a', {'class': 'post-title'})
for x in parser:
    print(x.text)

#ou usando list comprehension
'''
import requests
from bs4 import BeautifulSoup

resp = requests.get('http://pythonclub.com.br')
soup = BeautifulSoup(resp.content, 'html.parser')
parser = [x.text for x in soup.find_all('a', {'class': 'post-title'})]
print(parser)
'''
