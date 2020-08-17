import requests
from lxml import etree

import selenium.webdriver.support.ui as ui
from selenium import webdriver

url = input("Please input your property url: ")
if url == 'c':
    url = "https://www.sinyi.com.tw/buy/house/80965J/?breadcrumb=list"

chrome = webdriver.Chrome('./chromedriver')
wait = ui.WebDriverWait(chrome, 10)
chrome.get(url)
wait.until(lambda driver: driver.find_element_by_class_name('buy-content-title-name'))

#name = chrome.find_element_by_xpath('//*[@class="buy-content-title-name"]')
name        = chrome.find_element_by_class_name('buy-content-title-name')
address     = chrome.find_element_by_class_name('buy-content-title-address')
square_feet = chrome.find_element_by_class_name('buy-content-title-uni-price')
price       = chrome.find_element_by_class_name('buy-content-title-total-price')
agent_name  = chrome.find_element_by_class_name('buy-content-agent-name-area')  
agent_phone = chrome.find_element_by_class_name('buy-content-agent-phone-area')  

print(name.text)
print(address.text)
print(square_feet.text)
print(price.text)
print(agent_name.text)
print(agent_phone.text)

basic_cells = chrome.find_elements_by_class_name('buy-content-basic-cell')
print(len(basic_cells))

for cell in basic_cells:
    try:
        title = cell.find_element_by_class_name('basic-title')
        value = cell.find_element_by_class_name('basic-value')
        print(f"{title.text}: {value.text}")
    except:
        pass

chrome.close()
"""

basic_info_block = html.xpath('//*[@id="__next"]/div/div/span/div[3]/div/div/div[5]/div[3]/div[2]')

basic_cell_dict = {}

for cell in basic_info_block:

    c = cell.xpath('//div[@class="buy-content-basic-cell"]')

    for ele in c:
        title = ele[0]
        value = ele[1]
        basic_cell_dict[title.text] = value.text

print(basic_cell_dict)
"""
