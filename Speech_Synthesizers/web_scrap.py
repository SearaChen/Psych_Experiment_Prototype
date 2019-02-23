
import selenium

from selenium import webdriver
import time
import sys
import shutil
import os

'''
Install selenium, chrome web browser
'''
elements = ["/mʊmˈba/",""]
br = webdriver.Safari()
br.get('https://itinerarium.github.io/phoneme-synthesis/')

default_download_dir = "/Users/Seara/Downloads/" # the default folder where is download
target_download_dir ="/Users/Seara/Desktop/COMP480/To_Speech_Models/web_result/";
for index,item in enumerate(elements):
	print ("!")
	inputElement = br.find_element_by_id("ipa-input")
	inputElement.send_keys(item)
	inputElement.submit() 


	# output
	#time.sleep(0.5)
	outputElement = br.find_element_by_id("submit").click()

	outputElement = br.find_element_by_id("download-button").click()
	inputElement.clear()


	for fname in os.listdir(default_download_dir):
		if fname.endswith('.wav'):
			print (fname)
			os.rename(default_download_dir+fname, target_download_dir+str(index)+".wav")






