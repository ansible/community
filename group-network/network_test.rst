********************************
Adding tests for Network modules
********************************

.. contents:: Topics

Overview
========

This page details some of the network specific areas of testing. It should be read along side the main testing documentation http://docs.ansible.com/ansible/devel/dev_guide/testing.html

Integration Tests
=================

Structure
---------



Each test case should generally follow the pattern:

* setup —> test —> assert —> test again (idempotent) —> assert —> teardown (if needed) -> done

* This keeps test playbooks from becoming monolithic and difficult to troubleshoot.

* Include a name for each task that is not an assertion. (It’s OK to add names to assertions too. But to make it easy to identify the broken task within a failed test, at least provide a helpful name for each task.)

* Files containing test cases must end in ``.yaml``



Implementation
--------------

For platforms that support ``connection: local`` *and* ``connection: network_cli`` then can be tested using the following:

* Targets directories are named after the module name
* ``main.yaml`` should just reference the transport 

``test/integration/targets/ios_config/tasks/main.yaml``

.. code-block:: yaml

   ---
   - { include: cli.yaml, tags: ['cli'] }


``test/integration/targets/vyos_banner/tasks/cli.yaml``

.. code-block:: yaml

   ---
   - name: collect all cli test cases
     find:
       paths: "{{ role_path }}/tests/cli"
       patterns: "{{ testcase }}.yaml"
     register: test_cases
     delegate_to: localhost
   
   - name: set test_items
     set_fact: test_items="{{ test_cases.files | map(attribute='path') | list }}"

   - name: run test cases (connection=network_cli)
     include: "{{ test_case_to_run }} ansible_connection=network_cli"
     with_items: "{{ test_items }}"
     loop_control:
       loop_var: test_case_to_run

   - name: run test case (connection=local)
     include: "{{ test_case_to_run }} ansible_connection=local ansible_become=no"
     with_first_found: "{{ test_items }}"
     loop_control:
       loop_var: test_case_to_run
       
       
.. code-block:: yaml

   ---
   - debug:
       msg: "cli/basic-no-login.yaml on connection={{ ansible_connection }}"

   - name: Setup
     vyos_banner:
       banner: pre-login
       text: |
         Junk pre-login banner
         over multiple lines
       state: present

   - name: remove pre-login
     vyos_banner:
       banner: pre-login
       state: absent
     register: result

   - debug:
       msg: "{{ result }}"

   - assert:
       that:
         - "result.changed == true"
         - "'delete system login banner pre-login' in result.commands"

   - name: remove pre-login (idempotent)
     vyos_banner:
       banner: pre-login
       state: absent
     register: result

   - assert:
       that:
         - "result.changed == false"
         - "result.commands | length == 0"


       
Become
------

Certain platforms support support ``enable`` mode.

The user facing documentation for this feature can be found at http://docs.ansible.com/ansible/devel/become.html#become-and-networks


Testing enable & become on platforms that existed on 2.4  (and earlier)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In addition to setting ``enable:`` (and optionally ``enable_pass``) in the ``provider`` you must also set ``become:``

To allow the tests to run with ``connection: network_cli`` and ``connection: local``

.. code-block:: yaml

   - name: Turn on all endpoints
    eos_eapi:
       enable_http: yes
       enable_https: yes
       enable_local_http: yes
       enable_socket: yes
       provider: "{{ cli }}"
     become: yes
     register: eos_eapi_output
     
Testing become on modules added in 2.6 (and later)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For platforms added in 2.6 (and later) there shouldn't be a ``provider``, so simply set ``become:`` as part of the task.



Running network integration tests
=================================

Create an inventory file that points to your test machines. The inventory group should match the platform name (``eos``, ``ios``, ``vyos``, etc).

The tests can be ran by doing:


.. code-block:: console

   ansible-test network-integration  --inventory ~/myinventory -vvv vyos_facts
   ansible-test network-integration  --inventory ~/myinventory -vvv vyos_.*


See also the integration testing docs at http://docs.ansible.com/ansible/devel/dev_guide/testing_integration.html#network-tests

Code Coverage
=============

Code coverage data can be collected locally.  This is a great way of finding gaps in test coverage.

When running ``ansible-test network-integration`` simply add the ``--coverage`` command line argument

Note for the first run you may also need to specify ``--coverage --requirements`` to install the needed dependencies via PIP.

After the raw coverage data has been collected you can render the report into html by doing::

   ansible-test coverage html
   
To clear the results between runs, simply do:

   ansible-test coverage erase
   
More information can be found at http://docs.ansible.com/ansible/devel/dev_guide/testing_running_locally.html#code-coverage


More info
=========
For more information please join ``#ansible-network`` on Freenode IRC
