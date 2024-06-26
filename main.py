import random
import tkinter as tk
from tkinter import Entry, Button, Label , PhotoImage
from pygame import mixer


def generate_key():
    key = ''.join(random.choice('0123456789ABCDEF') for i in range(15))
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key)
    
   
window = tk.Tk()
window.title("Генератор ключей перед Божественным Драконом")
window.geometry('1300x750')
window.resizable(width=False , height=False) 

 
 
mixer.init()
mixer.music.load('29. Children of Rejuvenation.mp3')

mixer.music.play(-1)


background_image = tk.PhotoImage(file='SEKIR.png')  
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)


key_entry = Entry(window, font=("Helvetica", 16))
key_entry.pack(pady=20)

generate_button = Button(window, text="Сгенерировать ключ Дракона", command=generate_key)
generate_button.pack(pady=10)


window.mainloop()

	