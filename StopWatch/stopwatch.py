import PySimpleGUI as sg, sys
from time import time


def create_window():
    sg.theme('black')
    layout = [
        [
            sg.Push(), sg.Text('❌', justification='right', pad=0, enable_events=True, key="-CLOSE-")
        ],
        [sg.VPush()],
        [ sg.Text('', font="Young 27", key="-TIME_TEXT-")],
        [
            sg.Button("Start", button_color=('#FFFFFF', "#FF0000"), border_width=0, key="-START-"),
            sg.Button("Lap", button_color=('#FFFFFF', "#FF0000"), border_width=0, key="-LAP-", visible=False)
        ],
        [sg.Column([[]], key="-LAPS-")],
        [sg.VPush()]
    ]
    return sg.Window("Stopwatch", layout, size=(300, 300), no_titlebar=True, element_justification='center')


window = create_window()
start_time = 0
active = False
laps_count = 0
space_time = 0
while True:
    event, kew = window.read(timeout=10)
    if event in (sg.WIN_CLOSED, "-CLOSE-"):
        break
    if event == "-START-":
        if active:
            laps_count =0
            active = False
            window["-START-"].update('Reset')
            window["-LAP-"].update(visible=False)
        else:
            if start_time > 0:
                window.close()
                window = create_window()
                start_time = 0
            else:
                start_time = time()
                active = True
                window["-START-"].update('Stop')
                window["-LAP-"].update(visible=True)
    if active:
        space_time = round(time() - start_time, 1)
        window["-TIME_TEXT-"].update(space_time)
    if event == "-LAP-":
        laps_count += 1
        window.extend_layout(window['-LAPS-'], [[sg.Text(laps_count), sg.VSeparator(), sg.Text(space_time)]])

window.close()
sys.exit()
