#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver

# Get Web Driver
driver = webdriver.Firefox()
# Get Url
url='http://www.google.com.tw'
driver.get(url)

# Check Context txt
driver.find_element_by_xpath("//*[contains(text(), '台灣')]").is_displayed()
