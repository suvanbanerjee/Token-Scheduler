import PySimpleGUI as sg
import socket
import pygame.mixer

pygame.mixer.init()
ding = pygame.mixer.Sound('ding.mp3')
sg.theme('LightGrey1')

TCP_IP = "127.0.0.1"
TCP_PORT = 1234

def NextToken():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if sock.connect_ex((TCP_IP, TCP_PORT)) == 0:
        sock.sendto(bytes("next_token", "utf-8"), (TCP_IP, TCP_PORT))
        ding.play()
    else:
        sg.popup("Server is not running")

def HoldToken():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if sock.connect_ex((TCP_IP, TCP_PORT)) == 0:
        sock.sendto(bytes("hold_token", "utf-8"), (TCP_IP, TCP_PORT))
        ding.play()
    else:
        sg.popup("Server is not running")

layout = [[sg.Column([[sg.Button('Next Token',font="10" , size=(10, 2), button_color='green')]], justification='center')],
    [sg.Column([[sg.Button('Hold Token',font="10", size=(10, 2), button_color='red')]], justification='center')]]

window = sg.Window('Bank', layout, size=(200, 200), finalize=True)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Close':
        break
    elif event == 'Next Token':
        NextToken()
    elif event == 'Hold Token':
        HoldToken()

window.close()
