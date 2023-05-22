import customtkinter
import tkinter
import threading
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
    def __init__(self, master):
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

        self.combobox_1 = customtkinter.CTkComboBox(self.tab(PRANGE_2),
                                                    values=[PRANGE_2_VAL_NONE, PRANGE_2_VAL_1, PRANGE_2_VAL_2, PRANGE_2_VAL_3])
        self.combobox_1.grid(row=1, column=0, padx=20, pady=(20, 10))

        self.scrollable_frame = customtkinter.CTkScrollableFrame(
            self.tab(PRANGE_3), label_text="Scan Scripts")
        self.scrollable_frame.grid(row=1, column=0, sticky="nsew")

        self.label_tab_1 = customtkinter.CTkLabel(
            self.tab(PRANGE_1), text="Select TCP or UDP")
        self.label_tab_1.grid(row=0, column=0, padx=20, pady=20)

        self.combobox_2 = customtkinter.CTkComboBox(self.tab(PRANGE_1),
                                                    values=[PRANGE_1_VAL_1, PRANGE_1_VAL_2])
        self.combobox_2.grid(row=1, column=0, padx=20, pady=(20, 10))
        


        

        self.label_tab_2 = customtkinter.CTkLabel(
            self.tab(PRANGE_2), text="Select Service Scan Options")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        self.label_tab_3 = customtkinter.CTkLabel(
            self.tab(PRANGE_3), text="Select Advanced Scan Options")
        self.label_tab_3.grid(row=0, column=0, padx=20, pady=20)

        # threaded execution 
        self.create_switches_thread = threading.Thread(target=self.create_switches, args=(net_script_scan_list, self.scrollable_frame_switches))
        self.create_switches_thread.start()

    # This function is threaded due to it's long blocking time while switches are being appended
    def create_switches(self, names_list, switch_list):        
        
        for i, element in enumerate(names_list):
            self.switch = customtkinter.CTkSwitch(self.scrollable_frame, text=element)
            self.switch.grid(row=i, column=0, padx=10, pady=(0, 20), sticky="w")
            self.switch.bind("<Button-1>", self.testfunc)
            switch_list.append(self.switch)
            
            

        
        #self.create_switches_thread.join()

    def testfunc(self):
        print("switch_clicked")
   