#!/usr/local/bin/python3
"""This is our tutorial on tkinter."""
from tkinter import Frame, Menu, BOTH, Tk, Label
from PIL import Image, ImageTk
import os
my_path = os.path.abspath(os.path.dirname(__file__))


class Window(Frame):
    """This is the main window class."""

    def __init__(self, master=None):
        """Do something useful."""
        Frame.__init__(self, master)

        self.master = master
        self.init_window()

    def init_window(self):
        """Initialize window."""
        self.master.title("GUI")

        self.pack(fill=BOTH, expand=1)
        # quitButton = Button(self, text="Quit", command=self.client_exit)
        # quitButton.place(x=0,y=0)

        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label='Save', command=self.showTxt)
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        edit = Menu(menu)
        edit.add_command(label='Show Image', command=self.showImg)
        edit.add_command(label='Show Text', command=self.showTxt)
        menu.add_cascade(label='Edit', menu=edit)

    def showImg(self):
        """Show some image."""
        load = Image.open(os.path.join(my_path, "images", "googlelogo.png"))
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def showTxt(self):
        """Show some Text."""
        text = Label(self, text="My current working dir is "+os.getcwd())
        text.pack()

    def client_exit(self):
        """Exit the program."""
        exit()

    def warn_me(self):
        """Warn user about something."""
        pass


root = Tk()

root.geometry("800x600")

app = Window(root)

root.mainloop()
