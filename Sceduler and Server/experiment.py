import PySimpleGUI as sg
import multiprocessing

sg.theme('LightGrey1')

token_queue = [0,0,0,0]

layout = [
    [sg.Text('\nCurrent Token\n', font='Helvetica 50 bold', justification='centre', expand_x=True)],
    [sg.Text('\n\n\n', font='Helvetica 20', justification='center', expand_x=True)],
    [sg.Column([[sg.Button(token_queue[0], size=(5, 3), font='Helvetica 50 bold',pad=(50,0)),
                sg.Button(token_queue[0], size=(5, 3), font='Helvetica 50 bold', pad=(50,0)),
                sg.Button(token_queue[0], size=(5, 3), font='Helvetica 50 bold', pad=(50,0)),
                sg.Button(token_queue[0], size=(5, 3), font='Helvetica 50 bold', pad=(50,0))]], justification='center')],
]

while True:

    window = sg.Window('Token Scheduler', layout, finalize=True, resizable=True)
    window.maximize()

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            window.close()
            exit()
        