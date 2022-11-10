from event import types

class Template:
    event: types.Event

    def __init__(self, event: types.Event) -> None:
        self.event = event

    def get_payload(self) -> dict:
        return {
            'content': str(self.event)
        }
