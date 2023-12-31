import PySimpleGUI as sg
import socket


UDP_IP = "127.0.0.1"
UDP_PORT = 5005


def NextToken(MESSAGE):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))


layout = [[sg.Column([[sg.Button('Next Token', size=(10, 2))]], justification='center')],
    [sg.Column([[sg.Button('Hold Token', size=(10, 2))]], justification='center')],
    [sg.Column([[sg.Button('Close', size=(6, 1))]], justification='center')]]

window = sg.Window('Token Scheduler', layout, size=(200, 200), finalize=True)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Close':
        break
    elif event == 'Next Token':
        pass
    elif event == 'Put on Hold':
        pass
window.close()
