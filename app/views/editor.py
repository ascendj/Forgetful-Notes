from customtkinter import *
from tkinter import Text
from tkhtmlview import HTMLLabel

class EditorView(CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar_frame = CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = CTkLabel(self.sidebar_frame, text="Forgetful Notes", font=CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.load_button = CTkButton(self.sidebar_frame, text="Load Note", font=CTkFont(size=18))
        self.load_button.grid(row=1, column=0, padx=20, pady=10)
        self.save_button = CTkButton(self.sidebar_frame, text="Save Note", font=CTkFont(size=18))
        self.save_button.grid(row=2, column=0, padx=20, pady=10)
        self.new_button = CTkButton(self.sidebar_frame, text="New Note", font=CTkFont(size=18))
        self.new_button.grid(row=3, column=0, padx=20, pady=10)
        self.file_label = CTkLabel(self.sidebar_frame, text="Untitled Note", font=CTkFont(size=20, weight="bold"))
        self.file_label.grid(row=4, column=0, padx=20, pady=10)
        
        self.appearance_mode_label = CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"])
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"])
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # self.text_box = CTkEntry(self, placeholder_text="CTkEntry")
        # self.text_box.grid(row=3, column=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.forget_button = CTkButton(text="Start Forgetting", master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.forget_button.grid(row=3, column=1, rowspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.reveal_button = CTkButton(text="Reveal Differences", master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.reveal_button.grid(row=3, column=2, rowspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.textbox = Text(self, font=CTkFont(size=18), wrap="word")
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.outputbox = HTMLLabel(
            self, width="1", background="white", html=
            """
            <h1>Forgetful Notes</h1>
            <p>Your notes, misremembered</p>
            <h2>Getting Started</h2>
            <ul>
            <li>To get started, simply start typing in the <strong>source text editor</strong> to the left of this</li>
            <li>This app supports Markdown, and you can see your notes rendered in real-time on this window</li>
            </ul>
            <h2>Not Your Ordinary Note-taking App</h2>
            <ul>
            <li>This app can be <strong>forgetful</strong>, and you'll need to remember what you wrote!</li>
            <li>By filling in forgotten words, you'll encourage active recall and better memorisation of what you write here </li>
            </ul>

            <em>This startup page disappears when you start typing</em>

            """, )
        self.outputbox.grid(row=0, column=2, padx=(20, 20), columnspan=2, pady=(20, 20), sticky="nsew")

        self.settings_frame = CTkFrame(self, fg_color="transparent")
        self.settings_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.settings_frame.grid_columnconfigure(0, weight=1)
        self.settings_frame.grid_rowconfigure(4, weight=1)
        self.settings_label = CTkLabel(self.settings_frame, text="Forgetfulness Mode", font=CTkFont(size=18))
        self.settings_label.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.seg_button = CTkSegmentedButton(self.settings_frame, values=["RAKE NLP", "GPT-3.5 Blanks", "GPT-3.5 Incorrects"])
        self.seg_button.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure(2, weight=1)

        # self.grid_rowconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=1)
        # self.grid_rowconfigure(2, weight=3)
        # self.grid_rowconfigure(3, weight=1)
        
        # self.header = CTkLabel(self, text="Untitled Note", font=("Roboto", 20))
        # self.header.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        # self.load_button = CTkButton(self, text="Load File", font=("Roboto", 16))
        # self.load_button.grid(row=1, column=0, padx=5, pady=10, sticky="ew")

        # self.save_button = CTkButton(self, text="Save File", font=("Roboto", 16))
        # self.save_button.grid(row=1, column=1, padx=5, pady=10, sticky="ew")
        
        # self.settings_button = CTkButton(self, text="Settings", font=("Roboto", 16))
        # self.settings_button.grid(row=1, column=2, padx=5, pady=10, sticky="ew")
        
        # self.text_box = CTkTextbox(self, font=("Roboto", 20), wrap="word")
        # self.text_box.grid(row=2, column=0, columnspan=3, padx=10, sticky="nsew")

        # self.forget_button = CTkButton(self, text="Start Forgetting", font=("Roboto", 16))
        # self.forget_button.grid(row=3, column=0, padx=5, pady=10, sticky="ew")

        # self.username_label = CTkLabel(self, text="Username")
        # self.username_input = CTkEntry(self)
        # self.username_label.grid(row=1, column=0, padx=10, sticky="w")
        # self.username_input.grid(row=1, column=1, padx=(0, 20), sticky="ew")

        # self.password_label = CTkLabel(self, text="Password")
        # self.password_input = CTkEntry(self, show="*")
        # self.password_label.grid(row=2, column=0, padx=10, sticky="w")
        # self.password_input.grid(row=2, column=1, padx=(0, 20), sticky="ew")

        # self.signin_btn = CTkButton(self, text="Sign In")
        # self.signin_btn.grid(row=3, column=1, padx=0, pady=10, sticky="w")

        # self.signup_option_label = CTkLabel(self, text="Don't have an account?")
        # self.signup_btn = CTkButton(self, text="Sign Up")
        # self.signup_option_label.grid(row=4, column=1, sticky="w")
        # self.signup_btn.grid(row=5, column=1, sticky="w")
