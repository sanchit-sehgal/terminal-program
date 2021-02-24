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

import os
import subprocess
import pyautogui
import time 
from spinningcursor import spinning_cursor
from spinningcursor import progress_bar
from new_options import *

os.system("clear")
print("Thanks for using Terminal Simplifier! I hope you can find this as useful as I do.")
time.sleep(3)

def new_query():
	os.system("clear")
	print_options()
	print("")
	action = int(input("Enter the corresponding number for the action you would like to run: "))
	print("")
	if action == 1:
		send_noti()
	elif action == 2:
		browse_web()
	elif action == 3:
		echo_statement()
	elif action == 4:
		update_system()
	elif action == 5:
		ping_websites()
	elif action == 6:
		search_term()
	elif action == 7:
		view_files()
	elif action == 8:
		open_app()
	elif action == 9:
		view_stock_market()
	elif action == 10:
		view_memory_info()
	elif action == 11:
		view_disk_info()
	elif action == 12:
		view_processor_info()
	elif action == 13:
		view_hardware_info()
	elif action == 14:
		steam_loco()
	elif action == 15:
		turtle_race()
	elif action == 16:
		play_sudoku()
	elif action == 17:
		play_tetris()
	elif not (type(action) == int) or not 1<=action<=17:
		print("Not a valid option!")
		print("")

def rerun_prog(): 
	x = str(input("If you would like to run the program again, press Y. If not, press N: "))
	if x == "Y" or x == "y" or x == "":
		return True
	else:
		print("")
		print("Thanks for running the program. If you would like to run it again separately, type \"python runner.py\" in your terminal! Your terminal will be cleared and will close automatically.")
		time.sleep(3)
		os.system("clear")
		return False

new_query()
while rerun_prog() == True:
	new_query()
