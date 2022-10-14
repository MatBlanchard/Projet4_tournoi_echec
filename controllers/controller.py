from views.mainMenu import MainMenu


class Controller:
    __instance = None

    def __new__(cls,*args, **kwargs):
        if cls.__instance is None :
            cls.__instance = super(Controller, cls).__new__(cls, *args, **kwargs)
        return cls.__instance
