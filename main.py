from menu import Menu, MenuCommand, ExitCommand
from validators import validate_title, validate_date, validate_time
from calendar import Context, ListingStrategy, TextStrategy, ICalendarStrategy

calendar_list = []

context = Context(ListingStrategy)


class NewEventCommand(MenuCommand):

    def execute(self):
        self.event = {}
        self.correct_input = True

        while True:

            title = input("Title: ")
            if validate_title(title):
                self.event['title'] = title
            else:
                self.correct_input = False
                print('Invalid input')
                break

            date = input("Date (dd.mm.yyyy): ")
            if validate_date(date):
                self.event['date'] = date
            else:
                self.correct_input = False
                print('Invalid input')
                break

            time = input("Time (hh:mm): ")
            if validate_time(time):
                self.event['time'] = time
            else:
                self.correct_input = False
                print('Invalid input')
                break
            break
        if self.correct_input == True:
            calendar_list.append(self.event)

    def description(self):
        return "New event"


class ListCalendarCommand(MenuCommand):
    def execute(self):
        if len(calendar_list) == 0:
            print("There are no events in calendar.")
        else:
            context.set_strategy(TextStrategy)
            context.execute_strategy(calendar_list)

    def description(self):
        return "List calendar"


class ConvertToICalendarCommand(MenuCommand):
    def execute(self):
        if len(calendar_list) == 0:
            print("There are no events in calendar.")
        else:
            context.set_strategy(ICalendarStrategy)
            context.execute_strategy(calendar_list)

    def description(self):
        return "Export calendar to iCalendar"


def main():
    menu = Menu()

    menu.register(NewEventCommand())
    menu.register(ListCalendarCommand())
    menu.register(ConvertToICalendarCommand())
    menu.register(ExitCommand(menu))

    menu.run()


if __name__ == "__main__":
    main()
