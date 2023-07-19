from tkinter.messagebox import showerror


class Interface:
    def __init__(self, storage, event, menu):
        self.storage = storage
        self.event = event
        self.menu = menu
        self.add_event_view = None
        self.show_events_view = None
        self.save_calendar_view = None

    def add_event(self, name, date, time):
        try:
            self.event.name = name
            self.event.date = date
            self.event.time = time
            self.storage.add_event(name, date, time)

            self.add_event_view.destroy()
            print(self.storage.events_list)

        except ValueError as message:
            showerror(title="Error", message=message)

    def show_events(self):
        self.storage.show_events()

    def save_storage(self):
        self.storage.save()
