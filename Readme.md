[![tests](https://github.com/boutetnico/ansible-role-innotop/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-innotop/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.innotop-blue.svg)](https://galaxy.ansible.com/boutetnico/innotop)

ansible-role-innotop
====================

This role installs [Innotop](https://github.com/innotop/innotop).

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)

Role Variables
--------------

| Variable                     | Required | Default                  | Choices   | Comments                         |
|------------------------------|----------|--------------------------|-----------|----------------------------------|
| innotop_version              | true     | `1.13.0`                 | string    |                                  |
| innotop_packages             | true     |                          | list      | See `defaults/main.yml`.         |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-innotop

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
