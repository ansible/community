# AnsibleFest SF Contributor Summit, Networking Sessions

Sept. 6, 2017: 1-3pm, 3-5pm PDT

IRC: #ansible-network

## Discuss Ansible v2.5 roadmap

* https://github.com/ansible/community/wiki/Network%3ACore-roadmap-2.5
* Needs more detail
* What needs turning into proposals
* ACTION: EVERYBODY HERE to review this

## Developing networking modules +1+1

* Verb usage - How to be , absent, present
* Define declaritive
* User facing docs for aggregate intent: https://github.com/ansible/ansible/pull/26954/files
  * Does the term aggregate make sense
* What is the long term vision for declarative intent
  * What is the long-term meaning/plan for declarative intent (i.e. a bunch of feature specific modules)?
  * Q: Is this wanting to be common across all platforms
* Platform Agnostic
  * What's needed to support minimum viable platform agnostic (MVPA) modules+4
  * Q: There was a feel that
  * Peter to give overview about future of platform agnostic
* Add new argument to `net_interface` & one platform
  * Added to one platform
  * Double check on Ricky implementation on the above
  * If two people have created option, but they are doing something different...
* **ACTION:** Mark Platform agnostic as tech preview
* **ACTION:** Partners to join discussion in IRC

## Enabling declarative intent

* User facing docs for Declaritive Intent: https://github.com/ansible/ansible/pull/26954/files
* ACTION: Update modules to add comment for state (`net_interface`) doesn't make it clear which are config vs intended status
* status
* oper
* validation
* with_ loop
* AGREED: Will create proposal and discuss

## Enabling persistent connection framework +1

## A persistent connection framework for HTTP/REST based APIs

* Either a standard way for modules to pass tokens (through facts and parameters)
* Or a built-in framework in Ansible that provides auth/token information through a back-channel
  * How does authentication and tokens work when provider goes away?

## Playbook writing best practices (setting provider, vars, etc.)+1

## Documentation

### Provider

* Module docs don't list provider
* Very few people use ssh keys

### Top level user docs

* Link to use cases
* Link to debug
* Link to Network module index
* Link to Filters
* Link to Marketing site

### Use Cases

* Getting started
* **Agreed:** Don't document ansible ad-hoc
* **Agreed:** Link to yaml basic http://docs.ansible.com/ansible/latest/YAMLSyntax.html
* Components of Ansible
* Variables
* Getting access to variables that are under a different host
* Inventory
* **Agreed** Hello world https://github.com/Dell-Networking/ansible-dellos-examples/blob/master/getfacts_os10.yaml

  * Include credentials in same file
  * `get_facts`
  * register & debug
  * _command show version
  * set hostname
  * Credentials will be specified in file

**Agreed** Write switch config to file

use Copy module

**Agreed**: Interface filter

Show how to filter to only show which interfaces are up

### Better error messages

* Unable to open shell
* AVI: Debug and return information for modules, real time feedback

### Sharing and linking content

* Sharing documentation and examples -> push to docs.ansible.com?
* New 2.4 Networking tech guides +1
* New content
* Sample playbooks & gists
* Youtube videos
* Training resources+1
* How to's like https://github.com/ansible/ansible/pull/28856 - wrong PR?

Questions

* Who will be creating the content
* What are the target audiences
* Who maintains ths content

## Credential management+1+1

## Horizontal & Vertical Scaling best practices (for control nodes and tower)

* Specific to network, given the qty of data retrieved from network device are > from compute nodes
* Local connection implications to sizing
* Forking/strategies best practices

## Building Community

* Use of #ansible-network
* How to promote
* **AGREED:** Use IRC for meetings and general discussion
* ACTION: Get ansible-devel & ansible-network logged (notice given on join)
* Testing update
* Current (2.4) requirement
* Pre-merge Shippable
* (future) Pre-merge Zuul
* (WIP) Post merge DCI

## Getting stdout logging back issue #26809

* https://github.com/ansible/ansible/issues/26809
* So there's a long-standing idea to allow modules to return information in realtime back to Ansible (which could be shown as part of a specific verbosity)
* This is also needed for e.g. the Windows modules to show some of the communication channels in real-time

## Cover the current testing processes. How CI and unit tests are accomplished.

