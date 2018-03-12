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

def EraseText():
	# this is probably the hackiest thing i've ever done
	actions = ActionChains(browser)
	actions.send_keys(Keys.CONTROL)
	actions.send_keys("A")
	actions.send_keys(Keys.BACKSPACE)
	actions.send_keys(Keys.DELETE)
	x = 1
	while x < 100:
		actions.perform()
		x+=1

def UpdateInfo(target, id, value):
	# gets the item's editing page by the
	page = "https://elearning.asam.org/admin/products/%s/edit" % id
	browser.get(page)

	# defining the Tabs to click
	save = browser.find_element_by_id("btn-save-product-and-stay")
	description = browser.find_element_by_id('tab_basic')
	pricing = browser.find_element_by_id('tab_pricing')
	sales_date = browser.find_element_by_id('tab_status')
	packages = browser.find_element_by_id('tab_packages')
	time_limit = browser.find_element_by_xpath("//*[@id='prod_tabs']/li[5]/a")
	categories = browser.find_element_by_xpath("//*[@id='prod_tabs']/li[6]/a")
	seo = browser.find_element_by_xpath("//*[@id='prod_tabs']/li[7]/a")
	social = browser.find_element_by_xpath("//*[@id='prod_tabs']/li[8]/a")
	integration = browser.find_element_by_xpath("//*[@id='prod_tabs']/li[9]/a")

	if target=="title":
		description.click()
		title = browser.find_element_by_id("title")
		title.click()
		EraseText()
		title.send_keys("BALALLALALAL")
	elif target=="summary":
		description.click()
		summary = browser.find_element_by_name("summary")
		summary.click()
		EraseText()
		summary.send_keys("BAKAKAKAKAK")
	elif target=="description":
		description.click()
		descript = browser.find_element_by_id("redactor-uuid-0")
		descript.click()
		EraseText()
		# this works but not text alone for some reason
		descript.send_keys(Keys.SPACE)
		descript.send_keys("Blaka Blaka")
	elif target=="alt_url_slug":
		description.click()
		alt_url_slug = browser.find_element_by_name("alt_url_slug")
	elif target=="start_sales_at":
		sales_date.click()
		attack = browser.find_element_by_id("sales_start_at")
		attack.send_keys("YOLO")
	elif target=="auto_end":
		sales_date.click()
		auto_end = browser.find_element_by_id("end_sales_auto_status_checkbox")
		auto_end.click()
		auto_end = browser.find_element_by_id("auto_status_date")
		auto_end.send_keys("BALALALALALALA")
	elif target=="end_sales_at":
		sales_date.click()
		browser.find_element_by_id("sales_end_at")
	elif target=="end_sales_auto_status":
		sales_date.click()
	elif target=="auto_status_date":
		sales_date.click()
	elif target=="show_in_catalog":
		print("hiiiiiiii")
	elif target=="remote_product_id":
		print("hiiiiiiii")
	elif target=="meta_keywords":
		browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/form/div[1]/div/div[7]/textarea[1]")
	elif target=="meta_description":
		browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/form/div[1]/div/div[7]/textarea[2]")
	elif target=="remote_accounting_code":
		browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/form/div[1]/div/div[9]/select")
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
