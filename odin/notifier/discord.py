from requests import post

from . import Template


def publish_event(webhook_url: str, event: Template):
    post(
        webhook_url,
        json=event.get_payload(),
        headers={'Content-Type': 'application/json'}
    )
