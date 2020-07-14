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

#-------------------

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
				bt = ByteHolder()
				bt.byteValue = pw_bytes
				bt.byteOffset = hex(x)
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
			print('Byte at: ' + file1[i].byteColor + file1[i].byteOffset + " \033[92m" + 'are different!')
	return count

def saveToString(data, file, i, ending):
	hexString = data + file[i].byteColor + file[i].byteValue + "\033[92m" + ending
	return hexString

def displayBothFilesInHex(file1, file2):
	hexString = ''
	hexString1 = ''
	hexString2 = ''
	for i in range (len(file1)):
		if(i==0):
			hexString = str(file1[i].byteOffset) + '\t'
		hexString1 = saveToString(hexString1, file1, i, '')
		hexString2 = saveToString(hexString2, file2, i, '')
		if((i+1)%4==0):
			hexString1= hexString1 + ' '
			hexString2= hexString2 + ' '
		if((i+1)%16==0 or i==len(file1)-1):
			# Check length of hexString1, if it doesn't reach the halfway mark, add filler to make alignment work
			# Make sure to fix offsets by adding 1 to i, but check that its not added in the last one to prevent out of bounds error
			
			hexString = hexString + (hexString1 + ' | ' + hexString2) + '\n' + str(file1[i].byteOffset) + '\t'
			hexString1 = ''
			hexString2 = ''
		print(str(i))
			
	
	print('File 1: \t\t     |\t\t File 2:')
	print(hexString)

def printFile(num, hexString):
	print('File '+ num +': ')
	print(hexString)
	print('\n-------------------\n')
#######

def main():
	file1Hex = pickFile()
	file2Hex = pickFile()
	print('Number of differences: ' + str(compareFiles(file1Hex, file2Hex)))
	print('\n\n-------------------\n\n')
	displayBothFilesInHex(file1Hex, file2Hex)


if __name__ == "__main__":
	main()
