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
    def __init__(self, master, args_list, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.command = command
        self.grid(row=1, column=2, padx=(20, 0), pady=(20, 0))

        self.item_list = list(scan_techniques.keys())
        self.other_list = list(scan_techniques.values())
        self.checkbox_list = [] # gui - displays keys()
        self.args_list = args_list  # command args list 

        for i, item in enumerate(self.item_list):
            self.add_item(item, self.other_list[i])

    def add_item(self, item, other_value):
        var = tkinter.StringVar()
        var.set(other_value)

        self.checkbox = customtkinter.CTkCheckBox(self, text=item, variable=var, onvalue=1, offvalue=0,
                                                  command=lambda value=var.get(): self.checkbox_command(value))
        self.checkbox.grid(row=len(self.checkbox_list), column=0, pady=(0, 10), sticky='w')
        self.checkbox_list.append(self.checkbox)

    
    # load scan technique args
    def checkbox_command(self, value):
        on_value = self.checkbox._onvalue
        off_value = self.checkbox._offvalue
        index = self.other_list.index(value)
        xindex = self.other_list[index]
        if on_value == 1:
            if xindex not in self.args_list:
                self.args_list.append(xindex)
                print("LIST ", self.args_list, "VALUE ", value)
                return value
                
        elif off_value == 0:  # Modified condition to check if off_value is true
            if xindex in self.args_list:
                self.args_list.remove(xindex)
                print("LIST ", self.args_list, "VALUE ", value)
                return value





    



