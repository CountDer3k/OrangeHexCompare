import PySimpleGUI as sg
import codeBase as cb
from tkinter import Tk
from tkinter.filedialog import askopenfilename

listBoxWidth = 60
listBoxHeight = 50
sg.theme('DarkGrey3')
sg.theme('Topanga')

def show_hex_differences():
	s = 1

def showBothFiles(file1, file2):
	windowBase.hide()
	windowShow = make_windowShow(file1, file2)

def make_windowBase():
	layout = [
			[sg.Text("Select Files")],
			[sg.Button('Show Both Files')],
		 ]
	return sg.Window('Orange Hex Compare GUI', layout, finalize=True, size=(250,250))

def make_windowShow(file1, file2):
	layout=[]
	item = [sg.Text('File 1 in Hex'), sg.Text('File 2 in Hex')]
	layout.append(item)
	# Shows the 2 files that are being compared
	item = [sg.Listbox(file1, size=(listBoxWidth,listBoxHeight)), 
			sg.Listbox(file2, size=(listBoxWidth,listBoxHeight))]
	layout.append(item)

	item = [sg.Button('Show Only Differences'), sg.Button('Export Differences')]
	layout.append(item)
	return sg.Window('Orange Hex Compare GUI - Showing Files', layout, finalize=True)


windowBase, windowShow, windowDiff = make_windowBase(), None, None

# Main area that will load
def main():
	file1Hex = ''
	file2Hex = ''

	while True:
		window, event, values = sg.read_all_windows()
		# Exits application properly
		if event == 'Quit' or event == sg.WIN_CLOSED:
				exit(0)
		# Events for the main screen
		if window == windowBase:
			if event == 'Show Both Files':
				file1Hex = cb.pick_file()
				file2Hex = cb.pick_file()
				showBothFiles(file1Hex,file2Hex)
		# Events for the window showing the 2 files
		if window == windowShow:
			if event == 'Show Only Differences':
				show_hex_differences()
			elif event == 'Export Differences':
				s = 1



if __name__ == "__main__":
	main()