import PySimpleGUI as sg
layout =[
    [sg.Text("Text"),sg.Spin(['item1','item2','item3','item4',])],
    [sg.Button("Button")],
    [sg.Input()],
    [sg.Text('Test'),sg.Button("Test Button")],
]
window = sg.Window('Converter',layout)

while True :
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
window.close()