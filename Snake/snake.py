from random import randint

import PySimpleGUI as sg, sys
from time import time

start_time = time()


def convert_pos_to_pixel(cell):
    tl = cell[0] * CELL_SIZE, cell[1] * CELL_SIZE
    br = tl[0] + CELL_SIZE, tl[1] + CELL_SIZE
    return tl, br


def replace_fruit():
    n_fruit_pos = randint(0, CELL_NUM - 1), randint(0, CELL_NUM - 1)
    while n_fruit_pos in snake_body:
        n_fruit_pos = randint(0, CELL_NUM - 1), randint(0, CELL_NUM - 1)
    return n_fruit_pos


FIELD_SIZE = 800
CELL_NUM = 20
CELL_SIZE = FIELD_SIZE / CELL_NUM

snake_body = [(4, 4), (3, 4), (2, 4)]
DIRECTIONS = {'left': (-1, 0), 'right': (1, 0), 'up': (0, 1), 'down': (0, -1)}
direction = DIRECTIONS['up']
fruit_pos = (0, 0)
fruit_eaten = False
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
    if event == 'Left:37':
        direction = DIRECTIONS['left']
    if event == 'Up:38':
        direction = DIRECTIONS['up']
    if event == 'Right:39':
        direction = DIRECTIONS['right']
    if event == 'Down:40':
        direction = DIRECTIONS['down']
    time_since_start = time() - start_time
    if time_since_start >= 0.5:
        start_time = time()
        if snake_body[0] == fruit_pos:
            fruit_eaten = True
            fruit_pos = replace_fruit()

        new_head = (snake_body[0][0] + direction[0], snake_body[0][1] + direction[1])
        snake_body.insert(0, new_head)
        if not fruit_eaten:
            snake_body.pop()
        fruit_eaten = False

        if not 0 <= snake_body[0][0] <= CELL_NUM - 1 or \
                not 0 <= snake_body[0][1] <= CELL_NUM - 1 or snake_body[0] in snake_body[1:]:
            break

        # draw black frame to end snake move
        field.DrawRectangle((0, 0), (FIELD_SIZE, FIELD_SIZE), 'black')

        tl, br = convert_pos_to_pixel(fruit_pos)
        field.DrawRectangle(tl, br, 'red')

        for index, part in enumerate(snake_body):
            tl, br = convert_pos_to_pixel(part)
            color = 'yellow' if index == 0 else 'green'
            field.DrawRectangle(tl, br, color)
window.close()
sys.exit()
