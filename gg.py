import tkinter as tk
from tkinter import PhotoImage , Button , Label 

root = tk.Tk()
root.title('Ajy')



root.image = PhotoImage(file='SEKIROOOO.jpg')
bg_logo = Label(root, image=root.image)
bg_logo.grid(row=0, column=0)

btn = Button(root, text='Python')

root.mainloop()