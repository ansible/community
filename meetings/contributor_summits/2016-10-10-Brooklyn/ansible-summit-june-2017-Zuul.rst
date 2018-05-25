Ansible Contributor Summit- Zuul
================================

21-06-2017

********************************************************
Follow up session on Thursday 22nd June
11am
Room: Riverview 9 (UK 2nd floor)

Riverview 9 is on the floor above the main meeting rooms.
Ask at AnsibleFest registration desk if you need further directions
********************************************************

IRC: #ansible-meeting


Zuul Ansible Contributor Summit
===============================

Main Agenda Topics
==================

* Mildly Deeper Dive
* Zuul Automerge
* Deeper discussion on rollout steps/logistics
* All the Dirty Hacks

Don't really want to touch TODAY:

* Tower Integration
* Galaxy/Role Integration

Mildly Deeper Dive
==================

Zuul's job is to respond to events, prepare git repo state, procure nodes
to run tests on, execute ansible playbooks against those nodes and report
the results.

Simple architecture
===================

* Scheduler - receives events, schedules work, reports results
* Nodepool - provides build nodes to Executors from Nodesets defined in jobs
* Executors - Prepare git content, ansible config and run ansible
* Nodes - Executor puts nodes into inventories

With a few exceptions, content is intended to run REMOTELY on nodes, not on
Executors.

Scheduler is not yet distrubuted or scale-out. Everything else is.

Trusted vs. Untrusted
=====================

* Jobs defined in an untrusted repo updated job config based on PR content
* Jobs defined in trusted repos update job config only post-merge
* Untrusted jobs cannot request access to secrets

Multi-Repo (or even single repo) dependencies
=============================================

https://github.com/j2sol/z8s-sandbox/pull/2

::

  Depends-On: https://github.com/j2sol/z8s-sandbox/pull/1

OR

::

  Depends-On: https://github.com/j2sol/z8s/pull/1

OR

::

  Depends-On: https://review.openstack.org/#/c/475985/


Github App
==========

* Integration is done via the Github "App" interface

  * Looks like shippable or travis

* App is added to the repo
* Responds to events, reports back

Triggers
========

* Pushes (heads and tags)
* PRs
* Labels
* Comments
* Reviews
* Status

Reports
=======

* PR Comments
* Commit Status
* Set Labels
* Merging PRs

Shared Jobs
===========

* Job Content is defined in git repos
* git is distributed
* Zuuls can consume shared git repos with shared jobs

  * Example: "run tox -epy27"

Zuul Automerge
==============

* Fundamental to Zuul design - optimistic branch prediction
* If we want automerge, we should aim at Zuul owning it
* Discuss current direct push/merge access

Important Lessons Learned from Seven Years of Gated Automerge
=============================================================

* Flaky tests are death
* zuul will correctly, consistently and confidently run terrible tests
* At scale, interaction with remote services == flaky tests
* Bypassing the gate is like relabelling a rubik's cube

Rollout Steps and Logistics
===========================

Step One: OpenStack Zuul
========================

* OpenStack Zuul running jobs on Ansible
* Limited to Zuul/Ansible and Ansible/OpenStack interaction

  * Keep early noise to a minimum
  * Don't abuse donated OpenStack resources too much

* Totally in-scope from an OpenStack BoD perspective
* Jobs defined in ansible/ansible repo

OpenStack Zuul Outcomes
=======================

* Exposure to job definitions
* Exposure to results reporting
* Collaboration with Testing Working Group on shared Job Structure
* Don't have to run one yet

Step One point Five: BonnyCI + ansible-container
================================================

* BonnyCI is a Zuul v3-based service
* ansible-container is reasonably self-contained
* Adds more exposure to zuul operations for Ansible humans

Step Two: Ansible Zuul
======================

Operations:

* Who?
* Where? - control plane
* Where? - build resources
* When?

Repos:

* git.openstack.org/openstack-infra/zuul-jobs for shared standard jobs
* github.com/ansible/zuul-jobs for "trusted" job definitions

Who - Options
=============

* Ansible org runs a Zuul
* RH Software Factory Team runs a Zuul
* Use BonnyCI service / partner with IBM somehow

All the Dirty Hacks
===================

* Log streaming for command/shell tasks
* Ansible-level Restricted environment for Untrusted Jobs
* Callback plugin mushy API

Log Streaming
=============

* Ansible module called "zuul_console"

  * First task in first pre-playbook of base job
  * Forks daemon process to stream command output
  * Forks from ansible module to avoid installing software

* Fork of command module

  * Combines stdout/stderr (need interleaved output)
  * Adds host-side timestamps
  * Sends to zuul_console

* Callback plugin "zuul_stream"

  * Intercepts stdout from command tasks
  * Spawns streaming client thread, logs lines

* Log streaming to client

  * Finger protocol over port 79 - finger {jobid}@ze01.openstack.org
  * Websocket gateway for real-time web streaming
  * Reads from output from "zuul_stream"

Ansible-level restricted Environment
====================================

https://git.openstack.org/cgit/openstack-infra/zuul/zuul/ansible/

NOTE: Zuul ALSO wraps execution in bubblewrap

* Untrusted jobs are not allowed to have ansible _plugins dirs
* Zuul plugins that override core action and lookup plugins

  * In most cases, zuul action/lookup plugins subclass core plugins

* Some are just straight blocked with raise Exception
* Some have input values filtered. For example:

  * sync is ok if it's targetting local workspace dir
  * sync is not ok if it's targetting other dirs

