import tkinter as tk
from utils import create_new_window, open_archived_notes_window
from params import *

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Window")
        self.geometry(window_size) 

        self.title_label = tk.Label(self, text="Notebook", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        self.button1 = tk.Button(self, text="Take Notes", command=lambda: create_new_window("Take Notes", self))
        self.button1.pack(pady=10)

        self.button2 = tk.Button(self, text="Archived Notes", command=lambda: open_archived_notes_window(self))
        self.button2.pack(pady=10)

        self.button3 = tk.Button(self, text="Page3", command=lambda: create_new_window("Page3", self))
        self.button3.pack(pady=10)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
