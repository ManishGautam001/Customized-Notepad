from tkinter import *
from tkinter.filedialog import asksaveasfilename
import os
root = Tk()

def myfunc():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt',defaultextension='.txt',filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        f = open(file,"w")
        f.write(text.get(1.0, END))
        f.close()
        root.title(os.path.basename(file) + " - Notepad")



if __name__ == '__main__':
    text = Text(root, font='lucida 15')
    file = None
    text.pack(expand=True, fill=BOTH)
    mymenu = Menu(root)
    m1 = Menu(mymenu)
    m1.add_command(label="save", command=myfunc)
    m1.add_command(label="quit", command=quit)
    root.config(menu=mymenu)
    mymenu.add_cascade(label="file", menu=m1)

    root.mainloop()