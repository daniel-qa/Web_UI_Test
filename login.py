#!/usr/bin/python
# -*- coding: utf-8 -*-

#=== Web Unit Test ===
# Date    : 2018.04.26
# Program : login
# Author  : daniel
#===========================
from selenium import webdriver
from time import sleep
#==============================
# function :login_function
# Parameter :	
#	dr->must given
def login_function(dr,url="http://product.company.com.tw",wait_time=1,user_id="qa",password="qa"):
	ex=""
	try:
		#1/0  # for debug Error Case
		# Get Web Driver
		#dr = webdriver.Firefox(executable_path = 'D:/Code/py/lib/geckodriver.exe')	
		# Get Url
		#url='http://www.google.com.tw'		
		dr.get(url)
		dr.maximize_window()
		sleep(wait_time)
		# UserName
		inputElement = dr.find_element_by_id("inputUsername")
		inputElement.send_keys(user_id)
		# Password
		inputElement = dr.find_element_by_id("inputPassword")
		inputElement.send_keys(password)
		# Confirm
		inputElement = dr.find_element_by_id("btnLoginConfirm")
		inputElement.click()
		#print(dr.title)
		#print('Login OK')
		ret="OK"
	except Exception,ex:
		#print(Exception,":",ex)	
		ret="Fail"
		
	return ret,ex


if __name__== "__main__":
	print ("This is main function called")
	# Main
	# Get Web Driver
	dr = webdriver.Firefox(executable_path = 'c:/python27/Lib/geckodriver.exe')
	#print('call check_mail_function()')
	#ret = login_function(dr)
	ret = login_function(dr,url="http://product.company.com.cn")
	print("login_function : " + ret[0]+ "  " + str(ret[1]) )
	sleep(5)
	# Close Web Driver
	dr.quit()

