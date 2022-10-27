import PySimpleGUI as sg, sys
from  time  import  time
start_time = time()
def convert_pos_to_pixel(cell):
    tl = cell[0] * CELL_SIZE, cell[1] * CELL_SIZE
    br = tl[0] + CELL_SIZE, tl[1] + CELL_SIZE
    return tl, br


FIELD_SIZE = 800
CELL_NUM = 20
CELL_SIZE = FIELD_SIZE / CELL_NUM

snake_body = [(4, 4), (3, 4), (2, 4)]
DIRECTIONS = {'left': (-1, 0), 'right': (1, 0), 'up': (0, 1), 'down': (0, -1)}
direction = DIRECTIONS['up']
fruit_pos = (0, 0)
sg.theme('Green')
field = sg.Graph(
    canvas_size=(FIELD_SIZE, FIELD_SIZE),
    graph_bottom_left=(0, 0),
    graph_top_right=(FIELD_SIZE, FIELD_SIZE),
    background_color='black'
)
layout = [[field]]
window = sg.Window("Snake", layout, return_keyboard_events=True)

while True:
    event, values = window.read(timeout=10)
    if event == sg.WIN_CLOSED:
        break
    if event == 'Left:37': print('left')
    if event == 'Up:38': print('up')
    if event == 'Right:39': print('right')
    if event == 'Down:40': print('down')
    time_since_start = time() - start_time
    if time_since_start >= 0.5:
        start_time = time()
        new_head = (snake_body[0][0]+direction[0],snake_body[0][1]+direction[1])
        snake_body.insert(0,new_head)
        snake_body.pop()

        tl, br = convert_pos_to_pixel(fruit_pos)
        field.DrawRectangle(tl, br, 'red')

        #draw black frame to end snake move
        field.DrawRectangle((0,0),(FIELD_SIZE,FIELD_SIZE),'black')

        for index,part in enumerate(snake_body):
            tl,br = convert_pos_to_pixel(part)
            color = 'yellow' if index == 0 else 'green'
            field.DrawRectangle(tl, br, color)
window.close()
sys.exit()
