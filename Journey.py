#! /usr/bin/env python3 # coding: UTF-8 

# 
logo =    """
       _   __            __    ___         __  
   / | / /___  ____ _/ /_  /   |  _____/ /__
  /  |/ / __ \/ __ `/ __ \/ /| | / ___/ //_/
 / /|  / /_/ / /_/ / / / / ___ |/ /  / ,<   
/_/ |_/\____/\__,_/_/ /_/_/  |_/_/  /_/|_|  
                                        By: @KMx404 

"""

# I need to work on a better intro 
intro = """
   Welcome to NoahArk! 
   To get the full cover of this game check the story side. 
   Are you ready to play ? 

"""


print(logo)
print(intro)
from Puzzle import ask1 
from Puzzle import ask2 
from Puzzle import main
import os 
os.system('python Puzzle.py')


# i guess there is a problem passing a parameter 



