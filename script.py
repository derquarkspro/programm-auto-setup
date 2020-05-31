import os
from selenium import webdriver
PATH = "C:\Program Files (x86)\Google\Chrome\chromedriver.exe"

if __name__ == "__main__" :
	print('Hello World!')
	os.system('notepad')
	browser = webdriver.Chrome(PATH)
	browser.get('https://www.oracle.com/java/technologies/javase-jdk14-downloads.html')
