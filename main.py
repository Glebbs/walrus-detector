import tkinter as tk
from tkinter.filedialog import askdirectory
from pathlib import Path

def choose_directory():
    ent_dir.delete(0, tk.END)
    path_work = askdirectory(title='Выберите папку', initialdir='/')
    ent_dir.insert(0, path_work)


window = tk.Tk()
window.config(bg='#66a5ad')
window.geometry('600x100')
btn_choose = tk.Button(
    text='Выбрать папку',
    fg='black',
    highlightbackground='#66a5ad',
    activeforeground='green',
    command=choose_directory,
)
btn_save = tk.Button(
    text='Сохранить результат',
    fg='black',
    highlightbackground='#66a5ad',
    activeforeground='green',
)
ent_dir = tk.Entry(
    highlightbackground='#66a5ad',
    bg='#c4dfe6',
    width=60,
)
build_dir = Path.cwd() / 'output'
ent_dir.insert(0, str(build_dir))
# ent_dir.grid(row=0, column=1, sticky='nsew', pady=5, padx=5)
# btn_choose.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
# btn_save.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
ent_dir.pack()
btn_choose.pack()
btn_save.pack()
window.mainloop()
