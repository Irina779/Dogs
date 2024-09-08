from tkinter import *
from tkinter import messagebox as mb
from PIL import Image, ImageTk
import requests
from io import BytesIO

from bottle import response


def get_dog_image():
    try:
        response=reguests.get(https://dog.ceo/api/breeds/image/random)
        response.raise_for_status()
        data = response.json()
        return data ('message')
    except EXCEPTION as e:
        md.showerror("Ошибка", f "Возникла ошибка при загрузке изображения {e}")
        return None




def show_image(): # выводит изображение, но сначало получает из инета
    image_url = get_dog_image()# получаем ссылку
    if image_url:# если ссылка не пустая тру
        try:
            requests=requests.get(image_url,strieam= True)
            requests.raise_for_status()
            img_data = BytesIO (response.content)
            img = Image.open(img_data)
            img.thumbnail((300,300))
            img. = ImageTk.PhotoImage(img)
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
