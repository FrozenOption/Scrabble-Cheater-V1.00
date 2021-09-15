#Scrabble Cheater V1.00
#Written by: FrozenOption

import requests
import re

LINK = "https://lettersolver.com"
found = False

def find_number_of_words():
	try:
		number_of_words = re.search(f'[0-9][0-9] Words for {letters}', response.text).group()
		print("\n->->->->->->->->->->->")
		print(number_of_words.upper() + " :")
		print("->->->->->->->->->->-> \n")
		found = True

	except:
		print("NO RESULT FOUND!!")
		found = False

def display_words():
	count = 1
	if not found:
		words = list()
		words = re.findall('(?<=data-word=\').*(?=\'>)', response.text)
		c = [len(i) for i in words]
		for x in range(max(c),min(c)-1,-1):
			set=[]
			if not c.count(x): continue
			print(f"\n{x} Letter Words: {c.count(x)}")
			for word in words:
				if len(word)==x:
					set.append(word)
			print(' | '.join(set))

while True:

	letters = input("Write your letters : ").strip()
	if not letters:
		print("Good luck!")
		break

	response = requests.get(LINK + f"/words-for/{letters}/?dictionary=all_en")
	response.encoding = 'utf-8'

	find_number_of_words()
	display_words()
	print("\n")
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

