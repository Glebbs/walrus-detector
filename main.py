import tkinter as tk
from time import sleep
from tkinter.filedialog import askdirectory
from pathlib import Path
import threading


def non_gui_stuff():
    sleep(3)


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#66a5ad')

        self.btn_choose = tk.Button(
            self,
            text='Выбрать папку',
            fg='black',
            highlightbackground='#66a5ad',
            activeforeground='green',
            command=self.choose_directory,
        )
        self.btn_save = tk.Button(
            self,
            text='Сохранить результат',
            fg='black',
            highlightbackground='#66a5ad',
            activeforeground='green',
            command=controller.calculate,
        )
        self.ent_dir = tk.Entry(
            self,
            highlightbackground='#66a5ad',
            bg='#c4dfe6',
            width=60,
        )
        self.build_dir = Path.cwd() / 'output'
        self.ent_dir.insert(0, str(self.build_dir))
        self.ent_dir.pack()
        self.btn_choose.pack()
        self.btn_save.pack()

    def choose_directory(self):
        self.ent_dir.delete(0, tk.END)
        path_work = askdirectory(title='Выберите папку', initialdir='/')
        self.ent_dir.insert(0, path_work)


class LoadScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#66a5ad')
        label = tk.Label(self, text="Schitaem pelmeni")
        label.pack(padx=10, pady=10)


class FinishScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#66a5ad')
        label = tk.Label(self, text="poschitali blya")
        label.pack(padx=10, pady=10)


class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Walrus detection")

        container = tk.Frame(self, height=400, width=600)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainPage, LoadScreen, FinishScreen):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def calculate(self):
        t = threading.Thread(target=non_gui_stuff, daemon=True)
        t.start()
        self.show_frame(LoadScreen)
        while t.is_alive():
            self.update()
        self.show_frame(FinishScreen)


if __name__ == "__main__":
    window = Window()
    window.mainloop()
