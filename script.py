import os
from selenium import webdriver

if __name__ == "__main__" :
	print('Hello World!')
	os.system('notepad')
	browser = webdriver.Chrome()
	browser.get('https://www.oracle.com/java/technologies/javase-jdk14-downloads.html')
