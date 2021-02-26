"""
###################################################################

MIT License

----------Beginning of Lisence----------

This license was granted to user 'sanchit-sehgal' on February 21, 2021 at 1:49:15 PM EST.

Copyright (c) 2021 sanchit-sehgal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

-------------End of License-------------


###################################################################
"""

from spinningcursor import *
import time
import sys
import os
import subprocess
import pyautogui
import random 
from PyDictionary import PyDictionary
import pynput
from pynput.keyboard import Key, Controller
import turtle

keyboard = Controller()

def print_options():

	#Presents all of the productivity/system usage commands. 

	print("These are the current options: ")
	print("")
	print("1. Send a notification. This notification will be generated and will appear on your screen.")
	print("2. Browse the web. This will allow you to search any website through the terminal.")
	print("3. Echo a statement. This will return the statement in the terminal.")
	print("4. Perform a system upgrade. You have the option to upgrade your applications as well.")
	print("5. Send pings to a website. This checks your network connection to the web.")
	print("6. Generate the definition, synonyms, or antonyms of a word.")
	print("7. Access all of your files using a graphical user interface in your terminal.")
	print("8. Open any application using the terminal.")
	print("9. View specific tickers, historical data for tickers, or overall market summary for the stock market.")
	print("10. View memory information. This provides information about your RAM and SWAP usage.")
	print("11. View disk usage. This provides information about the storage on your computer.")
	print("12. View processor information. This provides information about the type of processor, core clock, and model information.")
	print("13. View shortened overall hardware information. This provides cumulative information on all components of your computer.")
	print("14. Steam locomotive. This option creates a steam locomotive animation on the terminal.")
	print("15. Turtle race. Each turtle will race to the finish line, and scores will be displayed after each race.")
	print("16. Sudoku. You has the option to play normally. If you cannot finish the puzzle, artificial intelligence will finish it for you.")
	print("17. Play tetris. Press Ctrl + C to quit the game at any time.")
	print("")

def send_noti():

	x = str(input("What is the subject of your notification? "))
	y = str(input("What is the body of your notification? Entering \"none\" will result in only the subject being printed: "))
	time.sleep(2)
	print("")

	#Prepares the notification 
	
	spinning_cursor("Formatting: ")
	time.sleep(2)
	if (len(x)+len(y)) > 40:
		progress_bar("Creating Notification", 0.05, random.randint(40, ((len(x))+(len(y)))), False)
	elif not (len(x)+len(y)) > 40:
		progress_bar("Creating Notification", 0.05, random.randint(40, 100), False) 
	
	#Command to execute the notification. Clears terminal afterwards
	
	if y == "none":
		string = "notify-send {sub} {text}".format(sub=x, text="")
	elif not y == "none":
		string = "notify-send {sub} {text}".format(sub=x, text=y)
	os.system(string)
	os.system("clear")

def browse_web():

	#Prepares website, asks for user input
	
	website = str(input("Enter the URL of your desired website. Entering \"default\" will direct you to Google: "))
	time.sleep(0.5)
	print("")
	progress_bar("Redirecting", 0.0001, random.randint(10000, 20000), False)
	time.sleep(1)
	print("")
	progress_bar("Entering domain", 0.0005, random.randint(10000, 20000), False)
	time.sleep(1)
	print("")
	
	#Provides rules, then directs to website using w3m command. 
	
	print("Website loaded. Please read the following rules. Press enter to continue to your site. ")
	print("")
	print("\t 1. Press Q + Y to exit.")
	print("\t 2. This is currently in development and is constantly being updated.")
	print("\t 3. Currently, videos cannot be played. However, all other functions are working!")
	print("\t 4. Use the arrow keys to navigate the UI.")
	print("\t 5. After you have exited the terminal, press Ctrl + L to clear your terminal.")
	x = str(input())
	if (x == ""):
		if website == "default":
			os.system("w3m www.google.com")
		elif not website == "default":
			os.system("w3m {web}".format(web=website))

def echo_statement():

	#Simple echo statement to reverb user input into the terminal. 
	statement = str(input("Enter the statement you would like to echo: "))
	spinning_cursor("Echoing statement: ")
	os.system("clear")
	os.system("echo {statement}".format(statement=statement))

def update_system():

	#Utilitarian upgrade of system. User has choice to upgrade applications as well. 
	
	upgradeornot = str(input("Are you sure you would like to perform a full system upgrade? [Y/N] "))
	appupgrade = str(input("Would you like to upgrade your applications as well? [Y/N] "))
	print("")
	if (appupgrade == "N" and upgradeornot == "N") or (appupgrade == "n" and upgradeornot == "N") or (appupgrade == "N" and upgradeornot == "n") or (appupgrade == "n" and upgradeornot == "n"):
		confirmation = str(input("Are you sure you wouldn't like to upgrade? [Y/N] "))
		if (confirmation == "Y") or (confirmation == "y"):
			print("\nPlease run the program again to select another option.")
		elif (confirmation == "N") or (confirmation == "n"):
			pass
	elif (appupgrade == "N" and upgradeornot == "y") or (appupgrade == "n" and upgradeornot == "Y") or (appupgrade == "N" and upgradeornot == "Y") or (appupgrade == "n" and upgradeornot == "y"):
		os.system("sudo apt-get update")
		print("\nPartial system upgrade successful.")
	elif (appupgrade == "Y" and upgradeornot == "Y") or (appupgrade == "y" and upgradeornot == "Y") or (appupgrade == "Y" and upgradeornot == "y") or (appupgrade == "y" and upgradeornot == "y"):
		os.system("sudo apt-get upgrade")
		print("\nFull system upgrade successful.")
	elif (appupgrade == "Y" and upgradeornot == "N") or (appupgrade == "y" and upgradeornot == "N") or (appupgrade == "Y" and upgradeornot == "n") or (appupgrade == "y" and upgradeornot == "n"):
		while (appupgrade == "Y" and upgradeornot == "N") or (appupgrade == "y" and upgradeornot == "N") or (appupgrade == "Y" and upgradeornot == "n") or (appupgrade == "y" and upgradeornot == "n"):
			print("This is not a feasible option. You must perform a system upgrade to upgrade applications. Please run the program again to select another option.")
			print("")
			upgradeornot = str(input("Are you sure you would like to perform a full system upgrade? [Y/N] "))
			appupgrade = str(input("Would you like to upgrade your applications as well? [Y/N] "))
			print("")
			if (appupgrade == "N" and upgradeornot == "N") or (appupgrade == "n" and upgradeornot == "N") or (appupgrade == "N" and upgradeornot == "n") or (appupgrade == "n" and upgradeornot == "n"):
				confirmation = str(input("Are you sure you wouldn't like to upgrade? [Y/N] "))
				if (confirmation == "Y") or (confirmation == "y"):
					print("\nPlease run the program again to select another option.")
				elif (confirmation == "N") or (confirmation == "n"):
					pass
			elif (appupgrade == "N" and upgradeornot == "y") or (appupgrade == "n" and upgradeornot == "Y") or (appupgrade == "N" and upgradeornot == "Y") or (appupgrade == "n" and upgradeornot == "y"):
				os.system("sudo apt-get update")
				print("\nPartial system upgrade successful.")
			elif (appupgrade == "Y" and upgradeornot == "Y") or (appupgrade == "y" and upgradeornot == "Y") or (appupgrade == "Y" and upgradeornot == "y") or (appupgrade == "y" and upgradeornot == "y"):
				os.system("sudo apt-get upgrade")
				print("\nFull system upgrade successful.")
	print("")

def ping_websites():

	website = input("Type the URL for website you would like to ping (entering default will ping Google): ")
	ping_count = input("How many times would you like to ping this website? Enter \"U\" for unlimited pings: ")
	print("")
	if website == "default":
		website == "www.google.com"
	elif not website == "default":
		pass
	if not ping_count == "U":
		os.system("ping {website} -c {count}".format(website=website, count=ping_count))
	elif ping_count == "U" or ping_count == "u":
		x = str(input("Pinging a website an unlimited amount of times will result in an infinite loop. To exit this loop and return to base terminal, press Ctrl + C. Press enter to confirm this message and begin your pings. "))
		if (x == ""):
			print("")
			progress_bar("Generating pings ", 0.05, 100, False)
			print("")
			os.system("ping {website}".format(website=website))
	print("")
	redo = str(input("Would you like to ping another website? [Y/N] "))
	while redo == "Y" or redo == "y" or redo == "":
		website = input("Type the URL for website you would like to ping: ")
		ping_count = input("How many times would you like to ping this website? Enter \"U\" for unlimited pings: ")
		print("")
		if not ping_count == "U" and not ping_count == "u":
			os.system("ping {website} -c {count}".format(website=website, count=ping_count))
		elif ping_count == "U":
			x = str(input("Pinging a website an unlimited amount of times will result in an infinite loop. To exit this loop and return to base terminal, press Ctrl + C. Press enter to confirm this message and begin your pings. "))
			if (x == ""):
				print("")
				progress_bar("Generating pings ", 0.05, 100, False)
				print("")
				os.system("ping {website}".format(website=website))
		print("")
		redo == str(input("Would you like to ping another website? [Y/N] "))
	if redo == "n" or redo == "N":
		print("")
		print("Thanks for pinging a website!")
		print("")

def search_term():

	dictionary = PyDictionary()
	print("")
	word = str(input("Enter the word you would like to search: "))
	print("")
	returnlabel = str(input("Enter whether you would like a definition, synonyms, or antonyms (D, S, or A): "))
	if returnlabel == "D":
		try:
			returnans = "{word}- {definition}".format(word=word, definition=dictionary.meaning(word))
			try:
				print("")
				print("The definition of {word} is: ".format(word=word))
				print("")
				print(returnans)
			except IndexError as error:
				print("This word was not found in our dictionary. However, we are still expanding our vocabulary. Hopefully we can understand your search term one day!")
		except IndexError as error:
			print("This word was not found in our dictionary. However, we are still expanding our vocabulary. Hopefully we can understand your search term one day!")
	elif returnlabel == "S":
		try:
			returnans = "{word}- {synonyms}".format(word=word, synonyms=dictionary.synonym(word))
			try:
				print("")
				print("The synonyms of {word} are: ".format(word=word))
				print("")
				print("")
				print(returnans)
			except IndexError as error:
				print("We could not find any synonyms for this word. Sorry!")
		except IndexError as error:
			print("We could not find any synonyms for this word. Sorry!")
	elif returnlabel == "A":
		try: 
			returnans = "{word}- {antonyms}".format(word=word, antonyms=dictionary.antonym(word))
			try:
				print("")
				print("The antonyms of {word} are: ".format(word=word))
				print("")
				print("")
				print(returnans)
			except IndexError as error:
				print("We could not find any antonyms for this word. Sorry!")
		except IndexError as error:
			print("We could not find any antonyms for this word. Sorry!")
	else:
		print("This is not a valid option! Sorry!")

	redo = str(input("Would you like to search another word? [Y/N] "))
	while redo == "y" or redo == "Y" or redo == "":
		word = str(input("Enter the word you would like to search: "))
		print("")
		returnlabel = str(input("Enter whether you would like a definition, synonyms, or antonyms (D, S, or A): "))
		if returnlabel == "D":
			try:
				returnans = "{word}- {definition}".format(word=word, definition=dictionary.meaning(word))
				try:
					print("")
					print("The definition of {word} is: ".format(word=word))
					print("")
					print(returnans)
					print("")
					redo = str(input("Would you like to search another word? [Y/N] "))
				except IndexError as error:
					print("This word was not found in our dictionary. However, we are still expanding our vocabulary. Hopefully we can understand your search term one day!")
			except IndexError as error:
				print("This word was not found in our dictionary. However, we are still expanding our vocabulary. Hopefully we can understand your search term one day!")
		elif returnlabel == "S":
			try:
				returnans = "{word}- {synonyms}".format(word=word, synonyms=dictionary.synonym(word))
				try:
					print("")
					print("The synonyms of {word} are: ".format(word=word))
					print("")
					print("")
					print(returnans)
					print("")
					redo = str(input("Would you like to search another word? [Y/N] "))
				except IndexError as error:
					print("We could not find any synonyms for this word. Sorry!")
			except IndexError as error:
				print("We could not find any synonyms for this word. Sorry!")
		elif returnlabel == "A":
			try: 
				returnans = "{word}- {antonyms}".format(word=word, antonyms=dictionary.antonym(word))
				try:
					print("")
					print("The antonyms of {word} are: ".format(word=word))
					print("")
					print("")
					print(returnans)
					print("")
					redo = str(input("Would you like to search another word? [Y/N] "))
				except IndexError as error:
					print("We could not find any antonyms for this word. Sorry!")
			except IndexError as error:
				print("We could not find any antonyms for this word. Sorry!")
		else:
			print("This is not a valid option! Sorry!")
	if redo == "N" or "n":
		print("")
		print("Thanks for picking this option!")
		print("")
	print("")

def steam_loco():
	progress_bar("Creating train:", 0.1, 20, False)
	os.system("sl")
	os.system("clear")
	redo = str(input("Would you like to run another steam locomotive? [Y/N] "))
	while redo == "Y" or redo == "y" or redo == "":
		progress_bar("Creating train:", 0.1, 20, False)
		os.system("sl")
		os.system("clear")
		redo = str(input("Would you like to run another steam locomotive? [Y/N] "))

def view_files():

	print("")
	progress_bar("Accessing files:", 0.005, 100, False)
	print("")
	print("Files have been accessed. Read the following rules and then press enter to access your files.")
	print("")
	print("\t1. You can navigate the user interface using arrow keys.")
	print("\t2. Press the back arrow to go back a folder and the forward arrow to navigate the next folder.")
	print("\t3. Pressing enter will open a file.")
	print("\t4. Press \"q\" to quit the file navigator at any time.")
	x = str(input(""))
	if (x == ""):
		time.sleep(0.05)
		os.system("nnn")
		os.system("clear")

def open_app():

	print("")
	print("Format: app1 & app2 & app3")
	print("")
	app = str(input("What application would you like to open? (view the format above to open multiple applications at once): "))
	print("")
	time.sleep(0.5)
	os.system("{application}".format(application=app))
	os.system("clear")
	redo = str(input("Would you like to open another application? [Y/N] "))
	print("")
	while redo == "Y" or redo == "y" or redo == "":
		app = str(input("What application would you like to open? (all lowercase) "))
		print("")
		print("To open another application, press Ctrl + C.")
		time.sleep(0.5)
		os.system("{application}".format(application=app))
		keyboard.press(Key.ctrl)
		keyboard.press('c')
		keyboard.release('c')
		keyboard.release(Key.ctrl)
		os.system("clear")
		redo = str(input("Would you like to open another application? [Y/N] "))
		print("")

def view_stock_market():

	#Provides real-time data from the stock market. 

	x = str(input("Enter whether you would like a specific stock ticker, overall market summary, or historical market data for one stock (SST, OMS, HMD): "))
	if x == "SST" or x == "sst":
		stock = str(input("Enter the stock ticker (or multiple stock tickers, each separated with commas with no spaces in between): "))
		print("")
		print("Generating ticker... ")
		print("")
		time.sleep(0.2)
		os.system("curl https://terminal-stocks.herokuapp.com/{stock}".format(stock=stock.upper()))
		redo = str(input("Would you like to look for another stock ticker? [Y/N] "))
		print("")
		while redo == "Y" or redo == "y" or redo == "":
			stock = str(input("Enter the stock ticker (or multiple stock tickers, each separated with commas with no spaces in between): "))
			print("")
			print("Generating ticker... ")
			print("")
			time.sleep(0.2)
			os.system("curl https://terminal-stocks.herokuapp.com/{stock}".format(stock=stock.upper()))
			redo = str(input("Would you like to look for another stock ticker? [Y/N] "))
			print("")
		if not redo == "Y" and not redo == "y" and not redo == "":
			print("")
			print("Thanks for using stock market ticker generator!")
	elif x == "OMS" or x == "oms":
		print("")
		print("Gathering overall market data... ")
		print("")
		time.sleep(2)
		os.system("curl https://terminal-stocks.herokuapp.com/market-summary")
		print("")
		redo = str(input("Would you like to look for more stock market information? [Y/N]"))
		while redo == "y" or redo == "Y" or redo == "":
			print("")
			x = str(input("Enter whether you would like a specific stock ticker, overall market summary, or historical market data for one stock (SST, OMS, HMD): "))
			if x == "SST" or x == "sst":
				stock = str(input("Enter the stock ticker (or multiple stock tickers, each separated with commas with no spaces in between): "))
				print("")
				print("Generating ticker... ")
				print("")
				time.sleep(0.2)
				os.system("curl https://terminal-stocks.herokuapp.com/{stock}".format(stock=stock.upper()))
				redo = str(input("Would you like to look for another stock ticker? [Y/N] "))
				print("")
				while redo == "Y" or redo == "y" or redo == "":
					stock = str(input("Enter the stock ticker (or multiple stock tickers, each separated with commas with no spaces in between): "))
					print("")
					print("Generating ticker... ")
					print("")
					time.sleep(0.2)
					os.system("curl https://terminal-stocks.herokuapp.com/{stock}".format(stock=stock.upper()))
					redo = str(input("Would you like to look for another stock ticker? [Y/N] "))
					print("")
				if not redo == "Y" and not redo == "y" and not redo == "":
					print("")
					print("Thanks for using stock market ticker generator!")
			elif x == "OMS" or x == "oms":
				print("")
				print("Gathering overall market data... ")
				print("")
				time.sleep(2)
				os.system("curl https://terminal-stocks.herokuapp.com/market-summary")
				print("")
				redo = str(input("Would you like to look for more stock market information? [Y/N]"))
			elif x == "HMD" or x == "hmd":
				print("")
				os.system("clear")
				stock = str(input("Enter the stock ticker for any one stock: "))
				print("")
				print("Generating ticker for {stock}... ".format(stock=stock.upper()))
				print("")
				time.sleep(5)
				print("Page 1 of Historical Data for {stock}: ".format(stock=stock.upper()))
				os.system("curl https://terminal-stocks.herokuapp.com/historical/{stock}".format(stock=stock.upper()))
				time.sleep(7.5)
				print("Page 2 of Historical Data for {stock}: ".format(stock=stock.upper()))
				os.system("curl https://terminal-stocks.herokuapp.com/historical/{stock}?page=2".format(stock=stock.upper()))
				time.sleep(7.5)
				print("Page 3 of Historical Data for {stock}: ".format(stock=stock.upper()))
				os.system("curl https://terminal-stocks.herokuapp.com/historical/{stock}?page=3".format(stock=stock.upper()))
				redo = str(input("Would you like to look for another stock ticker? [Y/N] "))
				print("")
				while redo == "Y" or redo == "y" or redo == "":
					print("")
					os.system("clear")
					stock = str(input("Enter the stock ticker for any one stock: "))
					print("")
					print("Generating ticker for {stock}... ".format(stock=stock.upper()))
					print("")
					time.sleep(5)
					print("Page 1 of Historical Data for {stock}: ".format(stock=stock.upper()))
					os.system("curl https://terminal-stocks.herokuapp.com/historical/{stock}".format(stock=stock.upper()))
					time.sleep(7.5)
					print("")
					print("Page 2 of Historical Data for {stock}: ".format(stock=stock.upper()))
					os.system("curl https://terminal-stocks.herokuapp.com/historical/{stock}?page=2".format(stock=stock.upper()))
					time.sleep(7.5)
					print("")
					print("Page 3 of Historical Data for {stock}: ".format(stock=stock.upper()))
					os.system("curl https://terminal-stocks.herokuapp.com/historical/{stock}?page=3".format(stock=stock.upper()))
					redo = str(input("Would you like to look for another stock ticker? [Y/N] "))
					print("")
			else:
				while not x == "SST" or not x == "sst" or not x == "OMS" or not x == "oms" or not x == "HMD" or not x  == "hmd":
					print("This is not a valid option! Please read the prompt carefully before proceeding. ")
					print("")
					time.sleep(3)
					x = str(input("Enter whether you would like a specific stock ticker, overall market summary, or historical market data for one stock (SST, OMS, HMD): "))
					if x == "SST" or x == "sst":
						stock = str(input("Enter the stock ticker (or multiple stock tickers, each separated with commas with no spaces in between): "))
						print("")
						print("Generating ticker... ")
						print("")
						time.sleep(0.2)
						os.system("curl https://terminal-stocks.herokuapp.com/{stock}".format(stock=stock.upper()))
						redo = str(input("Would you like to look for another stock ticker? [Y/N] "))
						print("")
						while redo == "Y" or redo == "y" or redo == "":
							stock = str(input("Enter the stock ticker (or multiple stock tickers, each separated with commas with no spaces in between): "))
							print("")
							print("Generating ticker... ")
							print("")
							time.sleep(0.2)
							os.system("curl https://terminal-stocks.herokuapp.com/{stock}".format(stock=stock.upper()))
							redo = str(input("Would you like to look for another stock ticker? [Y/N] "))
							print("")
						if not redo == "Y" and not redo == "y" and not redo == "":
							print("")
							print("Thanks for using stock market ticker generator!")
					elif x == "OMS" or x == "oms":
						print("")
						print("Gathering overall market data... ")
						print("")
						time.sleep(2)
						os.system("curl https://terminal-stocks.herokuapp.com/market-summary")
						print("")
					elif x == "HMD" or x == "hmd":
						print("")
						os.system("clear")
						stock = str(input("Enter the stock ticker for any one stock: "))
						print("")
						print("Generating ticker for {stock}... ".format(stock=stock.upper()))
						print("")
						time.sleep(5)
						print("Page 1 of Historical Data for {stock}: ".format(stock=stock.upper()))
						os.system("curl https://terminal-stocks.herokuapp.com/historical/{stock}".format(stock=stock.upper()))
						time.sleep(7.5)
						print("")
						print("Page 2 of Historical Data for {stock}: ".format(stock=stock.upper()))
						os.system("curl https://terminal-stocks.herokuapp.com/historical/{stock}?page=2".format(stock=stock.upper()))
						time.sleep(7.5)
						print("")
						print("Page 3 of Historical Data for {stock}: ".format(stock=stock.upper()))
						os.system("curl https://terminal-stocks.herokuapp.com/historical/{stock}?page=3".format(stock=stock.upper()))
						redo = str(input("Would you like to look for another stock ticker? [Y/N] "))
						print("")
						while redo == "Y" or redo == "y" or redo == "":
							print("")
							os.system("clear")
							stock = str(input("Enter the stock ticker for any one stock: "))
							print("")
							print("Generating ticker for {stock}... ".format(stock=stock.upper()))
							print("")
							time.sleep(5)
							print("Page 1 of Historical Data for {stock}: ".format(stock=stock.upper()))
							os.system("curl https://terminal-stocks.herokuapp.com/historical/{stock}".format(stock=stock.upper()))
							time.sleep(7.5)
							print("Page 2 of Historical Data for {stock}: ".format(stock=stock.upper()))
							os.system("curl https://terminal-stocks.herokuapp.com/historical/{stock}?page=2".format(stock=stock.upper()))
							time.sleep(7.5)
							print("Page 3 of Historical Data for {stock}: ".format(stock=stock.upper()))
							os.system("curl https://terminal-stocks.herokuapp.com/historical/{stock}?page=3".format(stock=stock.upper()))
							redo = str(input("Would you like to look for another stock ticker? [Y/N] "))
							print("")
	elif x == "HMD" or x == "hmd":
		print("")
		os.system("clear")
		stock = str(input("Enter the stock ticker for any one stock: "))
		print("")
		print("Generating ticker for {stock}... ".format(stock=stock.upper()))
		print("")
		time.sleep(5)
		print("Page 1 of Historical Data for {stock}: ".format(stock=stock.upper()))
		os.system("curl https://terminal-stocks.herokuapp.com/historical/{stock}".format(stock=stock.upper()))
		time.sleep(7.5)
		print("Page 2 of Historical Data for {stock}: ".format(stock=stock.upper()))
		os.system("curl https://terminal-stocks.herokuapp.com/historical/{stock}?page=2".format(stock=stock.upper()))
		time.sleep(7.5)
		print("Page 3 of Historical Data for {stock}: ".format(stock=stock.upper()))
		os.system("curl https://terminal-stocks.herokuapp.com/historical/{stock}?page=3".format(stock=stock.upper()))
		redo = str(input("Would you like to look for another stock ticker? [Y/N] "))
		print("")
		while redo == "Y" or redo == "y" or redo == "":
			print("")
			os.system("clear")
			stock = str(input("Enter the stock ticker for any one stock: "))
			print("")
			print("Generating ticker for {stock}... ".format(stock=stock.upper()))
			print("")
			time.sleep(5)
			print("Page 1 of Historical Data for {stock}: ".format(stock=stock.upper()))
			os.system("curl https://terminal-stocks.herokuapp.com/historical/{stock}".format(stock=stock.upper()))
			time.sleep(7.5)
			print("Page 2 of Historical Data for {stock}: ".format(stock=stock.upper()))
			os.system("curl https://terminal-stocks.herokuapp.com/historical/{stock}?page=2".format(stock=stock.upper()))
			time.sleep(7.5)
			print("Page 3 of Historical Data for {stock}: ".format(stock=stock.upper()))
			os.system("curl https://terminal-stocks.herokuapp.com/historical/{stock}?page=3".format(stock=stock.upper()))
			redo = str(input("Would you like to look for another stock ticker? [Y/N] "))
			print("")
		if redo == "n" or redo == "N":
			print("")
			print("Thanks for using stock market summary!")
			time.sleep(5)
			os.system("clear")
	else:
		if not x == "SST" or not x == "sst" or not x == "OMS" or not x == "oms" or not x == "HMD" or not x  == "hmd":
			print("")
			print("This is not a valid option! Please read the prompt carefully before proceeding. ")
			print("")
			print("Please run the program again if you would like and select a valid option.")
			print("")
			time.sleep(2)

def turtle_race():

	"""
	##################################################################

	This entire piece of code is the property of TechWithTim. I have no rights claimed to
	this code. All credit for this code is directed to Tim Ruscica. 

	This code is not covered by any validated license. Again, I claim no credit for this code- 
	all credit is directed to Tim Ruscica from TechWithTim. 

	I have only made some minor edits to this code for my purposes.

	-Sanchit

	##################################################################
	"""

	import math
	import random
	import turtle
	import time

	win_length = 500
	win_height = 500

	turtles = 8

	turtle.screensize(win_length, win_height)


	class racer(object):
	    def __init__(self, color, pos):
	        self.pos = pos
	        self.color = color
	        self.turt = turtle.Turtle()
	        self.turt.shape('turtle')
	        self.turt.color(color)
	        self.turt.penup()
	        self.turt.setpos(pos)
	        self.turt.setheading(90)

	    def move(self):
	        r = random.randrange(1, 20)
	        self.pos = (self.pos[0], self.pos[1] + r)
	        self.turt.pendown()
	        self.turt.forward(r)

	    def reset(self):
	        self.turt.penup()
	        self.turt.setpos(self.pos)


	def setupFile(name, colors):
	    file = open(name, 'w')
	    for color in colors:
	        file.write(color + ' 0 \n')
	    file.close()


	def startGame():
	    tList = []
	    turtle.clearscreen()
	    turtle.hideturtle()
	    colors = ["red", "green", "blue", 'yellow', 'pink', 'orange', 'purple', 'black', 'grey']
	    start = -(win_length/2) + 20
	    for t in range(turtles):
	        newPosX = start + t*(win_length)//turtles
	        tList.append(racer(colors[t],(newPosX, -230)))
	        tList[t].turt.showturtle()

	    run = True
	    while run:
	        for t in tList:
	            t.move()

	        maxColor = []
	        maxDis = 0
	        for t in tList:
	            if t.pos[1] > 230 and t.pos[1] > maxDis:
	                maxDis = t.pos[1]
	                maxColor = []
	                maxColor.append(t.color)
	            elif t.pos[1] > 230 and t.pos[1] == maxDis:
	                maxDis = t.pos[1]
	                maxColor.append(t.color)

	        if len(maxColor) > 0:
	            run = False
	            print('The winner is: ')
	            for win in maxColor:
	                print(win)

	    oldScore = []
	    file = open('scores.txt', 'r')
	    for line in file:
	        l = line.split()
	        color = l[0]
	        score = l[1]
	        oldScore.append([color, score])

	    file.close()

	    file = open('scores.txt', 'w')

	    for entry in oldScore:
	        for winner in maxColor:
	            if entry[0] == winner:
	                entry[1] = int(entry[1]) + 1

	        file.write(str(entry[0]) + ' ' + str(entry[1]) + '\n')

	    file.close()

	#The following code is unique code, and has no claims to it.

	confirmation = str(input("Are you sure you would like to start the turtle race? [Y/N] "))
	if confirmation == "Y" or confirmation == "y" or confirmation == "":
		print("")
		print("Starting race. Hold tight!")
		time.sleep(2)
		startGame()
		time.sleep(3)
		print('-----------------------------------')
		start = input('Would you like to play again? [Y/N] ')
		if start == "N" or start == "n":
			print("")
			exit = str(input("Thanks for playing! Press enter to clear the terminal and move on."))
			if exit == "":
				os.system("clear")
		while start == "y" or start == "Y" or start == "":
		    startGame()
		    print('-----------------------------------')
		    start = input('Would you like to play again? [Y/N] ')
	else:
		print("Sorry to see you go! Run ./terminal-simplifier again to select a different option.")

def play_sudoku():

	#Plays sudoku using noduku 2.1.0 software. 

	print("")
	confirmation = str(input("Are you sure you want to play sudoku? [Y/N] "))
	if confirmation == "y" or confirmation == "Y" or confirmation == "":
		print("")
		progress_bar("Generating sodoku puzzle ", 0.05, 7, False)
		print("")
		time.sleep(0.5)
		os.system("nudoku")
		print("")
		redo = str(input("Would you like to play again? [Y/N] "))
		print("")
		while redo == "Y" or redo == "y" or redo == "":
			print("")
			print("")
			progress_bar("Generating sodoku puzzle ", 0.05, 7, False)
			print("")
			time.sleep(0.5)
			os.system("nudoku")
			print("")
			redo = str(input("Would you like to play again? [Y/N] "))
			print("")
		if redo == "N" or redo == "n":
			print("")
			print("Thanks for playing sudoku!")
	elif confirmation == "N" or confirmation == "n":
		print("")
		print("Thanks for considering sudoku!")
		print("")
		time.sleep(0.5)

def play_tetris():

	print("")
	confirmation = str(input("Are you sure you want to play tetris? [Y/N] "))
	print("")
	if confirmation == "Y" or confirmation == "y" or confirmation == "":
		print("")
		time.sleep(0.5)
		print("Launching tetris shortly. Press Ctrl + C to quit tetris at any time. ")
		time.sleep(3)
		spinning_cursor("Launching... ")
		os.system("clear")
		os.system("bastet")
		os.system("clear")
		redo = str(input("Would you like to play again? [Y/N] "))
		while redo == "Y" or redo == "y" or redo == "":
			print("")
			time.sleep(0.5)
			print("Launching tetris shortly. Press Ctrl + C to quit tetris at any time. ")
			time.sleep(3)
			spinning_cursor("Launching... ")
			os.system("clear")
			os.system("bastet")
			os.system("clear")
		if redo == "N" or redo == "n":
			print("")
			print("Thanks for considering tetris!")
			print("")
			time.sleep(2)
			os.system("clear")
	elif confirmation == "N" or confirmation == "n":
		print("")
		print("Thanks for considering tetris!")
		print("")
		time.sleep(2)
		os.system("clear")

def view_memory_info():

	confirmation = str(input("Are you sure you would like to view memory info? [Y/N] " ))
	if confirmation == "Y" or confirmation == "y" or confirmation == "":
		os.system("clear")
		spinning_cursor("Launching memory info... ")
		print("")
		time.sleep(0.5)
		os.system("clear")
		os.system("free -m")
		print("")
		print("Thanks for using memory viewer!")
		print("")
	elif confirmation == "N" or confirmation == "n":
		print("")
		print("Thanks for considering memory viewer!")
		print("")
		time.sleep(0.5)

def view_disk_info():

	confirmation = str(input("Are you sure you would like to view disk info? [Y/N] "))
	if confirmation == "Y" or confirmation == "y" or confirmation == "":
		os.system("clear")
		spinning_cursor("Launching disk info... ")
		print("")
		time.sleep(0.5)
		os.system("clear")
		os.system("pydf")
		print("Thanks for viewing disk info!")
		print("")
	else:
		print("")
		print("Thanks for considering vieweing disk info!")
		print("")
		time.sleep(0.5)

def view_processor_info():

	print("")	
	confirmation = str(input("Are you sure you would like to view processor info? [Y/N] "))
	if confirmation == "Y" or confirmation == "y" or confirmation == "":
		print("")
		spinning_cursor("Launching processor info... ")
		print("")
		time.sleep(0.5)
		os.system("clear")
		os.system("lscpu")
		print("")
		print("Thanks for viewing processor info!")
		print("")
	else:
		print("")
		print("Thanks for considering viewing processor info!")
		print("")
		time.sleep(0.5)

def view_hardware_info():

	print("")
	confirmation = str(input("Are you sure you would like to view hardware info info? [Y/N] "))
	if confirmation == "Y" or confirmation == "y" or confirmation == "":
		print("")
		spinning_cursor("Launching overall hardware info... ")
		print("")
		time.sleep(0.5)
		os.system("clear")
		os.system("hwinfo --short")
		print("")
	else:
		print("")
		print("Thanks for considering viewing overall hardware info!")
		print("")
		time.sleep(0.5)
