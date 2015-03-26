import errno

__author__ = 'David Salami'
import os
import json
import logging.config
import shutil
# def __init__(self):
# self.setup_logging(env_key="LOG_CFG")
# logger = logging.getLogger(__name__)
# logger.debug('foo')


def setup_logging(
        default_path='PyInfo.json',
        default_level=logging.INFO,
        env_key='LOG_CFG'
):
    """Setup logging configuration

        """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
        print(value)
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


def ignore_function(ignore):
    def _ignore_(path, names):
        ignored_names = []
        if ignore in names:
            ignored_names.append(ignore)
        return set(ignored_names)

    return _ignore_


def copy(src, dest):
    try:
        shutil.copytree(src, dest, ignore=shutil.ignore_patterns('*.py', '*.sh', 'specificfile.file'))
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)


def __Main__():
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.error('started copying')
    copy("C:\\Users\\David Salami\\Downloads\\Coreinfo", "C:\\Users\\David Salami\\Downloads\\A")
    logger.error('finished copying')

