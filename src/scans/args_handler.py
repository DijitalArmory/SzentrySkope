


class ArgsHandler:
    def __init__(self, command=None, args_list=None, loaded_args=None):
        self.gui_callback1 = None
        self.gui_callback2 = None
        
        
        self.args_list = args_list if args_list is not None else []
        self.loaded_args = loaded_args if loaded_args is not None else []

    def register_gui_callback(self, callback1, callback2):
        self.gui_callback1 = callback1
        self.gui_callback2 = callback2

    # handle checkbox args
    def non_gui_method1(self):
        print("Non-GUI method")
        if self.gui_callback1 is not None:
            self.gui_callback1(self.args_list)
            print("Sending callback1 signal from non-GUI code:", self.args_list)
            

    def non_gui_method2(self):
        pass

    def test(self):
        pass



            
        

        