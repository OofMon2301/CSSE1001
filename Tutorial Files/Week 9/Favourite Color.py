"""
Simple GUI programming exercise to demonstrate component layout
and event handling.
"""

__copyright__ = "Copyright 2018, University of Queensland"


import tkinter as tk


class SampleApp(object) :
    def __init__(self, master) :
        self._master = master
        master.title("Hello!")
        master.minsize(430, 200)

        self._lbl = tk.Label(master, text="Choose a button")
        self._lbl.pack(expand=True)
        
        
        
        # Wrap in a frame to get the buttons to align properly
        frame = tk.Frame(master)
        # 10px padding so it doesn't touch the edge of the window
        blue_btn = tk.Button(frame, text="Make Blue", command=self.make_blue)
        blue_btn.pack(side=tk.LEFT, pady=10)
        
        green_btn = tk.Button(frame, text="Make Green", command=self.make_green)
        green_btn.pack(side=tk.LEFT, pady=10)
        
        # Pack the frame
        frame.pack(side=tk.BOTTOM)
        
    def make_blue(self):
        """ Makes the button blue. """
        self._lbl.config(text="This label is blue")
        self._lbl.config(bg="blue")
    
    def make_green(self):
        """ Makes the button green. """
        self._lbl.config(text="This label is green")
        self._lbl.config(bg="green")

if __name__ == "__main__" :
    root = tk.Tk()
    app = SampleApp(root)
    root.mainloop()
