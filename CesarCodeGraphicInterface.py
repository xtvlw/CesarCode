#_[N_F]_

import tkinter as tk

window = tk.Tk()

final_message = ''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3


def pClick():
    global key
    if key < 25:
        key += 1
    else:
        key = key
    keylabel["text"] = key


def mClick():
    global key
    if key > 1:
        key -= 1
    else:
        key = key
    keylabel["text"] = key


def Crypt():
    global final_message
    Message["text"] = ''
    n = 0
    message = str(box.get()).lower()
    while n < len(message):
        i = int(alphabet.find((message[n])))
        if message[n] in alphabet:
            final_message += alphabet[(i + key) % len(alphabet)]
        else:
            final_message += message[n]
        n += 1
    Message["text"] = final_message
    final_message = ''

def Decrypt():
    Message["text"] = ''
    n = 0
    global final_message
    message = str(box.get()).lower()
    while n < len(message):
        i = int(alphabet.find((message[n])))
        if message[n] in alphabet:
            final_message += alphabet[(i - key) % len(alphabet)]
        else:
            final_message += message[n]
        n += 1
    Message["text"] = final_message
    final_message = ''


box = tk.Entry(window, width=47)
box.place(x=5, y=5)

cryptButtonC = tk.Button(window, width=10, text="Crypt", command=Crypt)
cryptButtonC.place(x=5, y=90)

cryptButtonD = tk.Button(window, width=10, text="Decrypt", command=Decrypt)
cryptButtonD.place(x=190, y=90)


pButton = tk.Button(window, width=10, height=1, text="-", command=mClick)
pButton.place(x=5, y=50)

mButton = tk.Button(window, width=10, height=1, text="+", command=pClick)
mButton.place(x=190, y=50)

keylabelM = tk.Label(window, width=10, height=1, text="key")
keylabelM.place(x=100, y=30)

keylabel = tk.Label(window, width=10, height=1, text=key, relief='solid', background='white')
keylabel.place(x=100, y=50)

Message = tk.Label(window, text="crypt", width=40, height=1, relief='solid', background='white' )
Message.place(x=5, y=150)


window.title("Cesar Code")
window.geometry("300x250")
window.mainloop()
