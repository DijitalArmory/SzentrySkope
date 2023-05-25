import customtkinter
import tkinter
from constants.constants import (
    CORNER_RADIUS_0, GRID_ROW_2, GRID_COL_2, PADY_1, PADX_1, NSEW, PADX_2, 
    PADY_2, PADX_1, N
)
from data.net_scan_data import scan_ports


class PortOptionsBox(customtkinter.CTkFrame):
    def __init__(self, master, args_list=None, command=None):
        super().__init__(master)

        self.grid(row=1, column=3, padx=(PADX_1, 20), pady=(PADY_1, 0), sticky=NSEW)

        # styling config
        self._corner_radius = CORNER_RADIUS_0

        # setup port variables key/value pairs
        self.port_opt_len = len(scan_ports)
        self.kp_0 = self.port_opt_len - 3
        self.kp_1 = self.port_opt_len - 2
        self.kp_2 = self.port_opt_len - 1

        self.first_key, self.first_value = list(scan_ports.items())[self.kp_0]
        self.second_key, self.second_value = list(scan_ports.items())[self.kp_1]
        self.third_key, self.third_value = list(scan_ports.items())[self.kp_2]

        # init args
        self.args_list = args_list if args_list is not None else [] # list to append selected radiobtn value to
        self.command = command

        self.radio_var = tkinter.IntVar(value=0)

        self.label_radio_group = customtkinter.CTkLabel(self,  text="Port Range")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=PADX_2, pady=PADY_2, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(self, text=self.first_key, variable=self.radio_var, value=0, command=self.radio_button_command)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(self, text=self.second_key, variable=self.radio_var, value=1,command=self.radio_button_command)
        self.radio_button_2.grid(row=GRID_ROW_2, column=GRID_COL_2, pady=PADY_2, padx=PADX_1, sticky=N)
        self.radio_button_3 = customtkinter.CTkRadioButton(self, text=self.third_key, variable=self.radio_var, value=2,command=self.radio_button_command)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        self.entry_start = customtkinter.CTkEntry(self, placeholder_text="From...", state=tkinter.DISABLED)
        self.entry_start.grid(row=4, column=2, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.entry_end = customtkinter.CTkEntry(self, placeholder_text="To...", state=tkinter.DISABLED)
        self.entry_end.grid(row=5, column=2, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")



    def radio_button_command(self):
        if self.command is not None:
            self.selected_value = self.radio_var.get()  # Get the selected radio button value
            if self.selected_value == 0:
                self.args_list = self.first_value  # Example value for the first radio button
                print(self.first_value)
            elif self.selected_value == 1:
                self.args_list = self.second_value  # Example value for the second radio button
                print(self.second_value)
            elif self.selected_value == 2:
                # Example implementation for manual entry
                start = int(self.entry_start.get())
                end = int(self.entry_end.get())
                self.args_list = list(range(start, end + 1))
            self.args_list.append(self.selected_value)
            print(self.args_list)  # Print the updated list for testing purposes
            self.update_radio_button_args_list()
            self.command()

    def update_radio_button_args_list(self):
        self.master.port_button_args_list = self.args_list


'''
class PortOptionsBox(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=1, column=3, padx=(PADX_1, 20), pady=(PADY_1, 0), sticky=NSEW)

        # styling config
        self._corner_radius = CORNER_RADIUS_0

        # setup port variables key/value pairs
        self.port_opt_len = len(scan_ports)
        self.kp_0 = self.port_opt_len - 3
        self.kp_1 = self.port_opt_len - 2
        self.kp_2 = self.port_opt_len - 1

        self.first_key, self.first_value = list(scan_ports.items())[self.kp_0]
        self.second_key, self.second_value = list(scan_ports.items())[self.kp_1]
        self.third_key, self.third_value = list(scan_ports.items())[self.kp_2]

        
        self.args_list = [] # list to append selected radiobtn value to

        self.radio_var = tkinter.IntVar(value=0)

        self.label_radio_group = customtkinter.CTkLabel(self,  text="Port Range")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=PADX_2, pady=PADY_2, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(self, text=self.first_key, variable=self.radio_var, value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(self, text=self.second_key, variable=self.radio_var, value=1)
        self.radio_button_2.grid(row=GRID_ROW_2, column=GRID_COL_2, pady=PADY_2, padx=PADX_1, sticky=N)
        self.radio_button_3 = customtkinter.CTkRadioButton(self, text=self.third_key, variable=self.radio_var, value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        self.entry_start = customtkinter.CTkEntry(self, placeholder_text="From...", state=tkinter.DISABLED)
        self.entry_start.grid(row=4, column=2, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.entry_end = customtkinter.CTkEntry(self, placeholder_text="To...", state=tkinter.DISABLED)
        self.entry_end.grid(row=5, column=2, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")



        def radio_button_command(self):
            self.selected_value = self.radio_var.get()  # Get the selected radio button value
            if self.selected_value == 0:
                self.args_list = self.first_value  # Example value for the first radio button
                print(self.first_value)
            elif self.selected_value == 1:
                self.args_list = self.second_value  # Example value for the second radio button
                print(self.second_value)
            elif self.selected_value == 2:
                # Example implementation for manual entry
                start = int(self.entry_start.get())
                end = int(self.entry_end.get())
                self.args_list = list(range(start, end + 1))
            self.args_list.append(self.selected_value)
            print(self.args_list)  # Print the updated list for testing purposes'''