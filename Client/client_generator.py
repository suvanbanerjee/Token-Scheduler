import PySimpleGUI as sg

sg.theme('LightGrey1')
count = 1

def gen_token(counter):
    global count
    token = str(count) + counter
    count += 1
    return token

layout = [
    [sg.Text('\nWelcome to Namma Bank\n', font='Helvetica 50 bold', justification='centre', expand_x=True)],
    [sg.Text('Please seclect a Counter to get a token\n', font='Helvetica 20', justification='center', expand_x=True)],
    [sg.Column([[sg.Button('A', size=(5, 3), font='Helvetica 30'),
                sg.Button('B', size=(5, 3), font='Helvetica 30'),
                sg.Button('C', size=(5, 3), font='Helvetica 30'),
                sg.Button('D', size=(5, 3), font='Helvetica 30')]], justification='center')],
    
]

window = sg.Window('Token Scheduler', layout, finalize=True, resizable=True)
window.maximize()
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event:
        token=gen_token(event)
        layout2=[
            [sg.Text('\n  Your token is \n', font='Helvetica 20', justification='center', expand_x=True)],
            [sg.Text(token, font='Helvetica 50 bold', justification='center', expand_x=True, text_color='#0079D3')],
            [sg.Text('\n  Please wait for your turn \n', font='Helvetica 15', justification='center', expand_x=True)],
            [sg.Column([[sg.Button('Close', size=(5, 2), font='Helvetica 12', button_color="#0079D3")]], justification='center')]
        ]
        token_window = sg.Window('Token', layout2, finalize=True, resizable=False)
        event, values = token_window.read()
        if event == sg.WINDOW_CLOSED or event == 'Close':
            token_window.close()
window.close()