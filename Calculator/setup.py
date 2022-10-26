import PySimpleGUI as sg
import sys
import math


def create_window(theme: str):
    sg.theme(theme)
    button_size = (6, 3)
    sg.set_options(font='Franklin 14', button_element_size=button_size)
    layout = [
        # [sg.Push(),sg.Text("Output")],
        [sg.Text(
                '🕘',
                font='Franklin 20',
                justification='right',
                pad=(5, 5),
                right_click_menu=theme_menu,
            ), sg.Text(
                '0',
                font='Franklin 20',
                justification='right',
                pad=(5, 5),
                right_click_menu=theme_menu,
                key="-History-",
            ),
            sg.Text(
                '0',
                font='Franklin 20',
                justification='right',
                expand_x=True,
                pad=(5, 5),
                right_click_menu=theme_menu,
                key="-Ans-OutPut-",
            )
        ],
        [
            sg.Text(
                '0',
                font='Franklin 26',
                justification='right',
                expand_x=True,
                pad=(10, 20),
                right_click_menu=theme_menu,
                key="-OutPut-",
            )
        ],
        [sg.Button('(', expand_x=True), sg.Button(')', expand_x=True), sg.Button('◀', expand_x=True, key="Clear"),
         sg.Button('✖', size=button_size, key="*")],
        [sg.Button('7', size=button_size), sg.Button('8', size=button_size), sg.Button('9', size=button_size),
         sg.Button('/', size=button_size, key="/")],
        [sg.Button('4', size=button_size), sg.Button('5', size=button_size), sg.Button('6', size=button_size),
         sg.Button('➖', size=button_size, key="-")],
        [sg.Button('1', size=button_size), sg.Button('2', size=button_size), sg.Button('3', size=button_size),
         sg.Button('➕', size=button_size, key="+")],
        [sg.Button('Ans', expand_x=True), sg.Button('0', expand_x=True), sg.Button('.', size=button_size),sg.Button('=', size=button_size)]
    ]
    return sg.Window("Calculator", layout)


def get_last_element_and_his_index_in_list() -> list:
    len_list_num = len(current_num)
    if len_list_num > 1:
        return [len(current_num) - 1, current_num[len(current_num) - 1]]
    elif len_list_num == 1:
        return [0, current_num[0]]

def update_screen(type:int=2,):
    if type ==1:
        window["-History-"].update("".join(current_num))
        window["-Ans-OutPut-"].update(str(round(eval("".join(current_num)),2)))

    else:
        window["-OutPut-"].update("".join(current_num))
theme_menu = ["menu", ['LightGrey1', 'dark', 'DarkGray8', 'random']]
window = create_window('dark')
current_num = []
current_operation = []
last_result = 0
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event in theme_menu[1]:
        window.close()
        window = create_window(event)
    if event in [str(i) for i in range(0, 10)] or event in ['+', '-', '/', '*', '.', '(', ')']:
        current_num.append(event)
        window["-OutPut-"].update("".join(current_num))
        print(current_num)
    # if event in ['+', '-', '/', '*']:current_operation.append("".join(current_num))current_operation.append(event)window["-OutPut-"].update("".join(current_operation))
    if event == "Clear":
        if len(current_num) >0:
            del current_num[ get_last_element_and_his_index_in_list()[0] ]
        update_screen()
        print(current_num)
    if event == "Ans":
       #hhhhhh
       current_num.insert(0,str(last_result))
       update_screen()

    if event == "=":
        try:
            last_result = eval("".join(current_num))
            window["-OutPut-"].update(last_result)
            update_screen(1)
        except Exception as e:
            print(e)
        finally:
            current_num.clear()
window.close()

sys.exit()
