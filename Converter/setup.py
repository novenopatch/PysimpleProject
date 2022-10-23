import PySimpleGUI as sg
layout =[
    [sg.Text("Text"),sg.Spin(['item1','item2','item3','item3',])],
    [sg.Button("Button")],
    [sg.Input()],
    [sg.Text('Test'),sg.Button("Test Button")],
]
sg.Window('Converter',layout).read()