#!/usr/bin/python
# -*- coding: utf-8 -*-

#=== Product Unit Test =========
# Date    : 2018.10.17
# Program : Test Case Main
# Author  : daniel
#===========================

import os
import unittest, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from login import login_function
from check_mail import check_mail_fun
from import_student import import_student_fun
from add_paper import add_paper_fun
from add_quiz import add_quiz_fun
from add_grade import add_grade_fun
from add_cms_folder import add_cms_folder_fun
from collaborative_teacher import collaborative_teacher_fun
from add_student import add_student_fun
from write_quiz import write_quiz_fun
from HD_upload import HD_upload_fun

class Web_UnitTest(unittest.TestCase):
	""" Web Server Unit Test"""
	def setUp(self):
		""" Init Parameter , Login """
		self.driver = webdriver.Firefox(executable_path = 'C://Python27//Lib//geckodriver.exe')
		#self.driver = webdriver.Chrome(executable_path = 'D:/Code/py/lib/chromedriver.exe')
		
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
		
		
		#Set Url
		self.url=product_url
		#Set Language
		self.lang=product_lang
		#Set Wait Time
		self.wait_time = wait_time
		
		# login
		login_function(self.driver,self.url,self.wait_time)

	def test_login(self):
		"""	login """
		login_function(self.driver,self.url,self.wait_time)
		print(u" 登入 ")		
		
	def test_check_mail(self):
		"""	cehck mail """
		check_mail_fun(self)
		#print(" check mail : ")
		print(u" 檢查 mail ,收信 ")	
		
	def test_import_student(self):
		"""	import_student """	
		import_student_fun(self)
		#print(" import student  ")
		print(u" 匯入學生excel名單  ")
	
	def test_add_paper(self):
		"""	add_paper """
		add_paper_fun(self)		
		#print(" add paper  ")
		print(u" 新增一分試卷  ")
		
	def test_add_quiz(self):
		"""	add_quiz """		
		add_quiz_fun(self)		
		#print(" add quiz  ")
		print(u" 新增一個測驗活動  ")
    
	def test_add_grade(self):
		"""	add_grade """		
		add_grade_fun(self)		
		#print(" add grade  ")
		print(u" 在成績管理中，新增/修改/刪除學生的成績  ")
	
	def test_add_cms_folder(self):
		"""	add_cms_folder """
		add_cms_folder_fun(self)		
		#print(" add cms folder  ")
		print(u" 新增一個cms影音資料夾，之後刪除資料夾  ")
		
	def test_collaborative_teacher(self):
		"""	collaborative_teacher """
		collaborative_teacher_fun(self)		
		#print(" collaborative_teacher  ")
		print(u" 新增一位協同老師，之後刪除協同老師  ")
    
	def test_add_student(self):
		"""	add_student """
		add_student_fun(self)		
		#print(" add_student  ")
		print(u" 搜尋挑選，加入一名學生  ")
	
	def test_write_quiz(self):
		"""	write_quiz """
		write_quiz_fun(self)		
		#print(" write_quiz  ")
		print(u" 新增測驗後，由學生進行寫考卷  ")
    
	def test_HD_upload(self):
		"""	HD_upload """
		HD_upload_fun(self)		
		#print(" HD_upload  ")
		print(u" 我的硬碟-上傳一個普通檔案  ")
	
	def tearDown(self):
		self.driver.quit()	

if __name__ == '__main__':
	
	#Set Python Code Page
	#os.system('chcp 936') 
	#Call Unit Test
	unittest.main()
	
	sleep(3)
	if(0):		
		Product_UnitTest.login()
		