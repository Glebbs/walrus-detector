import tkinter as tk
from tkinter.filedialog import askdirectory
from pathlib import Path
from tkinter.font import Font
from time import sleep
from threading import Thread


def non_gui_stuff():
    sleep(1)


def raise_frame(frame):
    frame.tkraise()


def choose_directory():
    path_work = askdirectory(title='Выберите папку', initialdir='/')
    path = Path(path_work)
    if path.is_dir():
        ent_dir.delete(0, tk.END)
        ent_dir.insert(0, path_work)


def choose_and_save():
    path = askdirectory(title='Выберете папку для сохранения', initialdir=Path.home())
    # TODO логика выгрузки
    path = Path(path)
    label_font = Font(family="Comic Sans MS", size=16)
    if path.is_dir() and Path(ent_dir.get()).is_dir():
        t = Thread(target=non_gui_stuff, daemon=True)
        t.start()

        window.withdraw()
        loading_screen = tk.Toplevel(window, bg="#66a5ad")
        loading_screen.geometry('300x200+500+200')

        loading_label = tk.Label(loading_screen, text="Loading...", font=label_font, bg="#66a5ad")
        loading_label.pack(expand=True)

        # While the thread is alive
        while t.is_alive():
            # Update the root so it will keep responding
            window.update()

        loading_screen.withdraw()
        loading_screen = tk.Toplevel(loading_screen, bg="#66a5ad")
        loading_screen.geometry('300x200+500+200')
        loading_label = tk.Label(loading_screen, text="Complete!", font=label_font, bg="#66a5ad")
        loading_label.pack(expand=True)
    else:
        error_window = tk.Tk()
        error_window.configure(bg="#66a5ad")
        error_window.geometry('300x200+500+200')
        error_label = tk.Label(error_window, text="Путь указан неверно", font=label_font, bg="#66a5ad")
        error_label.pack(expand=True)


window = tk.Tk()
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
    command=choose_and_save,
)
ent_dir = tk.Entry(
    highlightbackground='#66a5ad',
    bg='#c4dfe6',
    width=60,
    font="Calibri 16"
)
ent_dir.insert(0, str(Path.cwd() / 'output'))
ent_dir.place(relx=0.43, rely=0.4, height=60)
btn_choose.place(relx=0.57, rely=0.5)
btn_save.place(relx=0.57, rely=0.6)
window.mainloop()
