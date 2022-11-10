from event import types
from . import Template

class ServerOnTemplate(Template):
    def get_payload(self) -> dict:
        payload = super().get_payload()
        payload['embeds'] = [{
            'author': {
                'name': 'Odin',
                'icon_url': 'https://static.wikia.nocookie.net/marvel-contestofchampions/images/4/47/Odin_portrait.png/revision/latest?cb=20210307223313',
            },
            'title': 'My world is ready for the best warriors',
            'description': 'Who will join me in our battle?',
        }]
        return payload



class ServerOffTemplate(Template):
    def get_payload(self) -> dict:
        payload = super().get_payload()
        payload['embeds'] = [{
            'author': {
                'name': 'Odin',
                'icon_url': 'https://static.wikia.nocookie.net/marvel-contestofchampions/images/4/47/Odin_portrait.png/revision/latest?cb=20210307223313',
            },
            'title': 'Very nice crusades today. We\'ll raid another day',
            'description': 'Have some rest dear warrior. We\'ll meet soon',
        }]
        return payload



class JoinTemplate(Template):
    def get_payload(self) -> dict:
        payload = super().get_payload()
        payload['embeds'] = [{
            'author': {
                'name': 'Odin',
                'icon_url': 'https://static.wikia.nocookie.net/marvel-contestofchampions/images/4/47/Odin_portrait.png/revision/latest?cb=20210307223313',
            },
            'title': f'Welcome my fellow partner {self.event.viking}, good to see you again',
            'description': 'Satisfy my wishes and you might reach Valhala',
        }]
        return payload



class DeathTemplate(Template):
    def get_payload(self) -> dict:
        payload = super().get_payload()
        payload['embeds'] = [{
            'author': {
                'name': 'Odin',
                'icon_url': 'https://static.wikia.nocookie.net/marvel-contestofchampions/images/4/47/Odin_portrait.png/revision/latest?cb=20210307223313',
            },
            'title': f'Oh come on {self.event.viking}! You are not ready for Valhala, yet',
            'description': 'Go back there and fight for our honor!',
        }]
        return payload


class WorldSaveTemplate(Template):
    pass


MAP = {
    types.ServerOn: ServerOnTemplate,
    types.ServerOff: ServerOffTemplate,
    types.Join: JoinTemplate,
    types.Death: DeathTemplate,
    types.WorldSave: WorldSaveTemplate,
}


def build_template(event: types.Event) -> Template:
    template = MAP.get(type(event))
    if not template:
        raise Exception(f'Template mapping for given event <{type(event)}> not found')

    return template(event)
