import PySimpleGUI as sg
import time
import cv2
layout = [[sg.Input(key='id')],
          [sg.T("tran le quy bao",key='label')],
          [sg.Image(key ='image',size = (300,300)),sg.T("                         \n\n                      \n\n                      ",key='name')],
          [sg.B("click")]]
window = sg.Window("OK",layout)
while True:
	event,values = window.read(timeout=100)
	if event =="Exit" or event == sg.WIN_CLOSED:
		break
	val = values['id']
	
	if val !='':
		print(val)

		if val =='0010995725':
			img = cv2.imread("1.jpg")
			print("tran le quy bao")
			imgbytes = cv2.imencode('.png', img)[1].tobytes()
			window['image'].update(data=imgbytes)
			window.FindElement('name').Update("Tran Le Quy Bao\n\n Tuoi : 24\n\n Giao Vien ")
		if val =='0007707061':
			img = cv2.imread("2.jpg")
			print("huynhlevu")
			imgbytes = cv2.imencode('.png', img)[1].tobytes()
			window['image'].update(data=imgbytes)
			window.FindElement('name').Update("Gai Xinh\n\n Tuoi : 24 \n\n Giao Vien ")			
	window.FindElement('label').Update(val)
	#if len(val) < 11:
	time.sleep(0.8)
	window.FindElement('id').Update("")
	
	if event=='click':
		print('ok')




	#window.FindElement('id').Update("")
	    #window.FindElement('id').Update(val)
	

