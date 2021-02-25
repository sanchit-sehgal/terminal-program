import sys
import time
from tqdm import tqdm
import random

def spinning_cursor(string):
    
    for cursor in '\\|/-\\|/-\\|/-\\|/-\\|/':
      time.sleep(0.1)
      # Use '\r' to move cursor back to line beginning
      # Or use '\b' to erase the last character
      sys.stdout.write('\r{}{}'.format(string, cursor))
      # Force Python to write data into terminal.
      sys.stdout.flush()

def progress_bar(string, inti, totalsize, boolearn):
  for i in tqdm(range(totalsize), ascii=boolearn, desc=string):
    time.sleep(inti)