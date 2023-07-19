# import calendar as cal
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from functions import *

class AddEventView(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Add event")
        self.geometry('250x150')
        self.columnconfigure(2, weight=1)

        self.name_label = ttk.Label(self, text='Name:')
        self.name_label.grid(row=0, column=0, padx=10, pady=5)

        self.name_var = tk.StringVar()
        self.name_entry = ttk.Entry(self, textvariable=self.name_var, justify='right')
        self.name_entry.grid(row=0, column=1, columnspan=3, padx=10, pady=5, sticky=tk.NSEW)
        self.name_entry.focus()

        self.date_label = ttk.Label(self, text='Date:')
        self.date_label.grid(row=1, column=0, padx=10, pady=5)

        self.date_button = ttk.Button(self, text='CC', width=5)
        self.date_button.grid(row=1, column=1, padx=10)

        self.date_var = tk.StringVar(self, "dd.mm.yy")
        self.date_entry = ttk.Entry(self, textvariable=self.date_var, justify='right')
        self.date_entry.grid(row=1, column=2, padx=10, pady=5, sticky=tk.NSEW)

        self.time_label = ttk.Label(self, text='Time:')
        self.time_label.grid(row=2, column=0, padx=10, pady=5)

        self.time_var = tk.StringVar(self, "hh:mm")
        self.time_entry = ttk.Entry(self, textvariable=self.time_var, justify='right')
        self.time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.NSEW, columnspan=3)

        # setting frame for buttons
        self.button_frame = ttk.Frame(self)
        self.button_frame.grid(row=3, column=0, columnspan=3)

        self.cancel_button = tk.Button(self.button_frame, text="Cancel", command=self.cancel)
        self.cancel_button.grid(row=0, column=0, pady=10, padx=10)

        self.add_button = tk.Button(self.button_frame, text="Add event", command=self.add_event)
        self.add_button.grid(row=0, column=1, pady=10, padx=10)

        self.interface = None

    def set_interface(self, interface):
        self.interface = interface

    def add_event(self):
        self.interface.add_event(self.name_var.get(), self.date_var.get(), self.time_var.get())

    def cancel(self):
        self.destroy()


######################################################################################
class ShowEventsView(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("List of your events")
        self.geometry('300x200')

        self.interface = self.parent.interface

        for event in self.interface.storage.events_list:






class SaveCalendarView(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Saving calendar")
        self.geometry('300x200')
