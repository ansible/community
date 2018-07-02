********************************
Network Roles Development Process
********************************

.. contents:: Topics

Overview
========





Versioning
==========

Ansible Network Roles are designed and tested to follow the stable Ansible releases.

They are not to be used with the `devel` version of Ansible/

Example 1
---------

`network-engine` release 2.5.3

* Supports Ansible 2.5.*
* Is the 3rd update to this role since supporting Ansible 2.5

Process when Ansible branches stable-x.y
----------------------------------------

Aim: Ensure that all Network Application Roles are tested against `devel` and the next `stable-x.y` branch

* Add new `ansible-role-tests-2.6-py2` test to https://github.com/ansible-network/ansible-zuul-jobs/blob/master/zuul.d/jobs.yaml
* https://github.com/ansible-network/network-engine/blob/devel/.zuul.yaml
* Do a `recheck` on all open PRs

Process for Ansible major version update
----------------------------------------

When the next major version of Ansible is released the following process needs to happen

Using the release of Ansible 2.6.0 as an example:

* Ensure the current `network-engine` integration tests pass when run against Ansible 2.6.0


* network-engine's devel branch 
