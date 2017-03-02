import errno
import os


def mkdir_p(dirpath):
    """Emulate `mkdir -p` shell command"""
    try:
        os.makedirs(dirpath)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(dirpath):
            # Ignore directory already exists errors
            pass
        else:
            raise