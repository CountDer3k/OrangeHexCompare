# Der3k Burrola
# July 2020
# Orange Hex Compare

import binascii
import emoji
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

class ByteHolder():
	byteValue = ''
	byteColor = "\033[92m"
	byteOffset = -1
	byteNextOffset = -1
	byteFake = False
 
#-------------------

RED = "\033[91m"
BLACK = "\033[92m"

def createByteObject(value, offset, isFake):
	bt = ByteHolder()
	bt.byteValue = value
	bt.byteOffset = hex(offset)
	bt.byteNextOffset = hex(offset+1)
	bt.byteFake = isFake
	return bt

def getHexOf(file):
	hexString = []
	isBlank = False
	x = 0
	with open(file, 'rb') as f:
		while(not isBlank):
			# Reads one byte at a time
			content = f.read(1)
			# Converts to hex then to useable string
			pw_bytes = binascii.hexlify(content)
			pw_bytes = pw_bytes.decode("utf-8")

			if(pw_bytes != ''):	
				bt = createByteObject(pw_bytes, x, False)
				hexString.append(bt)
				x = x + 1
			else:
				isBlank = True
	return hexString

def pickFile():
	print()
	Tk().withdraw()
	file = askopenfilename()
	return getHexOf(file)

def compareFiles(file1, file2):
	info = []
	textInfo = ''
	count = 0
	for i in range(len(file1)):
		if(file1[i].byteValue != file2[i].byteValue and not file1[i].byteFake and not file2[i].byteFake):
			count = count + 1
			file1[i].byteColor = RED
			file2[i].byteColor = RED
			compareString = 'File 1: '  + file1[i].byteColor + file1[i].byteValue + BLACK + ' vs File 2: ' + file1[i].byteColor + file2[i].byteValue + BLACK
			fullString = 'Byte at: ' + file1[i].byteColor + file1[i].byteOffset + BLACK + ' are different! ' + compareString
			textInfo = textInfo + 'Byte at: ' + file1[i].byteOffset + ' are different! ' + 'File 1 Value: ' + file1[i].byteValue + ' vs File 2 Value: ' + file2[i].byteValue + '\n'
			print(fullString)
	info.append(textInfo)
	info.append(count)
	return info

def saveToString(data, file, i, ending):
	hexString = data + file[i].byteColor + file[i].byteValue + "\033[92m" + ending
	return hexString

def displayBothFilesInHex(file1, file2):
	hexString = ''
	hexString1 = ''
	hexString2 = ''
	largerFile = len(file1) if len(file1) > len(file2) else len(file2)
	for i in range (largerFile):
		if(i==0):
			hexString = str(file1[i].byteOffset) + '\t'
		hexString1 = saveToString(hexString1, file1, i, '')
		hexString2 = saveToString(hexString2, file2, i, '')
		if((i+1)%4==0):
			hexString1= hexString1 + ' '
			hexString2= hexString2 + ' '
		if((i+1)%16==0 or i==len(file1)-1):
			if(i==len(file1)-1):
				hexString = hexString + (hexString1 + ' | ' + hexString2) + '\n'
			else:	
				hexString = hexString + (hexString1 + ' | ' + hexString2) + '\n' + str(file1[i].byteNextOffset) + '\t'
				hexString1 = ''
				hexString2 = ''
	print('File 1:                                      | File 2:')
	print(hexString)

def fixAlignmentof(file1, file2):
	#?? Add blank characters at end of file1 if line doesn't align
	files = []
	# blank characters at end of files if they are different sizes
	if(len(file1) != len(file2)):
		if(len(file1) > len(file2)):
			sizeToAdd = len(file1) - len(file2)
			for x in range(sizeToAdd):
				bt = createByteObject('  ', x, True)
				file2.append(bt)
		if(len(file1) < len(file2)):
			sizeToAdd = len(file2) - len(file1)
			for x in range(sizeToAdd):
				bt = createByteObject('  ', x, True)
				file1.append(bt)
	files.append(file1)
	files.append(file2)
	return files

def writeDifferencesToText(file1, file2):
	text_file = open("Diffrences.txt", "w")
	differences = compareFiles(file1, file2)[0]
	os.system('clear')
	toText = ''
	for i in differences:
		toText = toText + i
	n = text_file.write(toText)
	text_file.close()
	print('\nSuccessfully exported to Differences.txt')

def main():
	file1Hex = pickFile()
	file2Hex = pickFile()
	files =	fixAlignmentof(file1Hex, file2Hex)
	file1Hex = files[0]
	file2Hex = files[1]
	isRunning = True
	while(isRunning):
		print('_______________________')
		orange = emoji.emojize(':tangerine:')
		print(' '+orange + 'Orange HexCompare' + orange +'  ')
		print('_______________________\n')
		print('Select an option from below')
		print('[1] Display files side-by-side')
		print('[2] Display differences only')
		print('[3] Export differences to text file')
		print('[4] Exit')
		answer = str(input())		
		os.system('clear')

		if(answer == '1'):
			print('--------------------------')
			print('     File Comparison      ')
			print('--------------------------\n')
			displayBothFilesInHex(file1Hex, file2Hex)
			print('\n\n-------------------\n\n')
		if(answer == '2'):
			print('--------------------------')
			print('    Offset Differences    ')
			print('--------------------------\n')
			print('\nNumber of differences: ' + str(compareFiles(file1Hex, file2Hex)[1]))
			print('\n\n-------------------\n\n')
		if(answer == '3'):
			writeDifferencesToText(file1Hex, file2Hex)
			print('\n\n-------------------\n\n')
		if(answer == '4'):
			print('\n\n-------------------\n\n')
			print('Good-bye')
			isRunning = False
		if(answer == 'Easter Egg'):
			print('*********************************\n*** ****** ***** **** ***********\n*** ****** ********** ************\n*** ****** ***** **** ****  **  *\n*** ****** ***** **** ****  **  *\n***        ***** **** ***********\n*** ****** ***** **** *** ***** *\n*** ****** ***** **** ****      *\n*** ****** ***** **** ***********\n*** ****** ***** **** ***********\n*** ****** ***** ****************\n*** ****** ***** **** ***********\n*********************************')


if __name__ == "__main__":
	main()

