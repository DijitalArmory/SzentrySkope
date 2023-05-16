import customtkinter
from gui.frames.subframes.scan_techniques_box import ScanTechniquesBox
from gui.frames.subframes.vuln_range_box import VulnRangeBox
from constants.net_scan_gui_const import scan_techniques_txt
from constants.constants import (
    CORNER_RADIUS_0, GRID_COL_1, GRID_COL_2, GRID_COL_3, GRID_COL_0, GRID_ROW_3,
    GRID_WEIGHT_0, GRID_WEIGHT_1, NSEW, PADX_1, SHADE_3
)

class NetworkScanner(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # configure grid layout (4x4)
        self.grid_columnconfigure(GRID_COL_1, weight=GRID_WEIGHT_1)
        self.grid_columnconfigure((GRID_COL_2, GRID_COL_3), weight=GRID_WEIGHT_0)
        self.grid_rowconfigure((GRID_COL_0, GRID_COL_1, GRID_COL_2), weight=GRID_WEIGHT_1)

        # config style
        self._corner_radius = CORNER_RADIUS_0

        # create scrollable checkbox frame
        self.checked_items = scan_techniques_txt

        self.scan_techniques_box = ScanTechniquesBox(self,self.checked_items, command=self.test)
       
        self.scan_techniques_box.grid_columnconfigure(0, weight=1)

        # create port_range frame
        self.vuln_range_box = VulnRangeBox(self)
        self.vuln_range_box.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create 'Begin Scan' button
        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text="Start Scan", text_color=(SHADE_3, "#DCE4EE"))
        self.main_button_1.grid(row=GRID_ROW_3, column=GRID_COL_3, padx=(20, 20), pady=(PADX_1, PADX_1), sticky=NSEW)
        
    def test(self):
        print("TESTING")