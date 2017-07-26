# coding: utf-8
from tkinter.filedialog import *
from tkinter.messagebox import *

import nltk


def load_text():
    op = askopenfilename()
    return work_text(op)


def work_text(op):
    f = open(op, 'r')
    text = f.read()
    txt.insert(END, text)
    f.close()
    words = nltk.word_tokenize(text.lower())
    w = [w for w in words if w.isalpha()]
    result = nltk.pos_tag(w)
    txt1.insert(END, result)


def save_file():
    save_as = asksaveasfilename()
    try:
        x = txt1.get(1.0, END)
        f = open(save_as, "w")
        f.writelines(x)
        f.close()
    except:
        pass


def clear_text():
    txt.delete(1.0, END)
    txt1.delete(1.0, END)


def close_win():
    if askyesno("Exit", "Do you want to quit?"):
        tk.destroy()


tk = Tk()
main_menu = Menu(tk)
tk.config(menu=main_menu)
file_menu = Menu(main_menu)
main_menu.add_cascade(label="Menu", menu=file_menu)
file_menu.add_command(label="English text", command=load_text)
file_menu.add_command(label="Save file", command=save_file)
file_menu.add_command(label="To clear the text", command=clear_text)
file_menu.add_command(label="Exit", command=close_win)
txt = Text(tk, width=72, height=10, font="Arial 12", wrap=WORD)
txt.pack()
txt1 = Text(tk, width=72, height=10, font="Arial 12", wrap=WORD)
txt1.pack()
tk.mainloop()
