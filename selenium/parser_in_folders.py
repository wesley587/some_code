from selenium import webdriver
from time import sleep
import csv

url = 'https://github.com/BC-SECURITY/Empire/tree/master/data/module_source'
driver = webdriver.Firefox(executable_path='C:/geckodriver.exe')
driver.get(url)
arquivo = dict()
xpaths = driver.find_elements_by_xpath('//a[@class="js-navigation-open link-gray-dark"]')
for pastas in range(0, len(xpaths)):
    sleep(2)
    xpaths = driver.find_elements_by_xpath('//a[@class="js-navigation-open link-gray-dark"]')
    xpaths[pastas].click()
    sleep(2)
    files = driver.find_elements_by_xpath('//a[@class="js-navigation-open link-gray-dark"]')
    sleep(2)
    for file in range(0, len(files)):
        a = driver.find_elements_by_xpath('//a[@class="js-navigation-open link-gray-dark"]')
        file_name = a[file].text
        arquivo[file_name] = list()
        a[file].click()
        sleep(2)
        count = 0
        outher = driver.find_elements_by_xpath('//a[@class="js-navigation-open link-gray-dark"]')
        if len(outher) >= 1:
            print('outer')
            for x in range(0, len(outher) - 5):
                outher = driver.find_elements_by_xpath('//a[@class="js-navigation-open link-gray-dark"]')
                outher[x].click()
                sleep(2)
                while True:
                    count += 1
                    try:
                        a = driver.find_element_by_xpath(f'//td[@id="LC{count}"]')
                    except:
                        break
                    try:
                        a = driver.find_element_by_xpath(f'//td[@id="LC{count}"]//span[@class="pl-en"]')
                    except:
                        pass
                    else:
                        arquivo[file_name].append([count, a.text])
                driver.back()
        else:
            while True:
                count += 1
                try:
                    row = driver.find_element_by_xpath(f'//td[@id="LC{count}"]')
                except:
                    break
                try:
                    row = driver.find_element_by_xpath(f'//td[@id="LC{count}"]//span[@class="pl-en"]')
                except:
                    pass
                else:
                    arquivo[file_name].append([count, row.text])
        print(arquivo)
        sleep(2)
        driver.back()
    driver.back()
    sleep(2)


for key, value in arquivo.items():
    with open(f'{key}.csv', 'w', newline='') as f:
        row = csv.writer(f)
        row.writerow(['line', 'function'])
        for x in value:
            row.writerow(x)
