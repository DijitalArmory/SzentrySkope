import customtkinter
import tkinter
from constants.constants import (
    CORNER_RADIUS_0, GRID_ROW_2, GRID_COL_2, PADY_1, PADX_1, NSEW, PADX_2, 
    PADY_2, PADX_1, N
)

class HostOptionsBox(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=0, column=3, padx=(PADX_1, 20), pady=(PADY_1, 0), sticky=NSEW)

        # styling config
        self._corner_radius = CORNER_RADIUS_0

        self.radio_var = tkinter.IntVar(value=0)

        self.label_radio_group = customtkinter.CTkLabel(self,  text="Hosts")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=PADX_2, pady=PADY_2, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(self, text="Localhost", variable=self.radio_var, value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(self, text="All Hosts", variable=self.radio_var, value=1)
        self.radio_button_2.grid(row=GRID_ROW_2, column=GRID_COL_2, pady=PADY_2, padx=PADX_1, sticky=N)
        self.radio_button_3 = customtkinter.CTkRadioButton(self, text="Manual", variable=self.radio_var, value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        self.entry_start = customtkinter.CTkEntry(self, placeholder_text="From...", textvariable=None)
        self.entry_start.grid(row=4, column=2, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.entry_end = customtkinter.CTkEntry(self, placeholder_text="To...", textvariable=None)
        self.entry_end.grid(row=5, column=2, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.submit_button = customtkinter.CTkButton(self, text="submit", command=None) 
        self.submit_button.grid(row=6, column=2, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.entry_start.configure(state=tkinter.DISABLED)
        self.entry_end.configure(state=tkinter.DISABLED)
        self.submit_button.configure(state=tkinter.DISABLED)