


class ArgsHandler:
    def __init__(self, command=None, args_list1=None, loaded_args=None):
        self.gui_callback1 = None
        self.gui_callback2 = None
      
        
        
        self.args_list1 = args_list1 if args_list1 is not None else []
        

    def register_gui_callback(self, callback1):
        self.gui_callback1 = callback1
      

    # handle checkbox args
    def non_gui_method(self):
        print("Non-GUI method")
        if self.gui_callback1 is not None:
            self.gui_callback1(self.args_list1)
            print("Sending callback1 signal from non-GUI code:", self.args_list1)
        
        if self.gui_callback2 is not None:
            self.gui_callback2(self.args_list1)
            print("Sending callback2 signal from non-GUI code:", self.args_list2)

   

            
        

        