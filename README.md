Ansible role: gpii-version-updater
===========================

Minimal Ansible role to manage CentOS 7.3 worker nodes running the [GPII Version Updater](https://github.com/gpii-ops/gpii-version-updater). This includes some SSH configuration (private key delivered out-of-band).

Requirements
------------

 * CentOS 7.x
 * Ansible 2.x
 * systemd
 * [ansible-docker](https://github.com/idi-ops/ansible-docker)

Example Playbook
----------------

    - hosts: servers
      roles:
         - ansible-gpii-ci-version-updater

Tests
-----

Use [molecule](https://github.com/metacloud/molecule) to test this role.

Because this role depends on systemd and might one day need SELinux (as related role ansible-influxdb does), only a Vagrant provider is configured at the moment.

License
-------

MIT

Author Information
------------------

Raising the Floor - US
