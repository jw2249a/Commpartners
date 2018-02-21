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

variable = 0
counter = 0
target_file = "C:/Users/jwilliams/Desktop/working_file.csv"

# open data csv
def getFirst(str):
	csvfile = open(str, "rt", encoding ="utf-8")
	csvfile = csv.reader(csvfile)
	for row in csvfile:
		header = row
		break
	return(header)
#start chrome
def loadWebDriver():
	options = webdriver.ChromeOptions()
	options.add_argument("user-data-dir=C:/Users/jwilliams/AppData/Local/Google/Chrome/User Data") #Path to your chrome profile
	browser = webdriver.Chrome(executable_path="C:/Users/jwilliams/Documents/chromedriver.exe", chrome_options=options)

if len(sys.argv) == 1:
	print("you didn't add an argument dumb***")
	quit()
else:
	print('checking %s' % sys.argv[1])
	#iterate over variables for target
	header = getFirst(target_file)
	col_count = len(header)
	for target in header:
		if counter == 0:
			if (sys.argv[1] == target):
				print('Target Found...')
				print('for %s right?' % target)
				b =1
				counter+=1
				quit()
			else:
				variable+=1
				if variable == col_count:
					print("could't find anything. sorry man")
					quit()
		else:
		#login script
			base_url = 'https://elearning.asam.org'
			browser.get(base_url)
			time.sleep(2.5)
			browser.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[2]/div/div/div/ul[1]/li/form/a").click()
			time.sleep(1.5)
			count = 0

			while count < 2:
				count+=1
				time.sleep(1.5)
				login = browser.find_elements_by_css_selector('input[class=username-input]')
				login[0].send_keys(USERNAME)
				time.sleep(2)
				login = browser.find_elements_by_css_selector('input[class=password-input]')
				login[0].send_keys(PASSWORD)
				time.sleep(3)
				login = browser.find_elements_by_css_selector('#btnSubmit')
				login[0].click()
				time.sleep(2)
				browser.get("%s/%s" % base_url + additional_args)
				time.sleep(50)
				browser.quit()
