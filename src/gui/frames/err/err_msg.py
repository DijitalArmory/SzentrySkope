import customtkinter
from constants.constants import (
    PADY_1, NSEW, PADX_1
)

class ErrMsgWindow(customtkinter.CTkToplevel):
    def __init__(self, name=None, msg=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.grid(self, row=1, column=3, padx=(PADX_1, 20), pady=(PADY_1, 0), sticky=NSEW)

        self.name = msg = msg

        self.label = customtkinter.CTkLabel(self)
        self.label.configure(title=self.name, text=self.msg)
        self.label.pack(padx=20, pady=20)

    
    def open_err_msg_window(self, name, msg):
        self.name = name
        self.msg = msg
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ErrMsgWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it