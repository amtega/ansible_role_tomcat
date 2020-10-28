#!/usr/bin/python
# -*- coding: utf-8 -*-

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from xmltodict import parse
from traceback import format_exc


def main():
    module = AnsibleModule(argument_spec=dict(path=dict(type=str,
                                                        required=True)))

    path = module.params['path']
    try:
        with open(path) as xml_file:
            data_dict = parse(xml_file.read())
            xml_file.close()

        module.exit_json(
            changed=False,
            dict=data_dict,
        )
    except Exception as e:
        module.fail_json(msg=str(e), exception=format_exc())


if __name__ == '__main__':
    main()
