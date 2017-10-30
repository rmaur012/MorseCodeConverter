import re


def findLetter(str, currList):

	#When len(str) = 0, then we have to check to see if the current list is simply "None" or 
	#actually has a letter at index [1]
	if len(str) == 0:

		#If the current list only has "None" then return "_" since there are no sub-lists to enter if 
		if currList[0] == None:
			return "_"
		else:
			return currList[1]

	#If len(currList) = 1, that means it is a list with "None" as the value.
	#Since there are no more sub-lists to enter to look for a value, simply return a "|"
	if len(currList) == 1:
		return "|"

	#dashOrDot holds the next "-" or "." in the sequence.
	dashOrDot = str[0]

	#rest holds the rest of the sequence to then be passed down recursively.
	rest = str[1:]

	#If dashOrDot is a dash, pass the rest of the sequence and go to the left sub-list, which is currList[0]
	if dashOrDot == "-":
		return findLetter(rest, currList[0])

	#If dashOrDot is a dot, pass the rest of the sequence and go to the lright sub-list, which is currList[2]
	elif dashOrDot == ".":
		return findLetter(rest, currList[2])


def findMorse(character, currList):

	#If len(currList) = 1, that means it is a list with "None" as the value.
	#Since there are no more sub-lists to enter to look for a value, simply return a "|"	
	if len(currList) == 1:
		return "|"

	#midList holds both a character and the morse code representation of that character
	midList = currList[1]

	#If midList is "None" or a list with "None" then return "~" since there is no more lists to look through
	if midList is None or midList[0] is None:
		return "~"

	#Get the letter in midList for comparison
	letter = midList[0]

	#If letter is the character we are looking for, return the morse code of that character
	if character == letter:
		return midList[1]
	
	#If character is less when compared to letter, go to the left sub-list and keep searching
	elif character < letter:
		return findMorse(character, currList[0])

	#else character must be more when compared to letter, so go to the right sub-list and keep searching
	else:
		return findMorse(character, currList[2])


#The data structure for both indexMorse and indexLetters are slight variants of the following:
#  A binary tree via lists of Lists: [[...],data,[...]]
#  The left and right sub-lists are also lists of lists. The middle list is the list that will hold the data.
#  At the end of the lists of lists, a list simply holding "None" indicating the end of the lists of lists


#indexMorse data structure variant: [[...],character string,[...]]
#  Tree is ordered via the morse code given to that character. If "." go right and if "-" go left on tree. 
#  When morse code sequence ends, the data of the node it landed on is the character that belongs to that morse code.
indexMorse = [[[[[[[None],"0",[None]],None,[[None],"9",[None]]],"O",[[None],".",[[None],"8",[[None],":",[None]]]]],"M",[[[None],"Q",[None]],"G",
	[[[[None],",",[None]],None,[None]],"Z",[[None],"7",[None]]]]],"T",[[[[None],"Y",[[[None],")",[None]],"(",[None]]],"K",[[[[None],"!",[None]],None,[[None],";",[None]]],"C",[None]]],"N",[[[None],"X",[[None],"/",[None]]],"D",[[[None],"=",[None]],"B",
[[[None],"-",[None]],"6",[None]]]]]]," ",[[[[[[None],"1",[[None],"'",[None]]],"J",[None]],"W",[[[None],None,[[None],"@",[None]]],"P",[None]]],"A",[[[None],None,[[[None],".",[None]],"+",[None]]],"R",[[None],"L",[[None],"&",[None]]]]],"E",
[[[[[None],"2",[None]],None,[[[None],"_",[None]],None,[[None],"?",[None]]]],"U",[[None],"F",[None]]],"I",[[[[None],"3",[None]],"V",[[None],None,[[[None],"$",[None]],None,[None]]]],"S",[[[None],"4",[None]],"H",
[[None],"5",[None]]]]]]]


#indexLetters data structure variant: [[...],[character string, morse code string],[...]]
#  Tree is ordered via comparison. so A is to the left of B since A<B. It is the same for all characters
#  Please note that at the end of each morse code sequence is A SINGLE SPACE. Keeps this in mind when working on the logic with spaces.
indexLetters = [[[[[[None],["!", "-.-.-- "],[[None],["$", "...-..- "],[None]]],["&", ".-... "],[[[None],["'", ".----. "],[None]],["(", "-.--. "],[[None],[")", "-.--.- "],[None]]]],["+", ".-.-. "],[[[None],[",", "--..-- "],[[None],["-", "-....- "],[None]]],[".", ".-.-.- "],[[[None],["/", "-..-. "],[None]],["0", "----- "],[[None],["1", ".---- "],[None]]]]],["2", "..--- "],[[[[None],["3", "...-- "],[[None],["4", "....- "],[None]]],["5", "..... "],[[[None],["6", "-.... "],[None]],["7", "--... "],[None]]],["8", "---.. "],[[[None],["9", "----. "],[[None],[":", "---... "],[None]]],[";", "-.-.-. "],[[[None],["=", "-...- "],[None]],["?", "..--.. "],[[None],["@", ".--.-. "],[None]]]]]],["A", ".- "],[[[[[None],["B", "-... "],[[None],["C", "-.-. "],[None]]],["D", "-.. "],[[[None],["E", ". "],[None]],["F", "..-. "],[None]]],["G", "--. "],[[[None],["H", ".... "],[[None],["I", ".. "],[None]]],["J", ".--- "],[[[None],["K", "-.- "],[None]],["L", ".-.. "],[[None],["M", "-- "],[None]]]]],["N", "-. "],[[[[[None],["O", "--- "],[None]],["P", ".--. "],[[None],["Q", "--.- "],[None]]],["R", ".-. "],[[[None],["S", "... "],[None]],["T", "- "],[None]]],["U", "..- "],[[[None],["V", "...- "],[[None],["W", ".-- "],[None]]],["X", "-..- "],[[[None],["Y", "-.-- "],[None]],["Z", "--.. "],[[None],["_", "..--.- "],[None]]]]]]]

#"main" method down below


#The loop keeps the application going until the user quits by entering "\q"
print("Enter '\q' to quit application")
while(True):
	message = input(">>>")

	if message == "\q":
		break

	newmssg = message.upper()

	isLetter = False
	#determines if message is to be put into morse code
	#"isLetter = True" means it is to be put into morse code
	#"isLetter = False" means that it is morse code that will be decoded


	#If newmssg contains an alphabetic character, isLetter it true
	if re.search('\w+',newmssg):
		isLetter = True
	
	#If these other values are found as first character, isLetter is true
	otherValues = ["@", "?", ",", ":", ";", "'", "+", "=", "_", "!", "(", ")", "$"]
	for i in otherValues:
		if message.count(i) !=0:
			isLetter = True

	#saver holds the string as the conversion builds
	saver = ""
	if isLetter == True:

		#wholemssg holds a list of all the words in the submitted message
		wholemssg = newmssg.split()
	#	print("wholemssg")
	#	print(wholemssg)
		for p in wholemssg:

			#splitmssg holds a list of letters in the word stored in the variable p
			splitmssg = list(p)
			print("splitmssg")
			print(splitmssg)

			#for each letter, find the morse code equivalent and add a space to set up for the next letter in the same word
			for i in splitmssg:
				saver = saver + (findMorse(i, indexLetters))

			#Add a space because in this program, 2 spaces signifiesthat the next morse code is part of the next word.
			saver = saver + " "
	else:

		#wholemssg holds a list of all the words in morse code (which should be separated by 2 spaces)
		wholemssg = re.split(r'\s{2}', newmssg)
	#	print(wholemssg)
		for i in wholemssg:

			#splitmssg holds a list of each morse code sequence that belongs to one character
			splitmssg = i.split(" ")
	#		print("Into splitmssg")
	#		print(splitmssg)
			for i in splitmssg:
	#			if(i != ""):
				saver = saver + (findLetter(i, indexMorse))
	#			else:
	#				saver = saver + " "
			saver = saver + " "

	#!$&'()+,-./0123456789:;=?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_

	print("Message Decoded: ")
	print(saver)
