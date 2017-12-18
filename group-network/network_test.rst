********************************
Adding tests for Network modules
********************************

.. contents:: Topics

Overview
========



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

Certain platforms support 


For more information please join ``#ansible-network`` on Freenode IRC


Running network integration tests
=================================

Setup inventory

.. code-block:: console

   ansible-test network-integration  --inventory ~/myinventory -vvv vyos_facts
   ansible-test network-integration  --inventory ~/myinventory -vvv vyos_.*

