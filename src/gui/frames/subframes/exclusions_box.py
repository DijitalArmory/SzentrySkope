import tracemalloc
tracemalloc.start()

import customtkinter
import asyncio
from constants.constants import (
    CORNER_RADIUS_0, WIDTH_250, NSEW, PADY_1, PADY_1, GRID_ROW_1, GRID_COL_2
)
from constants.net_scan_gui_const import (PRANGE_1, PRANGE_2, PRANGE_3)
from constants.net_script_scan import net_script_scan_list

class ExclusionsBox(customtkinter.CTkTabview):
    def __init__(self, master):
        super().__init__(master)

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
                                                    values=["Value 1", "Value 2", "Value Long....."])
        self.combobox_1.grid(row=1, column=0, padx=20, pady=(20, 10))

        self.scrollable_frame = customtkinter.CTkScrollableFrame(
            self.tab(PRANGE_3), label_text="Vuln Options")
        self.scrollable_frame.grid(row=1, column=0, sticky="nsew")

        self.label_tab_1 = customtkinter.CTkLabel(
            self.tab(PRANGE_1), text="CTkLabel on Tab 2")
        self.label_tab_1.grid(row=0, column=0, padx=20, pady=20)
        self.string_input_button = customtkinter.CTkButton(self.tab(PRANGE_1), text="Load Advanced Options",
                                                           command=self.run_load_switches)
        self.string_input_button.grid(row=1, column=0, padx=20, pady=(20, 10))

        self.label_tab_2 = customtkinter.CTkLabel(
            self.tab(PRANGE_2), text="CTkLabel on Tab 2")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        self.label_tab_3 = customtkinter.CTkLabel(
            self.tab(PRANGE_3), text="Select Vulnerability Scan")
        self.label_tab_3.grid(row=0, column=0, padx=20, pady=20)

    # Create script switches 
    async def create_switches_async(self, name_list, switch_list):
        switches = []
        for i, element in enumerate(name_list):
            switch = customtkinter.CTkSwitch(self.scrollable_frame, text=element)
            switch.grid(row=i, column=0, padx=10, pady=(0, 20), sticky="w")
            switch.bind("<Button-1>", self.testfunc)
            switch_list.append(switch)
            switches.append(switch)
        return switches 
    
    async def load_switches(self):
            # Call create_switches_async() as an await-able function
            switch_list = []
            switches = await self.create_switches_async(net_script_scan_list, switch_list)
            print("Switches created:", switches)
        
    def run_load_switches(self):
        asyncio.run(self.load_switches())


            
    
    def testfunc(self):
        print("switch_clicked")
   