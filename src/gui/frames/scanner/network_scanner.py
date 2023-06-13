import customtkinter
from gui.frames.subframes.scan_techniques_box import ScanTechniquesBox
from gui.frames.subframes.exclusions_box import ExclusionsBox
from gui.frames.subframes.scan_intensity_box import ScanIntensityBox
from gui.frames.subframes.host_options_box import HostOptionsBox
from gui.frames.subframes.port_options_box import PortOptionsBox
from scans.args_handler import ArgsHandler
from constants.constants import (
    CORNER_RADIUS_0, GRID_COL_1, GRID_COL_2, GRID_COL_3, GRID_COL_0, GRID_ROW_3,
    GRID_WEIGHT_0, GRID_WEIGHT_1, NSEW, PADX_1, SHADE_3, PADY_1, TRANSPARENT,
)
from constants.net_scan_commands import (
    SCAN_INIT
)





class NetworkScanner(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # config style
        self._corner_radius = CORNER_RADIUS_0
        
        self.checkbox_list = [] # gui checkbox list
         
        self.loaded_args = [] # this is just placeholder for future checkbox_args_list appension
        

        self.checkbox_args_list = []
        self.scan_techniques_box = ScanTechniquesBox(self, args_list=self.checkbox_args_list, checkbox_list=self.checkbox_list, command=self.execute_non_gui_code)
        self.scan_techniques_box.grid_columnconfigure(0, weight=1)

        
        
        
        # create vuln_range frame
        self.tcpudp_options_args_list = []
        self.service_options_args_list = []
        self.script_options_args_list = []
        self.combined_exclusions_box_args_list = []
        self.vuln_range_box = ExclusionsBox(self, args_list1=  self.tcpudp_options_args_list, args_list2= self.service_options_args_list, args_list3= self.script_options_args_list, command=self.on_gui_callback4)
        self.vuln_range_box.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create scan_intensity_box frame
        self.scan_intensity_box = ScanIntensityBox(self)
        self.scan_intensity_box.grid_columnconfigure(0, weight=1)
        self.scan_intensity_box.grid_rowconfigure(4, weight=1)

        # creat host scaning options frame
        self.host_options_args_list = []
        self.host_options_box = HostOptionsBox(self, args_list=self.host_options_args_list, command=self.execute_non_gui_code3)
    
        # create port_range box
        self.port_args_list = []
        self.port_options_box = PortOptionsBox(self, args_list=self.port_args_list, command=self.execute_non_gui_code2)

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

        # handle checbox args phase1selected_value
        self.checkbox_args_handler = ArgsHandler(self.checkbox_args_list)
        self.checkbox_args_handler.register_gui_callback(self.on_gui_callback)

        self.port_args_handler = ArgsHandler(self.port_args_list)
        self.port_args_handler.register_gui_callback(self.on_gui_callback2)

        self.host_args_handler = ArgsHandler(self.host_options_args_list)
        self.host_args_handler.register_gui_callback(self.on_gui_callback3)

        #self.tcpudp_args_handler = ArgsHandler(self.tcpudp_options_args_list)
        #self.tcpudp_args_handler.register_gui_callback(self.on_gui_callback4)

        #self.service_args_handler = ArgsHandler(self.service_options_args_list)
        #self.service_args_handler.register_gui_callback(self.on_gui_callback4)

        #self.script_args_handler = ArgsHandler(self.script_options_args_list)
        #self.script_args_handler.register_gui_callback(self.on_gui_callback4)

    def execute_non_gui_code(self):
        self.checkbox_args_handler.non_gui_method() # handle checbox args phase2
        

    def execute_non_gui_code2(self, list):
        self.port_args_handler.non_gui_method()
        print("Executing non-gui code")

    def execute_non_gui_code3(self, list):
        self.host_args_handler.non_gui_method()

    
        

    def on_gui_callback(self, data):
        data = self.checkbox_args_list 
        print("Received callback1 signal from non-GUI code:", data)

    def on_gui_callback2(self, data):
            self.port_args_list = data
            print("Received callback2 signal from non-GUI code:", data)

    def on_gui_callback3(self, data):
        self.host_options_args_list = data
        print("Received callback3 signal from non-GUI code:", data)
        print("TYPE-> ", type(data))

    def on_gui_callback4(self, data1, data2, data3):
        self.tcpudp_options_args_list = data1
        self.service_options_args_list = data2
        self.script_options_args_list = data3
        print("Received callback4 signal from non-GUI code:", data1)
        print("TYPE-> ", type(data1))
        print("------------------------------------")
        print("Received callback4 signal from non-GUI code:", data2)
        print("TYPE-> ", type(data2))
        print("------------------------------------")
        print("Received callback4 signal from non-GUI code:", data3)
        print("TYPE-> ", type(data3))
       
