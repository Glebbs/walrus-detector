import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory
from pathlib import Path


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
        )
        self.ent_dir = tk.Entry(
            self,
            highlightbackground='#66a5ad',
            bg='#c4dfe6',
            width=60,
        )
        self.build_dir = Path.cwd() / 'output'
        self.ent_dir.insert(0, str(self.build_dir))

        self.switch_window_button = tk.Button(
            self,
            text="Go to the Side Page",
            command=lambda: controller.show_frame(SidePage),
        )
        self.ent_dir.pack()
        self.btn_choose.pack()
        self.btn_save.pack()
        self.switch_window_button.pack(side="bottom", fill=tk.X)

    def choose_directory(self):
        self.ent_dir.delete(0, tk.END)
        path_work = askdirectory(title='Выберите папку', initialdir='/')
        self.ent_dir.insert(0, path_work)


class SidePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is the Side Page")
        label.pack(padx=10, pady=10)

        switch_window_button = tk.Button(
            self,
            text="Go to the Completion Screen",
            command=lambda: controller.show_frame(CompletionScreen),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


class CompletionScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Completion Screen, we did it!")
        label.pack(padx=10, pady=10)
        switch_window_button = ttk.Button(
            self, text="Return to menu", command=lambda: controller.show_frame(MainPage)
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Walrus detection")

        container = tk.Frame(self, height=400, width=600)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainPage, SidePage, CompletionScreen):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


if __name__ == "__main__":
    window = Window()
    window.mainloop()
