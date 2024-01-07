import PySimpleGUI as sg
import socket
sg.theme('LightGrey1')



TCP_IP = "127.0.0.1"
TCP_PORT = 1234



def NextToken():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.sendto(bytes("next_token", "utf-8"), (TCP_IP, TCP_PORT))
def HoldToken():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.sendto(bytes("hold_token", "utf-8"), (TCP_IP, TCP_PORT))

layout = [[sg.Column([[sg.Button('Next Token',font="10" , size=(10, 2), button_color='green')]], justification='center')],
    [sg.Column([[sg.Button('Hold Token',font="10", size=(10, 2), button_color='red')]], justification='center')]]

window = sg.Window('Bank', layout, size=(200, 200), finalize=True)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Close':
        break
    elif event == 'Next Token':
        pass
    elif event == 'Put on Hold':
        pass
window.close()
