from customtkinter import *

class Root(CTk):
    def __init__(self):
        
        super().__init__()

        start_width = 1000
        min_width = 400
        start_height = 800
        min_height = 800

        self.geometry(f"{start_width}x{start_height}")
        self.attributes('-fullscreen', True)
        self.minsize(width=min_width, height=min_height)
        self.title("Forgetful Notes")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        set_appearance_mode("light")  # Modes: system (default), light, dark
        set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
