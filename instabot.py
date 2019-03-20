from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time

class instabot:

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.driver = webdriver.Chrome("C:\\Users\\Sheharyar Haq\\Desktop\\chromedriver.exe")

		def closebrowser(self):
			self.driver.close()

			def login(self):
				 driver = self.driver
				 driver.get("https://www.instagram.com/")
				 time.sleep(2)

				#<a href="/accounts/login/?source=auth_switcher">Log in</a>
				# "//a[@href'accounts/login']"
				#<input class="_2hvTZ pexuQ zyHYP" id="f1c62c23af5fa3" aria-label="Phone number, username, or email" aria-required="true" autocapitalize="off" autocorrect="off" maxlength="75" name="username" type="text" value="">
				# "//input[@name='username']"
				# "//input[@name='password']"

				myIG = instabot("hello", "passwod1234")
				myIG.login()
