import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno
from views import *


class CalendarWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # set name, width, height and grid
        self.title("Calendar")
        self.geometry('250x150')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # set rows and column to expand
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        # create and show menu buttons
        self.button_new_event = ttk.Button(self, text="Add new event", command=self.new_event)
        self.button_new_event.grid(row=0, column=0, sticky=tk.NSEW)

        self.button_show_events = ttk.Button(self, text="Show events", command=self.show_events)
        self.button_show_events.grid(row=1, column=0, sticky=tk.NSEW)

        self.button_save_calendar = ttk.Button(self, text="Save ", command=self.show_events)
        self.button_save_calendar.grid(row=2, column=0, sticky=tk.NSEW)

        # button closing entire app
        self.button_exit = ttk.Button(self, text="Exit", command=self.exit)
        self.button_exit.grid(row=3, column=0, sticky=tk.NSEW)

        # show MainFrame
        self.grid(sticky=tk.NSEW)

        self.interface = None

    def set_interface(self, interface):
        self.interface = interface

    def new_event(self):
        add_event_view = AddEventView(self)
        add_event_view.grab_set()
        add_event_view.set_interface(self.interface)
        self.interface.add_event_view = add_event_view

    def show_events(self):
        show_events_view = ShowEventsView(self)
        show_events_view.grab_set()
        self.interface.show_events_view = show_events_view

    def save_calendar(self):
        save_calendar_view = SaveCalendarView(self)
        save_calendar_view.grab_set()
        self.interface.save_calendar_view = save_calendar_view

    def exit(self):
        answer = askyesno(title='Confirmation', message='Are you sure that you want to quit?')
        if answer:
            self.master.destroy()
