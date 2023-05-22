import customtkinter
import tkinter
import os
from PIL import Image
from constants.constants import (
    W
)
from data.net_scan_data import (
    scan_techniques
) 


class ScanTechniquesBox(customtkinter.CTkScrollableFrame):
    def __init__(self, master, item_list, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.command = command
        self.grid(row=1, column=2, padx=(20, 0), pady=(20, 0))

        self.checkbox_list = []

        for i, item in enumerate(item_list):
            self.add_item(item)


    def add_item(self, item):
        var = tkinter.IntVar()
        self.checkbox = customtkinter.CTkCheckBox(self, text=item, variable=var,  command=self.checkbox_command)
        self.checkbox.grid(row=len(self.checkbox_list), column=0, pady=(0, 10), sticky=W)
        self.checkbox_list.append(self.checkbox)

    def checkbox_command(self):
        if self.command is not None:
            self.command()
    
            
    def remove_item(self, item):
        for checkbox in self.checkbox_list:
            if item == checkbox.cget("text"):
                checkbox.destroy()
                self.checkbox_list.remove(checkbox)
                return



    # Left OFF - 
    # TODO - the dictionary values need to print the key(s) of the checkbox(es)
    # when the checkbox(es) is/are clicked