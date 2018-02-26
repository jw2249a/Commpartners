import time
import csv
import sys
from sys import argv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import win32com.client
shell = win32com.client.Dispatch("WScript.Shell")

target_file = "working_file.csv"

# open data csv
def getTarget(str, target):
	variable = 0
	csvfile = open(str, "rt", encoding ="utf-8")
	csvfile = csv.reader(csvfile)
	for row in csvfile:
		header = row
		col_count = len(header)
		for name in header:
			print("%s  %s" % (target,name))
			if target==name:
				break
			else:
				variable+=1
				if variable == col_count:
					print("could't find anything. sorry man")
					quit()
		break
	return(header, variable)
#start chrome
def loadWebDriver():
	options = webdriver.ChromeOptions()
	options.add_argument("user-data-dir=C:/Users/jwilliams/AppData/Local/Google/Chrome/User Data") #Path to your chrome profile
	browser = webdriver.Chrome(executable_path="C:/Users/jwilliams/Documents/chromedriver.exe", chrome_options=options)
	return(browser)

def loadUserInfo(str):
	with open(str, 'r') as f:
		user_info = f.read()
	return(user_info)
def login():
	base_url = 'https://elearning.asam.org'
	browser.get(base_url)
	time.sleep(2.5)
	# find login page
	browser.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[2]/div/div/div/ul[1]/li/form/a").click()
	time.sleep(1.5)
	# get username and enter it
	USERNAME = loadUserInfo("USERNAME")
	login = browser.find_elements_by_css_selector('input[class=username-input]')
	login[0].send_keys(USERNAME)
	# get password and enter it
	login = browser.find_elements_by_css_selector('input[class=password-input]')
	PASSWORD = loadUserInfo("PASSWORD")
	login[0].send_keys(PASSWORD)
	# click submit
	time.sleep(1)
	login = browser.find_elements_by_css_selector('#btnSubmit')
	login[0].click()

def UpdateInfo(target, id, value):
	if target=="title":
		print("hiiiiiiii")
	elif target=="url_slug":
		print("hiiiiiiii")
	elif target=="summary":
		print("hiiiiiiii")
	elif target=="description":
		print("hiiiiiiii")
	elif target=="start_sales_at":
		print("hiiiiiiii")
	elif target=="end_sales_at":
		print("hiiiiiiii")
	elif target=="end_sales_auto_status":
		print("hiiiiiiii")
	elif target=="auto_status_date":
		print("hiiiiiiii")
	elif target=="show_in_catalog":
		print("hiiiiiiii")
	elif target=="remote_product_id":
		print("hiiiiiiii")
	elif target=="meta_keywords":
		print("hiiiiiiii")
	elif target=="meta_description":
		print("hiiiiiiii")
	elif target=="max_days_for_completion":
		print("hiiiiiiii")
	elif target=="remote_accounting_code":
		print("hiiiiiiii")
	elif target=="show_search_for_package":
		print("hiiiiiiii")
	elif target=="categories":
		print("hiiiiiiii")

if len(sys.argv) == 1:
	print("you didn't add an argument dumb***")
	quit()
else:
	print('checking %s' % sys.argv[1])
	#iterate over variables for target
	result = getTarget(target_file, sys.argv[1])
	for target in result[0]:
		print(target)
		print(result[1])
		if counter == 0:
			if sys.argv[1] == target:
				print('Target Found...')
				time.sleep(10)
				print('for %s right?' % target)
				b = 1
				counter+=1

		else:
			browser = loadWebDriver()
			login()
			UpdateInfo(target)
			browser.get("%s/%s" % base_url + additional_args)
			time.sleep(50)
			browser.quit()
