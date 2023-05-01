class Menu:
    def __init__(self):
        self._commands = []
        self._should_run = True


    def run(self):
        while self._should_run:
            print(" Menu")

            for i, cmd in enumerate(self._commands, start=1):
                print("{}. {}".format(i, cmd.description()))
            try:
                choice = int(input("Select menu item (1-4): "))
            except ValueError as e:
                print("Nieznana opcja")

            if choice < 1 or choice > len(self._commands):
                print("Nieznana opcja")
            else:
                self._commands[choice-1].execute()


    def stop(self):
        self._should_run = False


    def register(self, command):
        self._commands.append(command)


class MenuCommand:

    def execute(self):
        raise NotImplementedError("you should implement this method in subclass")


    def description(self):
        raise NotImplementedError("you should implement this method in subclass")


class ExitCommand(MenuCommand):
    def __init__(self, menu):
        self._menu = menu


    def execute(self):
        self._menu.stop()


    def description(self):
        return "Exit"
