********************************
Developing network_cli platforms
********************************

.. contents:: Topics

Updated: 27-Nov-2017

Overview
==========

The document provides details on how to implement a module using the new
network_cli connection plugin.  This document exists in the ``ansible/community`` namespace to allow quicker updates based on feedback from Partners. Once the documentation is stable it will be moved to ``docs/docsite/rst/dev_guide`` in the main Ansible GitHub repository.

Starting in Ansible 2.5 ``network_cli`` is a new first-class connection plugin to replace the ``connection: local``  functionality that was available in Ansible 2.2 through 2.4.

As the Ansible network team begins the transition towards implementing the
network_cli connection plugin, we wanted to provide a sample implementation
for module developers to use as a guide.

Requirements for network module developers
==========================================

Any `new` network CLI *platforms* added in Ansible 2.6 MUST:

* be developed to support network_cli.
* NOT use top-level nor ``provider:`` (as they are both being deprecated)

Network *platforms* that `already existed` in Ansible 2.5 (or earlier):

* should be updated to support network_cli
* MUST continue to support ``provider`` until Ansible 2.9 (at the earliest)


Writing a module to support the use of the network_cli connection plugin is
quite a bit easier than the current effort necessary to support connection
local.  This example will touch on the three key pieces necessary to provide
support for a new network platform (operating system) in order to develop
modules that implement a network_cli connection.

This document will guide you through the files used to provide support to a
Cisco IOS device and shows the necessary code required to support the
platform using network_cli.

Components of network_cli
==========================

Terminal Plugin
---------------

The first thing that must be developed is a terminal plugin.  Terminal plugins
are maintained at
`plugins/terminal/ <https://github.com/ansible/ansible/tree/devel/lib/ansible/plugins/terminal>`_

The purpose of the terminal plugin is to hook the operating system to set up
the terminal environment.  The terminal plugin is responsible for providing the
list of terminal prompts to look for as well as authorize CLI sessions.  For
instance, switch to enable mode on a Cisco IOS device.

You can see the IOS terminal plugin `plugins/terminal/ios.py <https://github.com/ansible/ansible/tree/devel/lib/ansible/plugins/terminal/ios.py>`_

To support a new platform, the terminal plugin should be created and, at a
minimum, the instance variables ``terminal_stdout_re`` and ``terminal_stderr_re``
should be provided.  These instance variables are used to introspect the
response stream after a command is sent to determine if the stream has been
returned and/or if an error as been generated.

cliconf Plugin
--------------

Once the terminal plugin has been created, its time to move on to implementing
the platform cliconf plugin.  The cliconf plugin provides the basic set of
functions to be executed on the device.

Cliconf plugins are maintained at `plugins/cliconf/ <https://github.com/ansible/ansible/tree/devel/lib/ansible/plugins/cliconf>`_

The purpose of the cliconf plugin is to implement standardized calls for
platform features such as retrieving the output from commands and editing the
platform configuration.

You can see the IOS cliconf plugin `plugins/cliconf/ios.py <https://github.com/ansible/ansible/tree/devel/lib/ansible/plugins/cliconf/ios.py>`_

Network Module
--------------

Once both the terminal plugin and cliconf plugin are done its time write your
first module.  Writing network modules that use network_cli connection plugin
are straight forward and easy.

You can find an example of an ios_command module that implements the network_cli
connection plugin `modules/network/ios/ios_command.py <https://github.com/privateip/ansible/blob/network-cli-example/lib/ansible/modules/network/ios/ios_command.py>`_

In the above module, the key is to import the Connection object from module_utils and
create an instance of Connection.  This will give you access to the network device
cliconf methods.  Then its just a matter of writing the logic for your module.

Notice in the above code lines 61 and 62.  Those lines are responsible for
using the network_cli connection plugin to send and receive commands and
responses from the device.

Action Plugin
-------------

Action plugins are no longer required when using network_cli

Testing
=======

To use the new module, the playbook might look something like this::

  ---
  - hosts: ios01
    gather_facts: no
    connection: network_cli

    tasks:
      - ios_command:
          command: "{{ item }}"
        loop:
          - show version
          - show running-config


`Playbook output <https://gist.github.com/privateip/27177caa90005a59219c91bffeeac3d5>`_


Just a quick recap, there are only 3 files necessary to add support for a new
platform that uses network_cli connection plugin:

* ``plugins/terminal/{{ ansible_network_os }}.py``
* ``plugins/cliconf/{{ ansible_network_os }}.py``
* ``modules/network/{{ ansible_network_os }}/{{ ansible_network_os }}_command.py``

Once the first module has been added, subsequent modules only require the
module code.


For more information please join ``#ansible-network`` on `irc.libera.chat <https://libera.chat/>`_
