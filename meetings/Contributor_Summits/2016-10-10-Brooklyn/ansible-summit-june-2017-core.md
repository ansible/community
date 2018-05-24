# Ansible Contributor Summit - Core update
21-06-2017

Topic: Core Update
Video conference link (BlueJeans): https://bluejeans.com/3008457278/
IRC: #ansible-meeting
IRC Meeting Logs link: (Please post afterwards)

Subtopics from original planning etherpad (https://public.etherpad-mozilla.org/p/ansible-summit-june-2017):

## Progress

* 10 minute summary of what action items were accomplished from last contributor summit (since we didn’t do action items in the past… I remember, the core-extras merge and how it will enable community to do more/core to be less of a bottleneck to be a theme).  Docs was a theme because of their break out session).

* Contributor Docs update

  * We know they need love
  * A new structure has been decided on, docs will be ported to docs.ansible.com/ansible/community

## Python 3 status: Where we are.

* Needs integration/unit tests to prevent regressions and find bugs
* Mostly usable now among core modules.  Test, file bugs or PRs. Talk to abadger1999/Toshio if you need information on proper way to fix a bug or any help to expedite a PR
* Ansible 2.4 has moved to Python-2.6 as new minimum version.  can remove some py3/py2 boilerplate from code (like get_exception)
* Could add other boilerplate (from __future__ imports, __metaclass__ = type)
* Python notes from planning pad:

  * remove python 2.6 support

  * -1 (dag) RHEL6, older Unix, appliances and other devices may still require older python versions. Please do not deliberately shut them out (for stuff already working)
  * python 2.6/2.7 support is here for a while, there are too many systems that are still operating with these as default/only option, same reason we kept 2.4/2.5 support for soo long (bcoca)
  * (abadger agrees with bcoca on supporting 2.6/2.7 for a long time.)  We can keep the policy of "if the module uses libraries which only are supported on a newer python, we can require that."
  * Maybe add a policy that it is no longer mandatory to support 2.6, but still accept changes to support python 2.4 or python 2.6 if it doesn't influence the style and/or complexity of the module
  * python 2.4 is already broken in Ansible 2.4 if the modules are using module_utils/basic.py (bcoca)
  * Any interpreter can be supported by specific modules, they just cannot rely on the 'official' shared code in module_utils/
    * Yeah, and exactly that is a real problem IMO.
  * how about we treat python < X similarly to router / cloud platforms - you manage it but don't run code there directly . or other metaprogramming ideas [mikedlr]

* Need to increase test coverage to give Python 3 confidence

## Certified modules (may overlap with testing.)

* What they are/will be
* What requirements we want to have to be certified

  * Have two community maintainers
    * -1 more maintainers does IMHO not necessary indicate good quality (resmo)
    * Must be maintained? (there may be some road warriors doing a good job in maintaining modules) (resmo)
    * How to assess if maintainers are still active ? (see maintainer responsibilities and expectations, and module metrics)
    * (bcoca) more maintainers increases probability of support, but agreed, does not ensure quality nor responsiveness
    * Things being stuck in the PR queue does not ensure quality nor responsiveness, but does increase frustration, people not longer caring, and more support issues
    * -1 number don't make quality
    * It may as well be the opposite, a lot of PRs improving/fixing modules get stuck because we lack maintainers to review/approve
    * Two or more maintainers proved to work together well (then +1)
    * Agree with above comments that having two people is more difficult than one.  However, if you can do it and they are from separate companies then that tends to prove that the software is more maintainable. [mikedlr]

Ansible internal documentation is being worked onhttps://github.com/ansible/ansible/commit/fa31043e7ee2a9fc74ccc39ddeb43587c2fea6d3

