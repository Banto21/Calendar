from validators import *


class Event:
    def __init__(self, name='', date='', time=''):
        self._name = name
        self._date = date
        self._time = time

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, new_date):
        if validate_date(new_date):
            self._date = new_date
        else:
            raise ValueError(f"Invalid date: {new_date}")

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, new_time):
        if validate_time(new_time):
            self._time = new_time
        else:
            raise ValueError(f"Invalid time: {new_time}")


class Storage:
    def __init__(self):
        self.events_dict = {}
        self.current_id = 0

    def add_event(self, name, date, time):
        self.current_id += 1
        self.events_dict[str(self.current_id)] = {
            'name': name,
            'date': date,
            'time': time
        }

    def show_events(self):
        pass

    def delete_events(self, id_list):
        pass

    def save(self):
        pass

    def delete_event(self):
        pass
