from tkinter import Tk, Button, Label, Frame, Canvas, BOTH, VERTICAL, RIGHT, LEFT, Y, ttk
from api import Api
import os

class Interface(Tk) :
    def __init__(self) :
        super().__init__()
        self.api = Api()
        self.geometry("800x600")
        self.PATH = os.path.dirname(os.path.dirname(__file__)) + "\\todoapp2\\static\\media\\"

        self.button = Button(self, text="Show All ToDos", padx=30, pady=20, command=self.show_todos)
        self.button.pack()

    def show_todos(self) :
        self.set_window()

        print("clicked")
        self.api.get_all_todos()
    def set_window(self):
        self.frame = Frame(self)
        self.frame.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self.frame)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.scroll_bar = ttk.Scrollbar(self.frame, orient=VERTICAL, command=self.canvas.yview)
        self.scroll_bar.pack(side=RIGHT, fill=Y)

        self.canvas.configure(yscrollcommand=self.scroll_bar.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.main_frame = Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.main_frame, anchor="nw")

        self.main_frame.bind("<Enter>", self.entered)
        self.main_frame.bind("<Leave>", self.left)
    def _on_mouse_wheel(self, event):
        self.canvas.yview_scroll(-1 * int((event.delta / 120)), "units")
    def entered(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)