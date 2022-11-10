from . import Event


class Death(Event):
    viking: str

    def __init__(self, viking: str) -> None:
        self.viking = viking

    def __str__(self) -> str:
        return f'**Viking {self.viking} has gone to Valhala!**'


class Join(Event):
    viking: str

    def __init__(self, viking: str) -> None:
        self.viking = viking

    def __str__(self) -> str:
        return f'*Viking {self.viking} has joined the battle!*'


class ServerOn(Event):
    def __str__(self) -> str:
        return '🟢 **Server is ON and Running** 🟢'


class ServerOff(Event):
    def __str__(self) -> str:
        return f'🛑 **Server is OFF** 🛑'


class WorldSave(Event):
    duration: str

    def __init__(self, duration) -> None:
        self.duration = duration

    def __str__(self) -> str:
        return f'*World has been saved. It took {self.duration}!*'
