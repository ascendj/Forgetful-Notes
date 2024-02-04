from .base import ObservableModel

class Forget(ObservableModel):
    def __init__(self):
        super().__init__()
        self.auto_forget = False
        self.forget_on = False
        self.data = ""

    def on_forget(self) -> None:
        if self.forget_on:
            print("forgetting")