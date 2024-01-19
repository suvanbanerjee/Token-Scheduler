from pyscript import document
import json

with open("data.json","r") as file:
    while True:
        token_queue=json.load(file)
        if len(token_queue)<4:
            for _ in range(4-len(token_queue)):
                token_queue.append(0) 
        output_toke_1 = document.querySelector("#token_1")
        output_toke_2 = document.querySelector("#token_2")
        output_toke_3 = document.querySelector("#token_3")
        output_toke_4 = document.querySelector("#token_4")
        output_toke_1.innerText = token_queue[0]
        output_toke_2.innerText = token_queue[1]
        output_toke_3.innerText = token_queue[2]
        output_toke_4.innerText = token_queue[3]