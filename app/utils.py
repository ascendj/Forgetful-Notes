import tkinter as tk
from tkinter import Toplevel
from params import *
import os

def open_archived_notes_window(main_window):
    create_new_window('Archived Notes', main_window, fetch_archived_file_names)


def create_new_window(window_title, prev_window, populate_function=None):
    prev_window.withdraw()

    new_window = Toplevel()
    new_window.title(window_title)
    new_window.geometry(window_size) 

    new_window.protocol("WM_DELETE_WINDOW", lambda: on_close_windows(prev_window, new_window))

    if populate_function:
        populate_function(new_window)
    else:
      default_label = tk.Label(new_window, text="No specific content for this window.")
      default_label.pack()

    back_button = tk.Button(new_window, text='Back', command=lambda: go_back(prev_window, new_window))
    back_button.pack(pady=10)

    
def go_back(prev_window, current_window):
    current_window.destroy()
    prev_window.deiconify()

def on_close_windows(prev_window, new_window):
    new_window.destroy()
    prev_window.destroy() 

def fetch_archived_file_names(window, folder_path=archived_folder_path):
    for file in os.listdir(folder_path):
        if file.endswith('.txt'):
            file_button = tk.Button(window, text=file)
            file_button.pack()