import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.ui import Select

import logging
import os.path,subprocess
from subprocess import STDOUT,PIPE
from selenium import webdriver
import unicodedata

def instantiate_driver():
    downdir = '/Users/madhuripalagummi/Desktop/MyStuff/Grader/'
    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory' : downdir}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome('/Users/madhuripalagummi/Desktop/MyStuff/Setups/chromedriver', chrome_options=chrome_options)
    driver.implicitly_wait(10)

    return driver


def scrapeNews():

	driver = instantiate_driver()
	sportsLink = "https://inshorts.com/en/read/sports"
	driver.get(sportsLink)
	time.sleep(5)

	cards = driver.find_elements_by_class_name('news-card')
	titles = driver.find_elements_by_xpath("//span[@itemprop='headline']")
#/html/body/div[4]/div/div[3]/div[17]/div/div[2]/a/span
#/html/body/div[4]/div/div[3]/div[17]/div/div[3]/div[1]	

	page = 0
	cardId = 0
	while (page!=2):
		f = open("demofile.txt", "a")
		cards = driver.find_elements_by_class_name('news-card')
		content = ""
		for card in cards[cardId:]:

			content += str(cardId)+"\t"
			print("CardId :   ", cardId)
			title = card.find_element_by_xpath("div[2]/a/span").text + ""
			title = unicodedata.normalize('NFKD', title).encode('ascii','ignore')
			print (title)
			content += title + "\t"

			article = card.find_element_by_xpath("div[3]/div[1]").text
			article = unicodedata.normalize('NFKD', article).encode('ascii','ignore')
			print (article)
			content += article + "\t"

			link = card.find_element_by_xpath("div[2]/a").get_property('href')
			link = unicodedata.normalize('NFKD', link).encode('ascii','ignore')
			print (link)
			content += link + "\n"
			f.write(content)
			cardId += 1

		f.close()
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(4)
		loadMorebutton = driver.find_element_by_xpath('//*[@id="load-more-btn"]')
		loadMorebutton.click()

		page += 1


scrapeNews()