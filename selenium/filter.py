from selenium import webdriver
from selenium.webdriver.firefox.options import Options

option = Options()
option.headless = True
driver = webdriver.Firefox(executable_path='C://geckodriver.exe', options=option)

url = 'https://github.com/BC-SECURITY/Empire/blob/a58e0a5e608b1ebed5f81d8018105d020735db89/data/module_source/situational_awareness/network/powerview.ps1'
driver.get(url)

nomes = driver.find_elements_by_xpath('//span[@class="pl-en"]')
func_names = list()
for x in nomes:
    func_names.append(x.get_attribute('innerHTML'))
