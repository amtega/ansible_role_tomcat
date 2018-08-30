# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


def tomcat_startswith(str, strings):
    """Test if a string start with one of the specified strings.

    Args:
        str (string): strings to check
        strings (list): strings to match with

    Returns:
        bool: true if the string match with any of the list.
    """
    for s in strings:
        if str.startswith(s):
            return True
    return False


class TestModule:
    """ Ansible tests """

    def tests(self):
        return {
            'tomcat_startswith': tomcat_startswith
        }
