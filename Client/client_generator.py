import PySimpleGUI as sg
sg.theme('LightGrey1')
count=1

def GenToken(counter):
    token=str(count)+counter
    count+=1
    return token

layout = [
    [sg.Column([[sg.Button('Token A', size=(10, 2) , font="Times 50")]], justification='center')],
    [sg.Column([[sg.Button('Token C', size=(10, 2))]], justification='center')],
    [sg.Column([[sg.Button('Token C', size=(10, 2))]], justification='center')],
    [sg.Column([[sg.Button('Token D', size=(10, 2))]], justification='center')],
    [sg.Column([],size=(10, 10))],
    [sg.Column([[sg.Button('Close', size=(100, 20))]], justification='center')]]
window = sg.Window('Token Scheduler', layout, finalize=True, resizable=True)
window.maximize()

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Close':
        break
    elif event == 'Next Token':
        pass
    elif event == 'Put on Hold':
        pass
window.close()