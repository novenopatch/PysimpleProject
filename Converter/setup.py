import PySimpleGUI as sg
import sys

text_sec = 'Sec to min'
text_km_to_mile = 'Km to mile'
text_kg = 'kg to pound'


list_text = [text_km_to_mile, text_kg, text_sec]
key_convert_button = "-Button-Covert-"
key_spin = "-Spin-"
key_output = "-Output-"
key_input = "-INPUT-"
layout = [
    [
        sg.Input(key=key_input),
     sg.Spin(list_text, key=key_spin),
     sg.Button("Convert", key=key_convert_button)
     ],
    [sg.Text("Output", key=key_output)]

]
window = sg.Window('Converter', layout)


def convert(select: str, text_input: str):
    if select in list_text and text_input.isnumeric():
        text_input = float(text_input)
        print(select)
        match select:
            case str(text_km_to_mile):
                result_cal = round(text_input * 0.6214, 2)
                output_string = f"{text_input} km are {result_cal} miles."
            case str(text_kg):
                result_cal = round(text_input * 2.20462, 2)
                output_string = f"{text_input} kg are {result_cal} pounds."
            case str(text_sec):
                result_cal = round(text_input / 60, 2)
                output_string = f"{text_input} second are {result_cal} minutes."
        window[key_output].update(output_string)
    else:
        window[key_output].update("Please enter a number")


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == key_convert_button:
        if values[key_spin] in list_text and str(values[key_input]).isnumeric():
            text_input = float(values[key_input])
            match values[key_spin]:
                case str(text_km_to_mile):
                    result_cal = round(text_input * 0.6214, 2)
                    output_string = f"{text_input} km are {result_cal} miles."
                case str(text_kg):
                    result_cal = round(text_input * 2.20462, 2)
                    output_string = f"{text_input} kg are {result_cal} pounds."
                case str(text_sec):
                    result_cal = round(text_input / 60, 2)
                    output_string = f"{text_input} second are {result_cal} minutes."
            window[key_output].update(output_string)
        else:
            window[key_output].update("Please enter a number")


        # print(values[key_spin])

window.close()
sys.exit()
