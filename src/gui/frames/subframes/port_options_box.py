import customtkinter
import tkinter
import sys

from constants.constants import (
    CORNER_RADIUS_0, GRID_ROW_2, GRID_COL_2, PADY_1, PADX_1, NSEW, PADX_2, 
    PADY_2, PADX_1, N
)
from data.net_scan_data import scan_ports
sys.path.append('/home/cybershield/SzentrySkope/src/gui/frames/')
import err.err_msg

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

        

        # init args
        self.args_list = []
        self.toplevel_window = None # err msg handler
        self.entry_start = None
        self.entry_end = None
        self.submit_button = None
        self.previous_selection = ""
        self.created_widgets  = []
        
        # set default selected value for radio buttons
        self.radio_var = tkinter.StringVar(value=self.first_value)

        self.label_radio_group = customtkinter.CTkLabel(self,  text="Port Range")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=PADX_2, pady=PADY_2, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(self, text=self.first_key, variable=self.radio_var, value=self.first_value, command=self.radio_button_command)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n",columnspan=1)
        self.radio_button_2 = customtkinter.CTkRadioButton(self, text=self.second_key, variable=self.radio_var, value=self.second_value, command=self.radio_button_command)
        self.radio_button_2.grid(row=GRID_ROW_2, column=GRID_COL_2, pady=PADY_2, padx=PADX_1, sticky=N,columnspan=1)
        self.radio_button_3 = customtkinter.CTkRadioButton(self, text=self.third_key, variable=self.radio_var, value=self.third_value, command=self.enable_entry_fields)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n", columnspan=1)

        self.start_value = tkinter.StringVar()
        self.end_value = tkinter.StringVar()

        self.entry_start = customtkinter.CTkEntry(self, placeholder_text="From...", state = tkinter.DISABLED, textvariable=self.start_value)
        self.entry_start.grid(row=4, column=2, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.entry_end = customtkinter.CTkEntry(self, placeholder_text="To...", state = tkinter.DISABLED, textvariable=self.end_value)
        self.entry_end.grid(row=5, column=2, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.submit_button = customtkinter.CTkButton(self, text="submit", state = tkinter.DISABLED, command=None) 
        self.submit_button.grid(row=6, column=2, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")


    def radio_button_command(self):
        self.current_selection = self.radio_var.get()  # Get the selected radio button value
        if self.current_selection != self.previous_selection:

            if self.current_selection == self.first_value:
                self.args_list = [self.first_value]
                print(self.first_value, " type ", type(self.first_value))
                     
                
            elif self.current_selection == self.second_value:
                self.args_list = [self.second_value]
                print(self.second_value, " type ", type(self.second_value))

            elif self.current_selection == self.third_value:
                print(self.third_value, " type ", type(self.third_value))
            

            self.previous_selection = self.current_selection
        else: 
            if self.current_selection != "Option 3":
                self.remove_entry_fields()

        print(self.args_list)



    def remove_entry_fields(self):
        
        if  self.entry_start is not None:
            self.entry_start.destroy()
            self.entry_start = None

        if  self.entry_end is not None:
            self.entry_end.destroy()
            self.entry_end = None

        if self.submit_button is not None:
           self.submit_button.destroy()
           self.submit_button= None

    
    def enable_entry_fields(self):
        self.start_value = tkinter.StringVar()
        self.end_value = tkinter.StringVar()
        
        self.entry_start = customtkinter.CTkEntry(self, placeholder_text="From...", textvariable=self.start_value)
        self.entry_start.grid(row=4, column=2, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.entry_end = customtkinter.CTkEntry(self, placeholder_text="To...", textvariable=self.end_value)
        self.entry_end.grid(row=5, column=2, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.submit_button = customtkinter.CTkButton(self, text="submit", command=None) 
        self.submit_button.grid(row=6, column=2, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")


