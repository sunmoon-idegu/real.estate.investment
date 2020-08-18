import re
from lxml import etree

import selenium.webdriver.support.ui as ui
from selenium import webdriver

from main import *

url = input("Please input your property url: ")
if url == 'c':
    url = "https://www.sinyi.com.tw/buy/house/91134B/?breadcrumb=list"

chrome = webdriver.Chrome('./chromedriver')
wait = ui.WebDriverWait(chrome, 10)
chrome.get(url)
wait.until(lambda driver: driver.find_element_by_class_name('buy-content-title-name'))

#name = chrome.find_element_by_xpath('//*[@class="buy-content-title-name"]')
name        = chrome.find_element_by_class_name('buy-content-title-name')
address     = chrome.find_element_by_class_name('buy-content-title-address')
square_feet = chrome.find_element_by_class_name('buy-content-title-uni-price')
price       = chrome.find_element_by_class_name('buy-content-title-total-price')

layout      = chrome.find_element_by_class_name('buy-content-detail-layout')
number_of_room = int(layout.text.split('房')[0])

agent_name  = chrome.find_element_by_class_name('buy-content-agent-name-area')
agent_phone = chrome.find_element_by_class_name('buy-content-agent-phone-area')  

print(name.text)
print(address.text)
print(square_feet.text)
price = float(''.join(x for x in price.text if x.isdigit()))
print(price)
#print(price.text)
print(agent_name.text)
print(agent_phone.text)

basic_cells = chrome.find_elements_by_class_name('buy-content-basic-cell')

cell_dict = {}
for cell in basic_cells:
    try:
        title = cell.find_element_by_class_name('basic-title')
        value = cell.find_element_by_class_name('basic-value')
        print(f"{title.text}: {value.text}")

        if title.text:
            cell[title.text] = value.text
    except:
        pass

renovation_cost_percentage = float(input(f"Please input your renovation cost (in percentage of the full price {price} w): "))
renovation_cost = price * (renovation_cost_percentage / 100)

print(f"Your renovation cost will be {renovation_cost} w")

total_cost = price + renovation_cost

print(f"Your total cost will be {total_cost} w.")

down_payments_percentage = float(input(f"Please input your down payment (in percentage): "))
down_payments = total_cost * (down_payments_percentage / 100)

total_loan = total_cost - down_payments

print(f"Your down_payments will be {down_payments} w.")
print(f"Your loan will be {total_loan} w.")

number_of_payment = int(input("Please input your loan period (in years): ")) * 12

interest_rate = float(input("Please input your annual interest rate (in percentage): "))

monthly_loan_payment = get_payment(number_of_payment, total_loan, 0, interest_rate)
annually_loan_payment = monthly_loan_payment * 12

print(f"Monthly loan payment: {monthly_loan_payment} w.")
print(f"Annually loan payment: {annually_loan_payment} w.")

rent_per_room = float(input("Please input your average rent per room (in w): "))

total_rent = rent_per_room * number_of_room

print(f"Total room number is {number_of_room}.")
print(f"Total rent per month is {total_rent} w.")

operating_cost = float(input("Please input your operating cost per month (in w): "))

net_operating_income = (total_rent - operating_cost)
net_operating_income_annual = net_operating_income * 12

print(f"Monthly net operating income: {net_operating_income} w.")
print(f"Annually net operating income: {net_operating_income_annual} w.")

cap_rate = (net_operating_income_annual / total_cost) 

print(f"Capitalization rate: {cap_rate * 100} %.")

profit = net_operating_income_annual - annually_loan_payment

print(f"Profit (per year): {profit} w.")

cash_on_cash = profit / down_payments

print(f"Cash on cash: {cash_on_cash * 100} %.")

get_payment_interest_sensitivity(number_of_payment, total_loan, 0, min_r=0.5, max_r=2.5, grid=101, monthly_rent=total_rent)

chrome.close()
