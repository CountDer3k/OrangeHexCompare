# Der3k Burrola
# July 2020
# Orange Hex Compare

import binascii
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def displayFilesInHex(file1, file2):
	hexString1 = ''
	hexString2 = ''
	offset = -16
	largerFile = file1 if len(file1) < len(file2) else file2
	for i in range (len(largerFile)):
		# This is the sidebar that shows the hex offset
		if(i%32==0):
			# 16 is the 16 bytes shown on screen
			offset = offset + 16
			hexString1 = hexString1 + '\n' + hex(offset) + '\t'
			hexString2 = hexString2 + '\n' +hex(offset) + '\t'
		if(i%8==0):
			hexString1 = hexString1 + '\t'
			hexString2 = hexString2 + '\t'
		if(i%2==0):
			if(file1[i] != file2[i]):
				hexString1 = hexString1 + "\033[91m"+ file1[i]
				hexString2 = hexString2 + "\033[91m"+ file2[i]
			else:	
				hexString1 = hexString1 + file1[i]+ "\033[92m"
				hexString2 = hexString2 + file2[i]+ "\033[92m"
		else:	
			hexString1 = hexString1 + file1[i] + ' '+ "\033[92m"
			hexString2 = hexString2 + file2[i] + ' '+ "\033[92m"
	#Print information out to the screen
	print('File 1: ')
	print(hexString1)
	print('\n-------------------\n')
	print('File 2: ')
	print(hexString2)


def getHexOf(file):
	hexString = ''
	with open(file, 'rb') as f:
    # Change 100 to read from the length of entire file
		for x in range(1000):
			# Reads one byte at a time
			content = f.read(1)
			# Converts to hex then to useable string
			pw_bytes = binascii.hexlify(content)
			pw_bytes = pw_bytes.decode("utf-8")
			hexString = hexString + str(pw_bytes)
	return hexString

def pickFile():
	print()
	Tk().withdraw()
	file = askopenfilename()
	fileHex = getHexOf(file)
	return fileHex
	

def compareFiles(file1, file2):
	for i in range( len(file1) ):
		if((i%2==0) and (i > 2)):
			byte1 = file1[i] + file1[i+1]
			byte2 = file2[i] + file2[i+1]
			if(byte1 != byte2):
				# Removes the 4 spaces added at the top
				i = 0 if (i) < 0 else (i)
				print('Byte at: ' + "\033[91m"+ str(hex(i)) + "\033[92m"+ ' are different!')


def main():
	file1Hex = pickFile()
	file2Hex = pickFile()
	displayFilesInHex(file1Hex, file2Hex)
	compareFiles(file1Hex, file2Hex)



if __name__ == "__main__":
	main()