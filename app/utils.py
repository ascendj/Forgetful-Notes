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
    prev_window.quit() 

def fetch_archived_file_names(window, folder_path=archived_folder_path):
    for file in os.listdir(folder_path):
        if file.endswith('.txt'):
            file_button = tk.Button(window, text=file, command=lambda f=file: archived_file_action(f, window))
            file_button.pack(pady=10)

def archived_file_action(file_name, current_window):
    file_path = os.path.join(archived_folder_path, file_name)

    with open(file_path, 'r') as file:
        file_content = file.read()

    create_new_window(file_name, current_window, lambda window: populate_with_file_content(window, file_content))

def populate_with_file_content(window, content):
    text_widget = tk.Text(window)
    text_widget.insert(tk.END, content)
    text_widget.pack(expand=True, fill=tk.BOTH)
