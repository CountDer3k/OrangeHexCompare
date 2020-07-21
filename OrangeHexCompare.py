# Der3k Burrola
# July 2020
# Orange Hex Compare

import codeBase
import emoji
import os
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

ORANGE_EMOJI = emoji.emojize(':tangerine:')

def main():
	file1Hex = codeBase.pickFile()
	file2Hex = codeBase.pickFile()
	files =	codeBase.fixAlignmentof(file1Hex, file2Hex)
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
			codeBase.displayBothFilesInHex(file1Hex, file2Hex)
			print('\n\n-------------------\n\n')
		if(answer == '2'):
			print('--------------------------')
			print('    Offset Differences    ')
			print('--------------------------\n')
			print('\nNumber of differences: ' + str(codeBase.compareFiles(file1Hex, file2Hex)[1]))
			print('\n\n-------------------\n\n')
		if(answer == '3'):
			codeBase.writeDifferencesToText(file1Hex, file2Hex)
			print('\n\n-------------------\n\n')
		if(answer == '4'):
			print('\n\n-------------------\n\n')
			print('Good-bye')
			isRunning = False
		if(answer == 'Easter Egg'):
			print('*********************************\n*** ****** ***** **** ***********\n*** ****** ********** ************\n*** ****** ***** **** ****  **  *\n*** ****** ***** **** ****  **  *\n***        ***** **** ***********\n*** ****** ***** **** *** ***** *\n*** ****** ***** **** ****      *\n*** ****** ***** **** ***********\n*** ****** ***** **** ***********\n*** ****** ***** ****************\n*** ****** ***** **** ***********\n*********************************')

def OrangeLayout(self):
	self.title = ORANGE_EMOJI + 'Orange HexCompare' + ORANGE_EMOJI
	layout = GridLayout(cols=3)
	layout.add_widget(Label(text='1\n2\n3\n4\n5\n6\n7', size_hint_x=None, width=35))
	layout.add_widget(Label(text='Hex Edit 1'))
	layout.add_widget(Label(text='Hex Edit 2'))
	return layout

#if __name__ == "__main__":
#	main()


class MyApp(App):

	def build(self):
		layout = OrangeLayout(self)
		return layout

        


if __name__ == '__main__':
    MyApp().run()




