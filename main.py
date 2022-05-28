import tkinter as tk
from tkinter.filedialog import askdirectory
from os import getcwd
from tkinter.font import Font
from PIL import ImageTk


def choose_directory():
    ent_dir.delete(0, tk.END)
    path_work = askdirectory(title='Выберите папку', initialdir='/')
    ent_dir.insert(0, path_work)


window = tk.Tk()
# window.config(bg='#66a5ad')
window.geometry("1920x1080")

frame1 = tk.Frame(master=window, width=450, height=100, bg="#66a5ad")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=900, bg="white")
frame2.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

canvas = tk.Canvas(window, height=400, width=400, bg='#66a5ad', highlightthickness=0)
img = tk.PhotoImage(file='./assets/image_1.png')
image = canvas.create_image(0, 0, anchor='nw', image=img, )
canvas.place(relx=0.02, rely=0.2)

lable = tk.Label(text="walrus detector",
                 bg='white',
                 )
myFont = Font(family="Comic Sans MS", size=64)
lable.configure(font=myFont)
lable.place(relx=0.43, rely=0.1)

lable2 = tk.Label(text='Путь к папке с фотографиями:',
                  bg='white', )
myFont = Font(family="Comic Sans MS", size=16)
lable2.configure(font=myFont)
lable2.place(relx=0.43, rely=0.35)

btn_choose = tk.Button(
    text='Выбрать папку',
    font="Calibri 14",
    height=1,
    width=30,
    fg='black',
    highlightbackground='#66a5ad',
    activebackground='#66a5ad',
    activeforeground='white',
    command=choose_directory,
)
btn_save = tk.Button(
    text='Сохранить результат',
    font="Calibri 14",
    height=1,
    width=30,
    fg='black',
    activebackground='#66a5ad',
    activeforeground='white',
)
ent_dir = tk.Entry(
    highlightbackground='#66a5ad',
    bg='#c4dfe6',
    width=60,
    font="Calibri 16"
)
ent_dir.insert(0, getcwd() + r'\output')
# ent_dir.grid(row=0, column=1, sticky='nsew', pady=5, padx=5)
# btn_choose.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
# btn_save.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
ent_dir.place(relx=0.43, rely=0.4, height=60)
btn_choose.place(relx=0.57, rely=0.5)
btn_save.place(relx=0.57, rely=0.6)
window.mainloop()
