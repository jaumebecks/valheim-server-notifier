import re
from typing import Optional

from . import Event
from settings import LOG_EVENT_TYPE_REGEXES


def resolve_event(log: str) -> Optional[Event]:
    for event in LOG_EVENT_TYPE_REGEXES.values():
        match = re.search(event.get('regex'), log)
        if not match:
            continue

        return event.get('class')(*match.groups())

    return None
