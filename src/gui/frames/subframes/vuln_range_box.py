import customtkinter
from constants.constants import (
    CORNER_RADIUS_0, WIDTH_250, NSEW, PADY_1, PADY_1, GRID_ROW_1, GRID_COL_2
)
from constants.net_scan_gui_const import (PRANGE_1, PRANGE_2, PRANGE_3)

class VulnRangeBox(customtkinter.CTkTabview):
    def __init__(self, master):
        super().__init__(master)

        # style config
        self._corner_radius = CORNER_RADIUS_0
        self.width=WIDTH_250

        # create tabviews and set grid config
        self.grid(row=GRID_ROW_1, column=GRID_COL_2, padx=(PADY_1, 0), pady=(PADY_1, 0), sticky=NSEW)
        self.add(PRANGE_1)
        self.add(PRANGE_2)
        self.add(PRANGE_3)
        self.tab(PRANGE_1).grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tab(PRANGE_2).grid_columnconfigure(0, weight=1)
        self.tab(PRANGE_3).grid_columnconfigure(0, weight=1)

        # create option menus for tabs
        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tab(PRANGE_1), dynamic_resizing=False,
                                                        values=["Value 1", "Value 2", "Value Long Long Long"])
        self.optionmenu_1.grid(row=1, column=0, padx=20, pady=(20, 10))

        self.combobox_1 = customtkinter.CTkComboBox(self.tab(PRANGE_2),
                                                    values=["Value 1", "Value 2", "Value Long....."])
        self.combobox_1.grid(row=1, column=0, padx=20, pady=(20, 10))

        self.string_input_button = customtkinter.CTkButton(self.tab(PRANGE_3), text="Open CTkInputDialog",
                                                           command=None)
        self.string_input_button.grid(row=1, column=0, padx=20, pady=(20, 10))
        
        self.label_tab_1 = customtkinter.CTkLabel(self.tab(PRANGE_1), text="CTkLabel on Tab 2")
        self.label_tab_1.grid(row=0, column=0, padx=20, pady=20)

        self.label_tab_2 = customtkinter.CTkLabel(self.tab(PRANGE_2), text="CTkLabel on Tab 2")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        self.label_tab_3 = customtkinter.CTkLabel(self.tab(PRANGE_3), text="CTkLabel on Tab 2")
        self.label_tab_3.grid(row=0, column=0, padx=20, pady=20)

        