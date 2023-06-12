import customtkinter
import tkinter
import threading
import functools
from data.net_scan_data import (udp_protocols, scan_service_detection)
from constants.constants import (
    CORNER_RADIUS_0, WIDTH_250, NSEW, PADY_1, PADY_1, GRID_ROW_1, GRID_COL_2, 
     GRID_COL_0, GRID_ROW_2, GRID_COL_0, PADY_2, PADX_2, PADX_1, N
)
from constants.net_scan_gui_const import (
    PRANGE_1, PRANGE_2, PRANGE_3, PRANGE_1_VAL_1, PRANGE_1_VAL_2, PRANGE_2_VAL_1, 
    PRANGE_2_VAL_2, PRANGE_2_VAL_3, PRANGE_2_VAL_NONE
    )
from constants.net_script_scan import net_script_scan_list

class ExclusionsBox(customtkinter.CTkTabview):
    def __init__(self, master, args_list1=None, args_list2=None, args_list3=None, command=None):
        super().__init__(master)

        self.scrollable_frame_switches = []

        # style config
        self._corner_radius = CORNER_RADIUS_0
        self.width = WIDTH_250

        # create tabviews and set grid config
        self.grid(row=GRID_ROW_1, column=GRID_COL_2, padx=(
            PADY_1, 0), pady=(PADY_1, 0), sticky=NSEW)
        self.add(PRANGE_1)
        self.add(PRANGE_2)
        self.add(PRANGE_3)
        self.tab(PRANGE_1).grid_columnconfigure(
            0, weight=1)  # configure grid of individual tabs
        self.tab(PRANGE_2).grid_columnconfigure(0, weight=1)
        self.tab(PRANGE_3).grid_columnconfigure(0, weight=1)


        self.command = command
        self.args_list1 = args_list1 if args_list1 is not None else []
        self.args_list2 = args_list2 if args_list2 is not None else []
        self.args_list3 = args_list3 if args_list3 is not None else []
        


        
            # TCP UDP OPTIONS
        
        self.udp_option = list(udp_protocols.keys())[0]
        self.udp_option_val = list(udp_protocols.values())[0]

        self.tcpudp_tab = customtkinter.CTkLabel(
            self.tab(PRANGE_1), text="Select TCP or UDP")
        self.tcpudp_tab.grid(row=0, column=0, padx=20, pady=20)

        self.combobox_tcpudp = customtkinter.CTkComboBox(self.tab(PRANGE_1),
                                                    values=["None", PRANGE_1_VAL_1, self.udp_option], command=self.set_tcpudp_val)
        self.combobox_tcpudp.grid(row=1, column=0, padx=20, pady=(20, 10))
        


            # SERVICE SCAN
        self.service_options = list(scan_service_detection.keys())
        self.service_options_vals = list(scan_service_detection.values())
        '''
        LEFT OFF:
        TODO - setup service args
        '''

        self.combobox_1 = customtkinter.CTkComboBox(self.tab(PRANGE_2),
                                                    values=[PRANGE_2_VAL_NONE, self.service_options[0], self.service_options[1], self.service_options[2]], 
                                                    command=self.set_service_val)
        self.combobox_1.grid(row=1, column=0, padx=20, pady=(20, 10))

        self.label_tab_2 = customtkinter.CTkLabel(
            self.tab(PRANGE_2), text="Select Service Scan Options")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        self.label_tab_3 = customtkinter.CTkLabel(
            self.tab(PRANGE_3), text="Select Advanced Scan Options")
        self.label_tab_3.grid(row=0, column=0, padx=20, pady=20)


            # scripts Scan Options
        self.scrollable_frame = customtkinter.CTkScrollableFrame(
            self.tab(PRANGE_3), label_text="Scan Scripts")
        self.scrollable_frame.grid(row=1, column=0, sticky="nsew")

        # threaded execution 
        self.create_switches_thread = threading.Thread(target=self.create_switches, args=(net_script_scan_list, self.scrollable_frame_switches))
        self.create_switches_thread.start()

        #self.handle_toggle_thread = threading.Thread(target=self.testfunc)
        #self.handle_toggle_thread.start()
        
    # This function is threaded due to it's long blocking time while switches are being appended
        # Dictionary to store switch states
        self.switch_states = {}

    def create_switches(self, names_list, switch_list):        
        for i, element in enumerate(names_list):
            self.switch = customtkinter.CTkSwitch(self.scrollable_frame, text=f"{i}. {element}")
            self.switch.grid(row=i, column=0, padx=10, pady=(0, 20), sticky="w")
            
            # Bind switch to a custom function with additional argument
            self.switch.bind("<Button-1>", functools.partial(self.testfunc, i, element=element))
            
            # Store initial switch state
            self.switch_states[i] = "off"
            
            switch_list.append(self.switch)


    def testfunc(self, switch_index, *args, **kwargs):
        # Retrieve the 'element' argument if it exists
        if "element" in kwargs:
            element = kwargs["element"]
            # Toggle the switch state
        if self.switch_states[switch_index] == "on":
            self.switch_states[switch_index] = "off"
            # Remove switch value from args_list3
            self.args_list3.remove(element)
        else:
            self.switch_states[switch_index] = "on"
            # Append switch value to args_list3
            self.args_list3.append(element)

        # Print the switch state
        if self.switch_states[switch_index] == "on":
            print(f"Switch {switch_index} clicked ON")
        else:
            print(f"Switch {switch_index} clicked OFF")

        # Print the updated args_list3
        print(self.args_list3)


    def set_tcpudp_val(self, selected_option):
        self.selected_option = selected_option
        if self.selected_option == self.udp_option:
            self.args_list1.append(self.udp_option_val)
            print(self.args_list1)
        elif self.udp_option_val in self.args_list1:
            self.args_list1.remove(self.udp_option_val)
            print(self.args_list1)
        else:
            print(self.args_list1)
            return
        
    def set_service_val(self, selected_value):
        if selected_value in self.service_options:
            index = self.service_options.index(selected_value)
            self.args_list2 = [self.service_options_vals[index]]
        else:
            self.args_list2 = []

        # Print the updated args_list
        print(self.args_list2)

    