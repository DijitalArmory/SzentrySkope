import customtkinter
import os
from PIL import Image
from constants.constants import (
    W
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
        checkbox = customtkinter.CTkCheckBox(self, text=item, command=self.checkbox_command)
        checkbox.grid(row=len(self.checkbox_list), column=0, pady=(0, 10), sticky=W)
        self.checkbox_list.append(checkbox)

    def checkbox_command(self):
        if self.command is not None:
            self.command()

    def remove_item(self, item):
        for checkbox in self.checkbox_list:
            if item == checkbox.cget("text"):
                checkbox.destroy()
                self.checkbox_list.remove(checkbox)
                return

    def get_checked_items(self):
        return [checkbox.cget("text") for checkbox in self.checkbox_list if checkbox.get() == 1]