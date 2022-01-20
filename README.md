# Ansible tomcat role

This is an [Ansible](http://www.ansible.com) role which setups tomcat application server.

## Role Variables

A list of all the default variables for this role is available in `defaults/main.yml`.

## Example Playbook

This is an example playbook:

```yaml
---

- hosts: all
  roles:
    - role: amtega.tomcat
      vars:
        tomcat_name: server1
        tomcat_version: 8.0.9
        tomcat_home: /opt/apache-tomcat-8.0.9
        tomcat_base: /srv/tomcat/server1
```

## Testing

Tests are based on [molecule with docker containers](https://molecule.readthedocs.io/en/latest/installation.html).

```shell
cd amtega.tomcat

molecule test --all
```

## License

Copyright (C) 2022 AMTEGA - Xunta de Galicia

This role is free software: you can redistribute it and/or modify it under the terms of:

GNU General Public License version 3, or (at your option) any later version; or the European Union Public License, either Version 1.2 or – as soon they will be approved by the European Commission ­subsequent versions of the EUPL.

This role is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details or European Union Public License for more details.

## Author Information

- Juan Antonio Valiño García.
- Partially based on [daniel-rhoades.tomcat role](https://galaxy.ansible.com/daniel-rhoades/tomcat).
- Partially based on [groover.tomcat role](https://galaxy.ansible.com/groover/tomcat).
