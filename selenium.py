import selenium
from selenium import webdriver
browser=webdriver.Chrome("C:\Users\sadaf\Downloads\simple_python_dialog_system_files\Desktop\chromedriver\chromedriver.exe")
browser.get('http://inventwithpython.com')
linkElem= browser.find_element_by_link_text('read it online')
print(type(linkElem))
linkElem.click()
