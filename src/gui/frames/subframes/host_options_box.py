import customtkinter
from data.net_scan_data import (
    ipv4_info_keys, ipv4_info_values, ipv6_info_keys, ipv6_info_values, 
    nic_info_keys, nic_info_values
)
import tkinter
from constants.constants import (
    CORNER_RADIUS_0, GRID_ROW_2, GRID_COL_2, PADY_1, PADX_1, NSEW, PADX_2,
    PADY_2, PADX_1, N
)


class HostOptionsBox(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=0, column=3, padx=(PADX_1, 20),
                  pady=(PADY_1, 0), sticky=NSEW)

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
            self, text="All Hosts", variable=self.radio_var, value=1)
        self.radio_button_2.grid(
            row=GRID_ROW_2, column=GRID_COL_2, pady=PADY_2, padx=PADX_1, sticky=N)
        self.radio_button_3 = customtkinter.CTkRadioButton(
            self, text="Manual", variable=self.radio_var, value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        self.entry_start = customtkinter.CTkEntry(
            self, placeholder_text="From...", textvariable=None)
        self.entry_start.grid(row=4, column=2, columnspan=1, padx=(
            10, 10), pady=(10, 10), sticky="nsew")
        self.entry_end = customtkinter.CTkEntry(
            self, placeholder_text="To...", textvariable=None)
        self.entry_end.grid(row=5, column=2, columnspan=1,
                            padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.submit_button = customtkinter.CTkButton(
            self, text="submit", command=None)
        self.submit_button.grid(row=6, column=2, columnspan=1, padx=(
            10, 10), pady=(10, 10), sticky="nsew")

        self.entry_start.configure(state=tkinter.DISABLED)
        self.entry_end.configure(state=tkinter.DISABLED)
        self.submit_button.configure(state=tkinter.DISABLED)  


    def toggle_button_text(self):
        self.current_selection = self.radio_var.get()
        if self.radio_var.get() == 0:  # Localhost selected
            self.radio_button_1.configure(text=ipv4_info_values[0]())
        else:
            self.radio_button_1.configure(text=ipv4_info_keys[0]())

        self.previous_selection = self.current_selection



'''
NOTE - LEFTOFF 
TODO - toggle radio buttons to display the data back and forth in gui labels
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