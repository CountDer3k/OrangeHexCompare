# Der3k Burrola
# July 2020
# Orange Hex Compare

import binascii
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

class ByteHolder():
	byteValue = ''
	byteColor = "\033[92m"
	byteOffset = -1
	byteNextOffset = -1
 
#-------------------

def getHexOf(file):
	#?? Add blank characters at end of files if they are different sizes
	#?? Add blank characters at end of file1 if line doesn't align
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
				bt = ByteHolder()
				bt.byteValue = pw_bytes
				bt.byteOffset = hex(x)
				bt.byteNextOffset = hex(x+1)
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
	count = 0
	for i in range(len(file1)):
		if(file1[i].byteValue != file2[i].byteValue):
			count = count + 1
			file1[i].byteColor = "\033[91m"
			file2[i].byteColor = "\033[91m"
			compareString = 'File 1: '  + file1[i].byteColor + file1[i].byteValue + " \033[92mvs File 2: " + file1[i].byteColor + file2[i].byteValue + " \033[92m"
			print('Byte at: ' + file1[i].byteColor + file1[i].byteOffset + " \033[92m" + 'are different! ' + compareString)
	return count

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

def printFile(num, hexString):
	print('File '+ num +': ')
	print(hexString)
	print('\n-------------------\n')
#######

def main():
	file1Hex = pickFile()
	file2Hex = pickFile()
	isRunning = True
	while(isRunning):
		print('Select an option from below')
		print('[1] Display 2 files side by side')
		print('[2] Display differences only')
		print('[3] Exit')
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
			print('\nNumber of differences: ' + str(compareFiles(file1Hex, file2Hex)))
			print('\n\n-------------------\n\n')
		if(answer == '3'):
			print('\n\n-------------------\n\n')
			print('Good-bye')
			isRunning = False



	
	
	
	#??Ask user to show comparison or show differences only


if __name__ == "__main__":
	main()
