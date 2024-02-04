from customtkinter import *

class SignUpView(CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.header = CTkLabel(self, text="Create a new account")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.fullname_label = CTkLabel(self, text="Full Name")
        self.fullname_input = CTkEntry(self)
        self.fullname_label.grid(row=1, column=0, padx=10, sticky="w")
        self.fullname_input.grid(row=1, column=1, padx=(0, 20), sticky="ew")

        self.username_label = CTkLabel(self, text="Username")
        self.username_input = CTkEntry(self)
        self.username_label.grid(row=2, column=0, padx=10, sticky="w")
        self.username_input.grid(row=2, column=1, padx=(0, 20), sticky="ew")

        self.password_label = CTkLabel(self, text="Password")
        self.password_input = CTkEntry(self, show="*")
        self.password_label.grid(row=3, column=0, padx=10, sticky="w")
        self.password_input.grid(row=3, column=1, padx=(0, 20), sticky="ew")

        self.has_agreed = BooleanVar()
        self.agreement = CTkCheckBox(
            self,
            text="I've agreed to the Terms & Conditions",
            variable=self.has_agreed,
            onvalue=True,
            offvalue=False,
        )
        self.agreement.grid(row=4, column=1, padx=0, sticky="w")

        self.signup_btn = CTkButton(self, text="Sign Up")
        self.signup_btn.grid(row=5, column=1, padx=0, pady=10, sticky="w")

        self.signin_option_label = CTkLabel(self, text="Already have an account?")
        self.signin_btn = CTkButton(self, text="Sign In")
        self.signin_option_label.grid(row=6, column=1, sticky="w")
        self.signin_btn.grid(row=7, column=1, sticky="w")
