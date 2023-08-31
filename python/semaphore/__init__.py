
# pip package name
NAME = 'sdss_semaphore'

from sdsstools import get_package_version
__version__ = get_package_version(path=__file__, package_name=NAME)

from .flags import Flags, FlagsArray
from .reference import FlagReference