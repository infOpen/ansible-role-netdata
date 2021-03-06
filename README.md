# netdata

[![Build Status](https://img.shields.io/travis/infOpen/ansible-role-netdata/master.svg?label=travis_master)](https://travis-ci.org/infOpen/ansible-role-netdata)
[![Build Status](https://img.shields.io/travis/infOpen/ansible-role-netdata/develop.svg?label=travis_develop)](https://travis-ci.org/infOpen/ansible-role-netdata)
[![Updates](https://pyup.io/repos/github/infOpen/ansible-role-netdata/shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-netdata/)
[![Python 3](https://pyup.io/repos/github/infOpen/ansible-role-netdata/python-3-shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-netdata/)
[![Ansible Role](https://img.shields.io/ansible/role/25354.svg)](https://galaxy.ansible.com/infOpen/netdata/)

Install and configure netdata package.

## Requirements

This role requires Ansible 2.2 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Xenial

and use:
- Ansible 2.2.x
- Ansible 2.3.x
- Ansible 2.4.x
- Ansible 2.5.x

### Running tests

#### Using Docker driver

```
$ tox
```

## Role Variables

### Default role variables

``` yaml
```

## How ...

### ... manage main configuration

> You can manage main configuration file using ini format

``` yaml
netdata_main_configuration_items:
  - section: 'foobar'
    option: 'foo'
    value: 'bar'
```

### ... manage plugins configuration

> To avoid hard regex or errors, when you want a specific configuration for a plugin,
> you need to manage all its configuration using *content* key

``` yaml
netdata_plugins_configuration_items:
  - path: 'python.d/squid.conf'
    content:
      foo: bar
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: infOpen.netdata }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
