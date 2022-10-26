import PySimpleGUI as sg,sys

layout = [
    [sg.Text('time')],
    [sg.Button("Start"),sg.Button("Lap")]
]
window = sg.Window("Stopwatch",layout,size=(300,300),no_titlebar=True)

while True:
    event , kew = window.read()
    if event in( sg.WIN_CLOSED,"Start"):
        break
window.close()
sys.exit()