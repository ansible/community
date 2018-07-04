********************************
Network Roles Development Process
********************************

.. contents:: Topics

Overview
========

This document is intended to outline the development process for Ansible Network Roles.

If you are an end user and wish to 



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

* Add tests for py2 and py3 to https://github.com/ansible-network/ansible-zuul-jobs/blob/master/zuul.d/jobs.yaml
* Update https://github.com/ansible-network/network-engine/blob/devel/.zuul.yaml so the new version of Ansible is tested on the `devel` branch of the role

* Add new `ansible-role-tests-2.6-py2` test to https://github.com/ansible-network/ansible-zuul-jobs/blob/master/zuul.d/jobs.yaml
* https://github.com/ansible-network/network-engine/blob/devel/.zuul.yaml
* Do a `recheck` on all open PRs

Release Procedure
-----------------

To version the roles in Galaxy we use Git Tags

FIXME Move details here from gdoc

Process for Ansible major version update
----------------------------------------

When the next major version of Ansible is released the following process needs to happen

Using the release of Ansible 2.6.0 as an example:

* Ensure the current `network-engine` integration tests pass when run against Ansible 2.6.0 - If not fix in `devel` (remembering to update changelog)
* Branch `stable-2.5` from `devel` - We don't expect this branch to change unless critial bugs are found.
* Ensure branch is protected in GitHub (this allows Zuul to run)
* If required, restrict who can commit
* network-engine's `devel` branch is now for the current stable Ansible release. 
* Create ``changelog/fragments/v260-initial.yml`` with `major_changes` entry
* ``git add changelog/fragments/v260-initial.yml && git commit changelog/fragments/v260-initial.yml``
* ``meta/main.yml`` update to be ``min_ansible_version: 2.6``
* Ensure local changes are committed
* ``git tag -a v2.6.0``
* Follow Role release procedure
