import tkinter as tk
from tkinter import Entry, Button, Label
import random

def generate_key():
    key = ''.join(random.choice('0123456789ABCDEF') for i in range(16))
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key)

# Создаем основное окно
window = tk.Tk()
window.title("Генератор ключей")

# Найденная картинка на фоне
background_image = tk.PhotoImage(file="")  # Замените "background_image.png" на путь к вашей картинке
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Поле для генерируемого ключа
key_entry = Entry(window, font=("Helvetica", 16))
key_entry.pack(pady=20)

# Кнопка для запуска генерации ключа
generate_button = Button(window, text="Сгенерировать ключ", command=generate_key)
generate_button.pack(pady=10)

# Запуск основного цикла обработки событий
window.mainloop()