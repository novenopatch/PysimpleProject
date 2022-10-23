import PySimpleGUI as sg
import sys
layout =[
    [sg.Text("Text",enable_events = True, key="-TEXT-"),sg.Spin(['item1','item2','item3','item4',])],
    [sg.Button("Button",key='-BUTTON1-')],
    [sg.Input(key="-Input-")],
    [sg.Text('Test'),sg.Button("Button",key='-BUTTON2-')],
]
window = sg.Window('Converter',layout)

while True :
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "-BUTTON1-":
        window["-TEXT-"].update(values["-Input-"])
        print(values)
    if event == "-TEXT-":
            print('text was pressed')
window.close()
sys.exit()