import re


def findLetter(str, currList):
	if len(str) == 0:
		if currList[0] == None:
			return "_"
		else:
			return currList[1]

	if len(currList) == 1:
		return "|"

	letter = str[0]
	strSize = len(str)
	rest = str[1:]

	if letter == "-":
		return findLetter(rest, currList[0])
	elif letter == ".":
		return findLetter(rest, currList[2])


def findMorse(character, currList):

	if len(currList) == 1:
		return "|"

	midList = currList[1]

	if midList is None or midList[0] is None:
		return "~"

	letter = midList[0]

	if character == letter:
		if midList[0] is None:
			return "_"
		else:
			return midList[1]
	
	if character < letter:
		return findMorse(character, currList[0])
	else:
		return findMorse(character, currList[2])

indexMorse = [[[[[[[None],"0",[None]],None,[[None],"9",[None]]],"O",[[None],".",[[None],"8",[[None],":",[None]]]]],"M",[[[None],"Q",[None]],"G",
	[[[[None],",",[None]],None,[None]],"Z",[[None],"7",[None]]]]],"T",[[[[None],"Y",[[[None],")",[None]],"(",[None]]],"K",[[[[None],"!",[None]],None,[[None],";",[None]]],"C",[None]]],"N",[[[None],"X",[[None],"/",[None]]],"D",[[[None],"=",[None]],"B",
[[[None],"-",[None]],"6",[None]]]]]]," ",[[[[[[None],"1",[[None],"'",[None]]],"J",[None]],"W",[[[None],None,[[None],"@",[None]]],"P",[None]]],"A",[[[None],None,[[[None],".",[None]],"+",[None]]],"R",[[None],"L",[[None],"&",[None]]]]],"E",
[[[[[None],"2",[None]],None,[[[None],"_",[None]],None,[[None],"?",[None]]]],"U",[[None],"F",[None]]],"I",[[[[None],"3",[None]],"V",[[None],None,[[[None],"$",[None]],None,[None]]]],"S",[[[None],"4",[None]],"H",
[[None],"5",[None]]]]]]]

indexLetters = [[[[[[None],["!", "-.-.-- "],[[None],["$", "...-..- "],[None]]],["&", ".-... "],[[[None],["'", ".----. "],[None]],["(", "-.--. "],[[None],[")", "-.--.- "],[None]]]],["+", ".-.-. "],[[[None],[",", "--..-- "],[[None],["-", "-....- "],[None]]],[".", ".-.-.- "],[[[None],["/", "-..-. "],[None]],["0", "----- "],[[None],["1", ".---- "],[None]]]]],["2", "..--- "],[[[[None],["3", "...-- "],[[None],["4", "....- "],[None]]],["5", "..... "],[[[None],["6", "-.... "],[None]],["7", "--... "],[None]]],["8", "---.. "],[[[None],["9", "----. "],[[None],[":", "---... "],[None]]],[";", "-.-.-. "],[[[None],["=", "-...- "],[None]],["?", "..--.. "],[[None],["@", ".--.-. "],[None]]]]]],["A", ".- "],[[[[[None],["B", "-... "],[[None],["C", "-.-. "],[None]]],["D", "-.. "],[[[None],["E", ". "],[None]],["F", "..-. "],[None]]],["G", "--. "],[[[None],["H", ".... "],[[None],["I", ".. "],[None]]],["J", ".--- "],[[[None],["K", "-.- "],[None]],["L", ".-.. "],[[None],["M", "-- "],[None]]]]],["N", "-. "],[[[[[None],["O", "--- "],[None]],["P", ".--. "],[[None],["Q", "--.- "],[None]]],["R", ".-. "],[[[None],["S", "... "],[None]],["T", "- "],[None]]],["U", "..- "],[[[None],["V", "...- "],[[None],["W", ".-- "],[None]]],["X", "-..- "],[[[None],["Y", "-.-- "],[None]],["Z", "--.. "],[[None],["_", "..--.- "],[None]]]]]]]

message = input(">>>")
newmssg = message.upper()

isLetter = False
#determines if message is to be put into morse code
#"isLetter = True" means it is to be put into morse code
#"isLetter = False" means that it is morse code that will be decoded

if re.search('\w+',newmssg):
	isLetter = True
otherValues = ["@", "?", ",", ":", ";", "'", "+", "=", "_", "!", "(", ")", "$"]
for i in otherValues:
	if message.count(i) !=0:
		isLetter = True

saver = ""
if isLetter == True:
	wholemssg = newmssg.split()
	for p in wholemssg:
		splitmssg = list(p)
		for i in splitmssg:
			saver = saver + (findMorse(i, indexLetters)) + " "
		saver = saver + " "
else:
	wholemssg = newmssg.split("  ")
#	print(wholemssg)
	for i in wholemssg:
		splitmssg = i.split(" ")
		#print("Into splitmssg")
		#print(splitmssg)
		for i in splitmssg:
#			if(i != ""):
			saver = saver + (findLetter(i, indexMorse))
#			else: 
#				saver = saver + " "
#			saver = saver + " "
	
#!$&'()+,-./0123456789:;=?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_ 

print("Message Decoded: ")
print(saver)
