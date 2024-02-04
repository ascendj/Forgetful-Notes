from models.main import Model
from views.main import View
from tkinter import filedialog, END
from markdown2 import Markdown
from tkhtmlview import HTMLLabel
import os.path

class EditorController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["editor"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.load_button.configure(command=self.load)
        self.frame.save_button.configure(command=self.save)
        self.frame.new_button.configure(command=self.new)
        self.frame.forget_button.configure(command=self.forget)
        self.frame.reveal_button.configure(command=self.reveal)
        self.frame.textbox.bind("<<Modified>>", self.on_input_change)
        self.frame.seg_button.configure(command=self.mode)
        self.sure = False
        # self.frame.signin_btn.configure(command=self.signin)
        # self.frame.signup_btn.configure(command=self.signup)
    def mode(self, value) -> None:
        self.model.forget.mode = value
    
    def load(self) -> None:
        file_path = filedialog.askopenfilename(title="Open a Note", filetypes=[("Markdown files", "*.md"), ("Text files", "*.txt"), ("All files", "*.*")])

        if file_path:
            self.frame.textbox.delete('1.0', END)
            self.frame.textbox.insert('1.0', open(file_path, "r").read())
            self.frame.file_label.configure(text=os.path.basename(file_path))
    
    def save(self) -> None:
        file_path = filedialog.asksaveasfilename(title="Save file to", filetypes=[("Markdown files", "*.md"), ("Text files", "*.txt"), ("All files", "*.*")])

        if file_path:
            open(file_path, "w").write(self.frame.textbox.get('1.0', END))
            self.frame.file_label.configure(text=os.path.basename(file_path))
    
    def forget(self) -> None:
        self.model.forget.forget_on = not self.model.forget.forget_on

        if self.model.forget.forget_on:
            self.frame.forget_button.configure(text="Disable Forgetfulness")
            self.view.root.after(5000, self.update_forget)
        else:
            self.frame.forget_button.configure(text="Enable Forgetfulness")
    
        
        if self.model.forget.reverted and self.model.forget.revealed:
            self.model.forget.original = self.frame.textbox.get('1.0', END)

    def update_forget(self) -> None:
        modified_text = self.model.forget.on_forget(self.frame.textbox.get('1.0', END))
        self.frame.textbox.delete('1.0', END)
        self.frame.textbox.insert('1.0', modified_text)
        self.forget()

    def on_input_change(self, event=None):
        self.frame.textbox.edit_modified(0)
        md2html = Markdown()
        markdownText = self.frame.textbox.get('1.0', END)
        html = md2html.convert(markdownText)
        self.frame.outputbox.set_html(html)

    def new(self):
        if self.sure:
            self.frame.textbox.delete('1.0', END)
            self.frame.file_label.configure(text="Untitled Note")
            self.frame.new_button.configure(text="New Note")
            self.sure = False
        else:
            self.frame.new_button.configure(text="Are you sure?")
            self.sure = True
    
    def reveal(self):
        if self.model.forget.revealed:
            if not self.model.forget.reverted:
                self.model.forget.reverted = True
                self.frame.textbox.delete('1.0', END)
                self.frame.textbox.insert('1.0', self.model.forget.on_revert())
                self.frame.reveal_button.configure(text="Reveal Differences")
        else:
            self.model.forget.revealed = True
            revealed_text = self.model.forget.on_reveal(self.frame.textbox.get('1.0', END))
            self.frame.textbox.delete('1.0', END)
            self.frame.textbox.insert('1.0', revealed_text)
            self.frame.reveal_button.configure(text="Revert to Original Text")

        
    # def signup(self) -> None:
        # self.view.switch("signup")

    # def signin(self) -> None:
    #     username = self.frame.username_input.get()
    #     pasword = self.frame.password_input.get()
    #     data = {"username": username, "password": pasword}
    #     print(data)
    #     self.frame.password_input.delete(0, last=len(pasword))
    #     user: User = {"username": data["username"]}
    #     self.model.auth.login(user)
