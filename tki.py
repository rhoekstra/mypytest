#!/usr/local/bin/python3
"""This is our tutorial on tkinter."""
import tkinter
from PIL import Image, ImageTk
import os
my_path = os.path.abspath(os.path.dirname(__file__))


class Window(tkinter.Frame):
    """This is the main window class."""

    def __init__(self, master=None):
        """Do something useful."""
        tkinter.Frame.__init__(self, master)

        self.master = master
        self.init_window()

    def init_window(self):
        """Initialize window."""
        self.master.title("GUI")

        self.pack(fill=tkinter.BOTH, expand=1)
        # quitButton = Button(self, text="Quit", command=self.client_exit)
        # quitButton.place(x=0,y=0)
        self.load_menus()

    def load_menus(self):
        """Load the menus here."""
        menu = tkinter.Menu(self.master)
        self.master.config(menu=menu)
        file = tkinter.Menu(menu)
        file.add_command(label='Save', command=self.showTxt)
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        edit = tkinter.Menu(menu)
        edit.add_command(label='Show Image', command=self.showImg)
        edit.add_command(label='Show Text', command=self.showTxt)
        menu.add_cascade(label='Edit', menu=edit)

    def showImg(self):
        """Show an image."""
        load = Image.open(os.path.join(my_path, "images", "img.jpg"))
        photo = ImageTk.PhotoImage(load)

        # labels can be text or images
        label = tkinter.Label(self, image=photo)
        label.image = photo
        # img.place(x=0, y=0)
        label.place()

    def showTxt(self):
        """Show some Text."""
        text = tkinter.Label(self, text="My current working dir is " +
                             os.getcwd())
        text.pack()

    def client_exit(self):
        """Exit the program."""
        exit()

    def warn_me(self):
        """Warn user about something."""
        pass


root = tkinter.Tk()

root.geometry("800x600")

app = Window(root)

root.mainloop()
