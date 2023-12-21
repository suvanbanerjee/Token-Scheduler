import PySimpleGUI as sg

layout = [[sg.Column([[sg.Button('Next Token', size=(10, 2))]], justification='center')],
    [sg.Column([[sg.Button('Hold Token', size=(10, 2))]], justification='center')],
    [sg.Column([[sg.Button('Close', size=(6, 1))]], justification='center')]]

window = sg.Window('Token Scheduler', layout, size=(200, 200), finalize=True)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Close':
        break
    elif event == 'Next Token':
        # TODO: Add code for handling "Next Token" button click
        pass
    elif event == 'Put on Hold':
        # TODO: Add code for handling "Put on Hold" button click
        pass
window.close()
