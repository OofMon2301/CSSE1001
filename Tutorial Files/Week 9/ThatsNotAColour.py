"""
Simple GUI programming exercise to demonstrate component layout
and event handling.
"""

__copyright__ = "Copyright 2018, University of Queensland"


import tkinter as tk
from tkinter import messagebox


class SampleApp(object) :
    def __init__(self, master) :
        self._master = master
        master.title("Hello!")
        master.minsize(430, 200)


        self._lbl = tk.Label(master, text="Choose a button")
        self._lbl.pack(expand=True)
        
        
        
        # Wrap in a frame to get the buttons to align left-right in the center of the window
        frame = tk.Frame(master)
        # 10px padding so it doesn't touch the edge of the window
        blue_btn = tk.Button(frame, text="Make Blue", command=self.make_blue)
        # Bottom-center left
        blue_btn.pack(side=tk.LEFT, pady=10)
        
        green_btn = tk.Button(frame, text="Make Green", command=self.make_green)
        # Bottom-center right
        green_btn.pack(side=tk.RIGHT, pady=10)
        
        # Pack the frame
        frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
        
        # Another frame for the bottom buttons #
        
        
        # Another frame at the bottom for entry widget
        entry_frame = tk.Frame(master)
        
        label = tk.Label(entry_frame, text="Change the colour to:") 
        label.pack(side=tk.LEFT)
        # Button to change the colour
        
        entry_frame.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=10)
        
        enter_frame = tk.Frame(master)
        # Entry colour, needs to fill the space horizontally
        colour_btn = tk.Button(entry_frame, text="Change it!", command=self.get_colour)
        colour_btn.pack(side=tk.RIGHT)
        self._entry = tk.Entry(master)
        self._entry.pack(expand=True, side=tk.LEFT)
        enter_frame.pack(side=tk.RIGHT, fill=tk.X, padx=10, pady=10)
        
    def make_blue(self):
        """ Makes the button blue. """
        self._lbl.config(text="This label is blue")
        self._lbl.config(bg="blue")
    
    def make_green(self):
        """ Makes the button green. """
        self._lbl.config(text="This label is green")
        self._lbl.config(bg="green")
    
    def get_colour(self):
        """ Gets the colour from the entry widget. """
        if self._entry.get() in [
            "blue", 
            "green", 
            "red", 
            "yellow", 
            "orange", 
            "purple", 
            "pink", 
            "black", 
            "white", 
            "grey", 
            "brown", 
            "cyan", 
            "magenta",
            "turquoise",
            "lime",
            "indigo",
            "violet",
            "teal",
            "navy",
            "maroon",
            "olive",
            "beige",
            "apricot",
            "azure",
            "lavender",
            "mint",
            "tan",
            "coral",
            "salmon",
            "gold",
            "silver",
            "bronze",
            "copper",
            "rose",
            "crimson",
            "fuchsia",
            "plum",
            "ivory",
            "khaki",
            "lemon",
            "peach",
            "ruby",
            "sapphire",
            "emerald",
            "topaz",
            "pearl",
            "sand",
            ]:
            return self._lbl.config(bg=self._entry.get()) or self._lbl.config(text="This label is " + self._entry.get())
        else:
            return messagebox.showerror("Invalid Colour",  self._entry.get() +" is not a colour!")

if __name__ == "__main__" :
    root = tk.Tk()
    app = SampleApp(root)
    root.mainloop()
