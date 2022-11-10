import os, time
from typing import Generator, Optional

def read_logs(path: str)-> Generator[Optional[str], None, None]:
    """generator function that yields new lines in a file

    :param path: File Path as a string
    :type path: str
    :rtype: collections.Iterable
    """
    seek_end = True
    while True:  # handle moved/truncated files by allowing to reopen
        with open(path) as f:
            if seek_end:  # reopened files must not seek end
                f.seek(0, 2)
            while True:  # line reading loop
                line = f.readline()
                if not line:
                    try:
                        if f.tell() > os.path.getsize(path):
                            # rotation occurred (copytruncate/create)
                            f.close()
                            seek_end = False
                            break
                    except FileNotFoundError:
                        # rotation occurred but new file still not created
                        pass  # wait 1 second and retry
                    time.sleep(1)
                yield line
