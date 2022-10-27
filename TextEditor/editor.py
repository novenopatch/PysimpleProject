import PySimpleGUI as sg, sys
from pathlib import Path

smileys = [
    'happy', [';)', ':)', '>:(', 'O.O', '~_~', '+_+'],
    'sad', ['X_X', 'T_T', '^_^ ', '^_~', 'O.O'],
    'other', [';-)', ':-)', ':-()', ':O', '>_<']
]
smileys_events = smileys[1] + smileys[3] + smileys[5]
menu_layout = [
    ['File', ['Open', 'Save', '---', 'Exit']],
    ['Tools', ['Word Count','Character Count']],
    ['Add', smileys]
]
sg.theme('GrayGrayGray')
layout = [
    [sg.Menu(menu_layout)],
    [sg.Text("Untitled", key='-DOCNAME-')],
    [sg.Multiline(no_scrollbar=True, size=(40,30),key = '-TEXTBOX-')]
]

window = sg.Window('Text Editor', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event =='Word Count':
        full_text = values[ '-TEXTBOX-']
        clean_text = full_text.replace('\n',' ').split(' ')
        word_count = len(clean_text)
        sg.popup(f"word count:{word_count}")
    if event == 'Character Count':
        full_text = values['-TEXTBOX-']
        clean_text = full_text.replace('\n', ' ').split(' ')
        sg.popup(f"Char Count:{len(''.join(clean_text))}")
    if event in smileys_events:
        current_text = values['-TEXTBOX-']
        new_text = current_text + " " + event
        window['-TEXTBOX-'].update(new_text)
    if event == 'Open':
        file_path = sg.popup_get_file('open',no_window= True)
        if file_path:
            file = Path(file_path)
            window['-DOCNAME-'].update(file.name)
            window['-TEXTBOX-'].update(file.read_text('UTF-8'))

    if event == 'Save':
        file_path = sg.popup_get_file('Save as', no_window=True,save_as=True) + '.txt'
        file = Path(file_path)
        file.write_text(values['-TEXTBOX-'],'UTF-8')
        window['-DOCNAME-'].update(file.name)



window.close()
sys.exit()
