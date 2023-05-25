#====================================================================
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Program : login
# Author  : daniel
#====================================================================
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from time import sleep
import logging
from selenium.webdriver.firefox.options import Options
import re
import requests	
    
FORMAT = '%(asctime)s %(message)s'  # 時間
#logging.basicConfig(level=logging.DEBUG,format=FORMAT)  # 詳細資訊
logging.basicConfig(level=logging.INFO,format=FORMAT)   # Info
#logging.basicConfig(level=logging.CRITICAL,format=FORMAT)   # 重大 Error 才輸出

#====================================================================
# function :login
# Parameter :	
#	driver->must given

# Login
def login(driver,url="https://www.teammodel.net/login",tmid = "user",pwd = "a12345678"):
	
	#driver = webdriver.Firefox()
	driver.get(url)
	driver.maximize_window()
	
	#  Wait Page Load
	WebDriverWait(driver, 60).until(visibility_of_element_located((By.XPATH, "//span[@class='subtitle']")))
	
	## 身分
	elements = driver.find_elements_by_xpath("//span[@class='subtitle']")
	#print(len(elements))
	elements[0].click()
	
	# Wait Page Load Finish
	WebDriverWait(driver, 60).until(visibility_of_element_located((By.ID, 'tmdID')))
	 
	# 輸入 TMID		
	element = driver.find_element_by_id("tmdID")
	element.send_keys(tmid)
	logging.info("輸入 TMID")
	
	# 輸入 PWD
	#pwd = "a12345678"
	element = driver.find_element_by_id("tmdpw")
	element.send_keys(pwd)
	logging.info("輸入 PWD")
	
	sleep(5)
	# 登入 Button
	element = driver.find_element_by_xpath("//i[contains(@class,'ivu-icon-md-arrow-forward')]")
	element.click()
	logging.info("登入 Button")
	
	# check login status
	#WebDriverWait(driver, 60).until(visibility_of_element_located((By.XPATH, "//span[contains(@class,'ivu-badge')]")))
	driver.find_element_by_xpath("//span[contains(@class,'ivu-badge')]").is_displayed()
	logging.info("Login finish ")

if __name__== "__main__":
	#print("This is main function called")
	
	# Web Driver
	
	# Web Driver
	#driver = webdriver.Firefox()	
	options = Options()
	options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'	
	driver = webdriver.Firefox(options=options)	
	
	driver.implicitly_wait(7)	
	
	# url
	url="https://www.example.com"		
	
	tmid = 'guest'
	
	# pwd
	pwd = 'guest.'
	logging.info("Login")	
	
	login(driver,url,tmid,pwd)
	
	print("login finish " )
	
	sleep(3)
	# Close Web Driver
	#driver.quit()	
	
	url2= url + "/home/system"
	driver.get(url2)
	sleep(3)
	
	url2=  url + "/home/settings?tab=0"		
	# 設定語系
	driver.get(url2)
	sleep(1)
	
	element = driver.find_element_by_xpath("//li[text()='English']")	
	#element.click()
	driver.execute_script("arguments[0].click();", element)
	sleep(3)
	
	url3= url + "/area/areaIndex"
	driver.get(url3)
	sleep(3)
  
  driver.quit()
