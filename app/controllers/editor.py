from models.main import Model
from models.auth import User
from views.main import View
from tkinter import filedialog, END
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
        # self.frame.signin_btn.configure(command=self.signin)
        # self.frame.signup_btn.configure(command=self.signup)

    def load(self) -> None:
        file_path = filedialog.askopenfilename(title="Open a Note", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

        if file_path:
            self.frame.text_box.delete('1.0', END)
            self.frame.text_box.insert('1.0', open(file_path, "r").read())
            self.frame.header.configure(text=os.path.basename(file_path))
    
    def save(self) -> None:
        file_path = filedialog.asksaveasfilename(title="Save file to", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

        if file_path:
            open(file_path, "w").write(self.frame.text_box.get('1.0', END))
            self.frame.header.configure(text=os.path.basename(file_path))
    
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
