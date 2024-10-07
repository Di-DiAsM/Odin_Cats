from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

Allowed_tags = ["sleep", "jump", "fight", "black", "white", "siamese", "cute"]

def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600, 400), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Произошла ошибка {e}")
        return None

def open_new_window():
    tag = tag_conbobox.get()
    url_tag = f"https://cataas.com/cat/{tag}" if tag else "https://cataas.com/cat"
    img = load_image(url_tag)

    if img:
        new_window = Toplevel()
        new_window.title("Картинка с котиком")
        new_window.geometry("600x400")
        label = Label(new_window, image = img)
        label.pack()
        label.image = img

def exit():
    window.destroy()

window = Tk()
window.title("Cats")
window.geometry("300x150+600+200")

# tag_entry = Entry()
# tag_entry.pack()

# update_butoon = Button(text="Обновить", command=set_image)
# update_butoon.pack()

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход",command=exit)

url = "https://cataas.com/cat"

tag_label = Label(text="Выберите тег")
tag_label.pack()

tag_conbobox = ttk.Combobox(values=Allowed_tags)
tag_conbobox.pack()

load_button = Button(text="Загрузить по тегу", command=open_new_window)
load_button.pack()

window.mainloop()