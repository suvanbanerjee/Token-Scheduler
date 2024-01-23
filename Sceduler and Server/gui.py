import tkinter as tk
import json
def gui():
    latency=1000 #MiliSec
    def update_tokens():
        try:
            with open("./data.json", 'r') as file:
                data = json.load(file)
            # i=0
            # if len(data) > 4:
            #     for _ in range(len(data)//4):
            #         data.insert((4*i)-1, '\n')
            #         i+=1                    
            tokens.config(text='     '.join(data))
        except FileNotFoundError:
            print("File not found: data.json")
        root.after(latency, update_tokens)
    root = tk.Tk()
    root.attributes('-fullscreen',True)
    root.title("Token System")
    root.configure(bg='#FFFFFF')
    tk.Label(text="\nCurrent Tokens\n", bg='#FFFFFF', font=("Helvetica",70,"bold")).pack()
    #tk.Label(text="Procede to counters\n\n\n", font=("Arial",20), bg="#FFFFFF").pack()
    tokens = tk.Label(root, pady=5, padx=5 ,font=("Helvetica",80,"bold"), fg="#0079D3",bg='#FFFFFF')
    tokens.pack()
    update_tokens()
    root.mainloop()

if __name__ == "__main__":
    gui()