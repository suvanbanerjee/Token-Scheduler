import PySimpleGUI as sg
import socket
sg.theme('LightGrey1')



UDP_IP = "127.0.0.1"
UDP_PORT = 5005


def NextToken(MESSAGE):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))


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
