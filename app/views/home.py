from customtkinter import *


class HomeView(CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.header = CTkLabel(self, text="Home")
        self.header.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.greeting = CTkLabel(self, text="")
        self.greeting.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.signout_btn = CTkButton(self, text="Sign Out")
        self.signout_btn.grid(row=2, column=0, padx=10, pady=10)
