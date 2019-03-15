#!/usr/bin/python
# -*- coding: utf-8 -*-

#=== Product Unit Test =====
# Date    : 2019.03.15
# Program : check_mail
# Author  : daniel
#===========================
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from login import login_function

# This is shell
def check_mail_fun(self):
	#print "Enter check_mail_fun"
	#1/0
	# check_mail_fun
	driver = self.driver
	wait_time = int(self.wait_time)	
	
	check_mail_function(driver,wait_time)	


# for __main__ , Design...ing
# This is Reall Function Body
# Parameter
# 	driver : must give
def check_mail_function(driver,wait_time=3):
	# Head Img
	sleep(wait_time)
	element = driver.find_element_by_id("head_img")
	element.click()
	sleep(wait_time)
	element = driver.find_element_by_xpath("//a[contains(@href,'Fucn=eMessage')]")
	element.click()

if __name__== "__main__":
	print ("This is main function called")	
	
	os.system('chcp 936')
	
	#Set Default Wait Time
	wait_time = 1
	# 設定網址，語系:'cn','tw','en'
	if(1):
		product_url= 'http://product2.company.com.cn'
		product_lang = 'cn'				
	if(0):
		product_url= 'http://product.company.com.tw'
		product_lang = 'tw'
	if(0):
		product_url= 'http://product.company.com.cn'
		product_lang = 'cn'
		wait_time = 2 # 大陸等級時間較久
	if(0):
		product_url= 'http://product.class.com.tw'
		product_lang = 'en'		
	if(0):
		product_url= 'http://192.168.1.228'
		product_lang = 'tw'		
	if(0):
		product_url= 'http://192.168.0.200'
		product_lang = 'tw'		
	if(0):
		product_url= 'http://222.175.100.115' # 山東歷下
		product_lang = 'cn'		
	if(0):
		product_url= 'http://192.168.1.228:8080' # Product Release
		product_lang = 'cn'

	print ies_url + '   lang: ' + ies_lang
	
	# Get Web Driver
	driver = webdriver.Firefox(executable_path = 'C://Python27/Lib//geckodriver.exe')
	# login
	login_function(driver,url=ies_url,wait_time=wait_time)
	check_mail_function(driver)
	sleep(5)
	# Close Web Driver
	driver.quit()


