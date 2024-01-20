import tkinter as tk
import json
latency=1000 #MiliSec
def update_tokens():
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
        tokens.config(text='     '.join(data))
    except FileNotFoundError:
        print("File not found: data.json")
    root.after(latency, update_tokens)
root = tk.Tk()
root.attributes('-fullscreen',True)
root.title("Token System")
tk.Label(text="\nCurrent Tokens\n", font=("Arial",70,"bold")).pack()
# tk.Label(text="Procede to counters\n", font=("Arial",20)).pack()
tokens = tk.Label(root, pady=5, padx=5 ,font=("Heavlitica",90,"bold"), fg="#0079D3")
tokens.pack()
update_tokens()
root.mainloop()