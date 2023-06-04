import customtkinter
import sys
import traceback
from data.net_scan_data import (
    ipv4_info_keys, ipv4_info_values, ipv6_info_keys, ipv6_info_values, 
    nic_info_keys, nic_info_values, calculate_network_address
)
import tkinter
from constants.constants import (
    CORNER_RADIUS_0, GRID_ROW_2, GRID_COL_2, PADY_1, PADX_1, NSEW, PADX_2,
    PADY_2, PADX_1, N
)

sys.path.append('/home/cybershield/SzentrySkope/src/data/')
from data.ifaces import ifaces

sys.path.append('/home/cybershield/SzentrySkope/src/gui/frames/err')
from err.err_msg import ErrMsg


class HostOptionsBox(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=0, column=3, padx=(PADX_1, 20),
                  pady=(PADY_1, 0), sticky=NSEW)
        self.localhost = ipv4_info_values[0]()
        self.ip4 = ipv4_info_values[1](ifaces, 'addr', '4')
        self.ip4_mask = ipv4_info_values[2](ifaces, 'netmask', '4')
        self.net_addr = ipv4_info_values[4](self.ip4, self.ip4_mask)

        # styling config
        self._corner_radius = CORNER_RADIUS_0

        self.previous_selection = ""

        self.radio_var = tkinter.IntVar(value=0)

        self.label_radio_group = customtkinter.CTkLabel(self,  text="Hosts")
        self.label_radio_group.grid(
            row=0, column=2, columnspan=1, padx=PADX_2, pady=PADY_2, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(
            self, text="Localhost", variable=self.radio_var, value=0, command=self.toggle_button_text)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")        
        self.radio_button_2 = customtkinter.CTkRadioButton(
            self, text="All Hosts", variable=self.radio_var, value=1, command=self.toggle_button_text)
        self.radio_button_2.grid(
            row=GRID_ROW_2, column=GRID_COL_2, pady=PADY_2, padx=PADX_1, sticky=N)
        self.radio_button_3 = customtkinter.CTkRadioButton(
            self, text="Manual", variable=self.radio_var, value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        self.entry_start = customtkinter.CTkEntry(
            self, placeholder_text="From...", textvariable=self.start_value)
        self.entry_start.grid(row=4, column=2, columnspan=1, padx=(
            10, 10), pady=(10, 10), sticky="nsew")
        self.entry_end = customtkinter.CTkEntry(
            self, placeholder_text="To...", textvariable=self.end_value)
        self.entry_end.grid(row=5, column=2, columnspan=1,
                            padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.submit_button = customtkinter.CTkButton(
            self, text="submit", command=self.submit_button_event)
        self.submit_button.grid(row=6, column=2, columnspan=1, padx=(
            10, 10), pady=(10, 10), sticky="nsew")

        self.entry_start.configure(state=tkinter.DISABLED)
        self.entry_end.configure(state=tkinter.DISABLED)
        self.submit_button.configure(state=tkinter.DISABLED)  


    def toggle_button_text(self):
        self.current_selection = self.radio_var.get()
        if self.radio_var.get() == 0:  # Localhost selected
            self.radio_button_1.configure(text=self.localhost)
        elif self.radio_var.get() == 1:  # Localhost selected
            self.radio_button_2.configure(text=self.net_addr)

        self.previous_selection = self.current_selection


    def submit_button_event(self):
        self.start_input = self.start_value.get()
        self.end_input = self.end_value.get()
        
        try:
            self.start_value = int(self.start_input)
            self.end_value = int(self.end_input)
            
            if 1 <= self.start_value <= 65535 and 1 <= self.end_value <= 65535 and self.start_value < self.end_value:
                self.start_value = self.start_value
                self.end_value = self.end_value
                # Use the start_value and end_value as needed
                print("Start value:", self.start_value)
                print("End value:", self.end_value)
                self.args_list = [f"-p {str(self.start_value)}-{str(self.end_value)}"]
                print(self.args_list)
                self.command(self.args_list)
                self.reset_instance()
            
            else:
                self.err1 = ErrMsg(message="Invalid input values. Please enter integers between 1 and 65535, with the start value less than the end value.\nPort settings being reset back to default settings")
                self.reset_instance()  # Reset instance on error

        except ValueError as e:
            self.err2 = ErrMsg(message="Invalid input values. No characters Allowed. Only integers between 1-65535\nPort settings being reset back to default settings")
            self.reset_instance()  # Reset instance on error
        except Exception as e:
            print("An error occurred:", str(e))
            traceback.print_exc()  # Print the traceback for debugging
            self.reset_instance()  # Reset instance on error



'''
NOTE - Leftoff; entry fields need logic
6/4/23
'''


'''
NOTE - using these method initializations as ref

ip4_addr = ip_data(ifaces, 'addr', '4')
print(ip4_addr)

ip4_mask = ip_data(ifaces, 'netmask', '4')
print(ip4_mask)

ip4_broadcast = ip_data(ifaces, 'broadcast', '4')
print(ip4_broadcast)

ip6_addr = ip_data(ifaces, 'addr', '6')
print(ip6_addr)

mac_addr = ip_data(ifaces, 'addr', 'mac')
print(mac_addr)

mac_broadcast = ip_data(ifaces, 'broadcast', 'mac')
print(mac_broadcast)

iface = get_iface(ifaces)
print(iface)

ip6_mask = get_ip6_mask()
print(ip6_mask)

localhost_ip = get_localhost_ip()
print("Localhost IP:", localhost_ip)
'''