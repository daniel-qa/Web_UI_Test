#!/usr/bin/python
# -*- coding: utf-8 -*-

# Get Web Driver
driver = webdriver.Firefox()
# Get Url
url='http://www.google.com.tw'
driver.get(url)

# check element
driver.find_element_by_xpath(" xxxx").is_displayed() 
