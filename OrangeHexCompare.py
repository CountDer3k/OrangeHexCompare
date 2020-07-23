# Der3k Burrola
# July 2020
# Orange Hex Compare

import codeBase, os, kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import *


def main():
	file1Hex = codeBase.pickFile()
	file2Hex = codeBase.pickFile()
	files =	codeBase.fixAlignmentof(file1Hex, file2Hex)
	file1Hex = files[0]
	file2Hex = files[1]
	isRunning = True
	while(isRunning):


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
	

	file1Hex = codeBase.pickFile()
	file2Hex = codeBase.pickFile()
	files = codeBase.FormatFilesInHex(file1Hex,file2Hex)
	file1Hex = files[0]
	file2Hex = files[1]
	hexCount = files[2]

	layout = GridLayout(cols=5)
	layout.add_widget(Label(text=hexCount, size_hint_x=None, width=50))

	separatorLabel = Label(size_hint_x=None, width=3)
	with separatorLabel.canvas:
            Color(1, 1, 1, 1)
            Rectangle(pos=(42,0), size=(3,1000))
	layout.add_widget(separatorLabel)

	layout.add_widget(Label(text=file1Hex, markup=True))
	separatorLabel2 = Label(size_hint_x=None, width=3)
	with separatorLabel2.canvas:
            Color(1, 1, 1, 1)
            Rectangle(pos=(415, 0), size=(3,1000))
	layout.add_widget(separatorLabel2)
	layout.add_widget(Label(text=file2Hex, markup=True))
	return layout


class MyApp(App):

	def build(self):
		self.title = codeBase.ORANGE_EMOJI + 'Orange HexCompare' + codeBase.ORANGE_EMOJI
		layout = OrangeLayout(self)
		return layout

        


if __name__ == '__main__':
    MyApp().run()




