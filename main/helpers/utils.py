from fnmatch import fnmatch
from main import config


def check_email_allowed(string):
    if not any(fnmatch(string, match) for match in config.options['blacklist']):
        if config.options['whitelist']:
            if all(fnmatch(string, match) for match in config.options['whitelist']):
                return True
            else:
                return False
        else:
            return True
    else:
        return False