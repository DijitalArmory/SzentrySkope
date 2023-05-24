from constants.net_scan_commands import (
    SCAN_INIT
)


class ArgsHandler:
    def __init__(self, command=None, checkbox_args_list=None):
           
        self.checkbox_args_list = checkbox_args_list if checkbox_args_list is not None else []
    
    def update_checkbox_args_list(self, new_args_list):
        self.checkbox_args_list = new_args_list
        print("Updated checkbox_args_list in ArgsHandler:", self.checkbox_args_list)