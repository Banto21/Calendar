from main_menu import *
from event import *
from interface import *

if __name__ == "__main__":
    app = CalendarWindow()
    menu = MainFrame(app)
    storage = Storage()
    event = Event()
    interface = Interface(storage, event, menu)

    menu.set_interface(interface)

    app.mainloop()
