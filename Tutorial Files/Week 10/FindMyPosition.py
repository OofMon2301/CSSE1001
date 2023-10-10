"""
Simple GUI programming exercise to demonstrate simple graphics programming
and event handling.
"""

__copyright__ = "Copyright 2018, University of Queensland"


import tkinter as tk


class SettingsFrame(tk.Frame):
    """A frame which allows users to change settings of the application
    Settings to change are: whether or not a line preview is shown.
    """

    def __init__(self, parent):
        """Initialise the widget, with its subwidgets."""
        super().__init__(parent)

        self._position_label = tk.Label(self, text="Current Position:")
        self._position_label.pack(side=tk.LEFT)

        self._preview_button = tk.Button(
            self, text="Preview On", bg="green", command=self._toggle_preview
        )
        self._preview_button.pack(side=tk.RIGHT)

    def _toggle_preview(self):
        """Toggle the line preview on/off."""
        if self.is_preview_on():
            self._preview_button.config(text="Preview Off", bg="gray")
        else:
            self._preview_button.config(text="Preview On", bg="green")

    def is_preview_on(self) -> bool:
        """(bool) Return True if the preview setting is on, otherwise False."""
        if self._preview_button["text"] == "Preview On":
            return True
        else:
            return False

    def set_position(self, x, y):
        """Change the 'Current Position' label to show new (x,y) coordinates."""
        if x is None or y is None:
            self._position_label.config(text="Current Position: None")
        else:
            self._position_label.config(text="Current Position: ({}, {})".format(x, y))


class DrawingApp(object):
    """An application for drawing lines."""

    def __init__(self, master):
        """Initialise a DrawingApp object, including widget layout."""
        self._master = master
        master.title("Drawing Application")
        master.minsize(500, 375)

        self._canvas = tk.Canvas(master, bd=2, relief=tk.SUNKEN)
        self._canvas.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self._canvas.bind("<Motion>", self.evt_motion)
        # More Canvas bindings can be added here

        self._settings = SettingsFrame(master)
        self._settings.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        menubar = tk.Menu(master)
        master.config(menu=menubar)

        filemenu = tk.Menu(menubar)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Exit", command=self.exit)

        editmenu = tk.Menu(menubar)
        menubar.add_cascade(label="Edit", menu=editmenu)
        editmenu.add_command(label="Clear All Lines", command=self.clear)

    def evt_motion(self, event):
        """Event handler for Mouse movement on the Canvas."""
        self._settings.set_position(event.x, event.y)

    def exit(self):
        """Close the application."""
        self._master.destroy()

    def clear(self):
        """Delete all lines from the application."""
        self._canvas.delete(tk.ALL)


if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
