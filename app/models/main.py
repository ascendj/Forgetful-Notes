from .auth import Auth
from .forget import Forget

class Model:
    def __init__(self):
        self.auth = Auth()
        self.forget = Forget()
        
