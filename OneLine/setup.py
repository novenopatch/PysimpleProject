import  PySimpleGUI as sg
import sys
layout = [
    [ sg.Button('clear'),sg.Button('enter') ],
    [sg.Button('7'),sg.Button('8'),sg.Button('9'),sg.Button('*')],
    [],[],[]
]
window =sg.Window("Calculator",[[sg.Input(),sg.Button('Ok'),sg.Button('Cancel')]])
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
sys.exit()