import customtkinter
from gui.frames.subframes.scan_techniques_box import ScanTechniquesBox
from gui.frames.subframes.exclusions_box import ExclusionsBox
from constants.net_scan_gui_const import scan_techniques_txt
from gui.frames.subframes.scan_intensity_box import ScanIntensityBox
from gui.frames.subframes.host_options_box import HostOptionsBox
from gui.frames.subframes.port_options_box import PortOptionsBox
from scans.args_handler import ArgsHandler
from constants.constants import (
    CORNER_RADIUS_0, GRID_COL_1, GRID_COL_2, GRID_COL_3, GRID_COL_0, GRID_ROW_3,
    GRID_WEIGHT_0, GRID_WEIGHT_1, NSEW, PADX_1, SHADE_3, PADY_1, TRANSPARENT,
)





class NetworkScanner(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        # config style
        self._corner_radius = CORNER_RADIUS_0
        
        self.checkbox_list = [] # gui checkbox list
        #self.checkbox_args_list = [] # onvalue checkbox args (when-checked)
        #self.args_list = [] # receives the args_list of self.checkbox_args_list
        self.checkbox_args_list = [] 

        self.scan_techniques_box = ScanTechniquesBox(self, args_list=self.checkbox_args_list, checkbox_list=self.checkbox_list, command=self.update_args_handler)
        self.scan_techniques_box.grid_columnconfigure(0, weight=1)

        
        
        
        # create vuln_range frame
        self.vuln_range_box = ExclusionsBox(self)
        self.vuln_range_box.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create scan_intensity_box frame
        self.scan_intensity_box = ScanIntensityBox(self)
        self.scan_intensity_box.grid_columnconfigure(0, weight=1)
        self.scan_intensity_box.grid_rowconfigure(4, weight=1)

        # creat host scaning options frame
        self.host_options_box = HostOptionsBox(self)
    
        # create port_range box
        self.port_range_box = PortOptionsBox(self)


        # create 'Begin Scan' button
        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color=TRANSPARENT, border_width=2, text="Start Scan", text_color=(SHADE_3, "#DCE4EE"))
        self.main_button_1.grid(row=GRID_ROW_3, column=GRID_COL_3, padx=(20, 20), pady=(PADX_1, PADX_1), sticky=NSEW)
        
        # create entry bar
        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=3, column=1, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        # create output box
        self.output_box = customtkinter.CTkTextbox(self, width=250)
        self.output_box.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.output_box.insert("0.0", "CTkoutput_box\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)

        # create 'Abort Scan' button
        # create 'Begin Scan' button
        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color=TRANSPARENT, border_width=2, text="Abort Scan Scan", text_color=(SHADE_3, "#DCE4EE"))
        self.main_button_1.grid(row=GRID_ROW_3, column=GRID_COL_2, padx=(PADX_1, PADX_1), pady=(PADY_1, PADY_1), sticky=NSEW)
        
        #self.args_handler = ArgsHandler(args_list=self.checkbox_args_list)

    def update_args_handler(self):
        print("Updated checkbox_args_list in NetworkScanner:", self.checkbox_args_list)

        #self.after(0, self.perform_args_update)
    '''  
    def perform_args_update(self):
        print("Updated checkbox_args_list in NetworkScanner:", self.checkbox_args_list)
    
        self.args_handler.update_checkbox_args_list(self.checkbox_args_list)
    ''' 