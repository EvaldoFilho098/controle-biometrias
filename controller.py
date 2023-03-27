import tkinter as tk
from viewer import View
from model import Model


class Controller:
    def __init__(self):
        self.root = tk.Tk()
        self.model = Model()
        self.view = View(self.root)
        self.view.set_model(self.model)

    def run(self):
        self.root.mainloop()
