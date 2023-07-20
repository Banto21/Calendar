# import calendar as cal
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno
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

        self.events_frame = ttk.Frame(self)
        self.events_frame.pack()
        self.events_row_number = 0

        self.action_buttons_frame = ttk.Frame(self)
        self.action_buttons_frame.pack()

        self.edit_button = ttk.Button(self.action_buttons_frame, text='Edit', command=self.edit_event)
        self.edit_button.grid(row=0, column=0, padx=10, pady=10)
        self.delete_button = ttk.Button(self.action_buttons_frame, text='Delete', command=self.delete_event)
        self.delete_button.grid(row=0, column=1, padx=10, pady=10)
        self.exit_button = ttk.Button(self.action_buttons_frame, text='Exit', command=self.exit)
        self.exit_button.grid(row=0, column=2, padx=10, pady=10)

        self.interface = self.parent.interface

        self.show_events()

        self.checked_events = []

    def show_events(self):
        for event_id, event in self.interface.storage.events_dict.items():

            check = tk.Checkbutton(self.events_frame, text=event['name'], variable=tk.StringVar(),
                                    onvalue=event_id, offvalue='0')
            check.deselect()
            check.grid(row=self.events_row_number, column=0, padx=10, pady=5, sticky='w')

            date_label = ttk.Label(self.events_frame, text=event['date'])
            date_label.grid(row=self.events_row_number, column=1, padx=10, pady=5)

            time_label = ttk.Label(self.events_frame, text=event['time'])
            time_label.grid(row=self.events_row_number, column=2, padx=10, pady=5)

            self.events_row_number += 1

        self.events_row_number = 0

    def check_clicked(self):
        pass



    def edit_event(self):
        pass

    def delete_event(self):
        pass

    def exit(self):
        answer = askyesno(title='Confirmation', message='Are you sure that you want to quit?')
        if answer:
            self.destroy()






class SaveCalendarView(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Saving calendar")
        self.geometry('300x200')
