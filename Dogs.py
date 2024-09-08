from tkinter import *
from tkinter import messagebox as mb
from PIL import Image, ImageTk
import requests
from io import BytesIO

from bottle import response
from pygame.examples.cursors import image


def show_image(): # выводит изображение, но сначало получает из инета
    image_url = get_dog_image()# получаем ссылку
    if image_url:# если ссылка не пустая тру
        try:
            requests=requests.get(image_url,strieam= True)
            requests.raise_for_status()
            img_data = BytesIO (response.content)
            img = Image.open(img_data)
            img.thumbnail((300,300))
            label.config(image=img)
            label.image=img
        except Exception as e:
            mb.showerror("Ошибка", f "Возникла ошибка {e}")



window = Tk()
window.title("Картинки с собачками")
window.geometry("360x420")

label = Label()
label.pack(pady=10)

button = Button (text="Загрузить изображение", command=show_image)
button.pack (pady=10)


window.mainloop()
