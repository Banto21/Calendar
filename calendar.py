from abc import ABC, abstractmethod


# Context class

class Context:

    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_strategy(self, calendar):
        self._strategy.execute(self, calendar)


# Strategy interface
class ListingStrategy(ABC):

    @abstractmethod
    def execute(self, calendar):
        pass


# Concrete strategies
class TextStrategy(ListingStrategy):

    def execute(self, calendar):
        for event in calendar:
            print("Title: {}".format(event['title']))
            print("Date: {}, {}".format(event['date'], event['time']))


class ICalendarStrategy(ListingStrategy):
    def execute(self, calendar):
        print("BEGIN:VCALENDAR\nVERSION:2.0\nBEGIN:VTIMEZONE\nTZID:Europe/Warsaw\nX-LIC-LOCATION:Europe/Warsaw")
        print("END:VTIMEZONE")

        for event in calendar:
            icalendar_date = event['date'][6:] + event['date'][3:5] + event['date'][:2]
            icalendar_time = event['time'][0:2] + event['time'][3:]
            print("BEGIN:VEVENT")
            print("DTSTART:{}T{}00".format(icalendar_date, icalendar_time))
            print("DTEND:{}T{}00".format(icalendar_date, icalendar_time))
            print("SUMMARY:{}".format(event['title']))
            print("END:VEVENT")

        print("END:VACLENDAR")
