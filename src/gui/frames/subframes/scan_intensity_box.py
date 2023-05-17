import customtkinter
from constants.constants import (
    CORNER_RADIUS_0, TRANSPARENT, GRID_ROW_1, GRID_COL_1, PADX_1, PADY_1, NSEW, EW, 
    PADY_2, GRID_COL_0, GRID_ROW_0 
)
from constants.net_scan_gui_const import (
    SCAN_1_INT, SCAN_2_INT, SCAN_3_INT
)

class ScanIntensityBox(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=1, column=GRID_COL_1, padx=(PADX_1, 0), pady=(PADY_1, 0), sticky=NSEW)

        # config style
        self._corner_radius = CORNER_RADIUS_0
        self.fg_color = TRANSPARENT

        # create segmented button 1
        self.seg_button_1 = customtkinter.CTkSegmentedButton(self)
        self.seg_button_1.grid(row=GRID_ROW_0, column=GRID_COL_0, padx=(PADX_1, 10), pady=(PADY_2, 10), sticky=EW)
        self.seg_button_1.configure(values=[SCAN_1_INT, SCAN_2_INT, SCAN_3_INT])
        self.seg_button_1.set("Value 2")


        # create progress bars
        self.progressbar_1 = customtkinter.CTkProgressBar(self)
        self.progressbar_1.grid(row=GRID_ROW_1, column=GRID_COL_0, padx=(PADX_1, 10), pady=(PADY_2, 10), sticky=EW)
        
        self.progressbar_2 = customtkinter.CTkProgressBar(self)
        self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        
        self.progressbar_3 = customtkinter.CTkProgressBar(self, orientation="vertical")
        self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")

        self.slider_1 = customtkinter.CTkSlider(self, from_=0, to=1, number_of_steps=4)
        self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        
        self.slider_2 = customtkinter.CTkSlider(self, orientation="vertical")
        self.slider_2.grid(row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
        
        