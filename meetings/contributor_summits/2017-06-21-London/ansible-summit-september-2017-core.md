# AnsibleFest SF Contributor Summit, Core Session (9am-11am PDT)

IRC: #ansible-meeting

## bcoca's playbook bundle/ installer proposal (gdk via thaumos)

* Can we have a minimal installer with certain modules?
* Modules that are vetted better
* bcoca working on playbook bundle / installer "thing" https://github.com/bcoca/playbook_bundle (draft skeleton)
* We want to avoid "yet another package manager" and leverage Ansible instead
* This is "proposal written" and thaumos will update with link
* jlk: can we customize what that minimal set of modules is? thaumos: yes, it will leverage Ansible config (which we're discussing later today) and other stuff in 2.5 that are prereqs for this
* Also a "kitchen sink" package that delivers ALL THE MODULES (this is current package)
* mckerr: not just about installing, but also delivering more variable content
* jag: another possible direction: bringing pre-baked playbooks into bundles (make me an ec2 server! upgrade a db!)
* OpenShift's Ansible (only in name) Playbook Bundles: https://github.com/ansibleplaybookbundle/ansible-playbook-bundle
* thaumos: not going to be 100% 2.5 thing
* What makes us nervous?
  * toshio: proposal has a playbook that delivers the module and runs depsolver, which means it's up to the packager to decide, and there are no restrictions on the playbook. Good: we don't have to maintain code. Bad: we care about the deps *everywhere*, and the packagers may not care so much -- they'll only care about the deps on their machine.
  * bcoca: kitchen sink still doesn't solve dependent library problem.
  * bcoca: note that this isn't in "ansible" -- it's an optional helper convention that people can choose to follow
  * gdk: what's the diff between this and a role? bcoca: roles don't have specific targets, and can't be run directly, they need a wrapper playbook
    * jimic: not entirely true: `ansible -m include_role -a 'name=foo' localhost` (how many people know this?) <- the ones who read the docs
    * jimic: Also, we're talking about having bundled playbooks, so we're already going to have playbooks that wrap something?
  * toshio: we could write the installer to unbundle a role instead
  * mattclay: Ansible will be responsible for providing and supporting bundles for modules supported by Ansible.
    * bcoca: These modules would not use bundles but would install their dependencies as part of the module execution.
  * Who's providing the bundles, and how can we guarantee their stability?
  * belanger: "bindep" does this in the Openstack world, run bindep first which takes dep list and generates a list of stuff to be installed (only works with system packages at present)
    * https://docs.openstack.org/infra/bindep/
    * Examples: https://docs.openstack.org/infra/bindep/readme.html#examples
  * How do we deliver? Maybe galaxy client, maybe tarball
  * The ultimate goal is to split out the modules. Is this the best proposal for that ultimate goal? Is a depsolver needed?
  * gdk: what are the steps to get us down this path in the nearer term?
  * mclay: risk is that customers can only get bundles for things they don't ship

## Finishing config (bcoca)

* we already have some feedback
* config was organic growth, we used config stuff from everywhere, we're just normalizing it, now separated out config definitions into yaml (soon  config file is yaml!)
* plugins had to create their own config methods, now they can be defined in the plugin itself, also helps with the difficulty in documenting plugins
* new ansible config cli tells you how your config is actually set up
* "backwards compatible" for users, not if you were delving inside config api :)

  * your existing ansible.cfg's should work fine with no changes

## Core 2.5 roadmap (thaumos)

* Roadmaps: https://github.com/ansible/ansible/blob/devel/ROADMAP.rst
  * "2.4: We are starting to build the 2.4 Roadmap. We are seeking community feedback!" -- when are we posting the 2.5 roadmap? :D
* Finish Ansible Config (thanks bcoca!) need to finish
* Loop directive that fell out of 2.4 (with _*)
* Facts namespacing also dropped out of 2.4, need it in for 2.5
  * prepend Ansible facts with "ansible_facts"
* Possible: Allowing for abstraction of remote host platform that would give default for transport mechanism
* 2.4 introduced new inventory plugin methodology, in 2.5 we want to start migrating existing dynamic inventory for cloud platforms to new plugin mechanism, abstracts out the need to build grouping, would move into jinja templates instead
* Ansible-doc will extend to all plugins etc. (already in 2.4 to some plugin categories)
* Various engine/backend stuff
* Network: more stability work, refactor of network libraries into module_utils, more connection plugin stuff
  * https://github.com/ansible/community/wiki/Network%3ACore-roadmap-2.5 (feedback welcome via #ansible-network)
* Windows: use windows ssh maybe? (and other boring stuff lolz)
* All this will be posted into the public 2.5 roadmap in the next little while

## Getting community features onto the 2.5 roadmap?

* https://github.com/ansible/ansible/pull/23769
* dag: what about core proposals? if they're not in the same process, the community doesn't have the opportunity to review
  * A lot of this is about taking the time to communicate
* "Fix the process" by just saying "come to meetings and advocate for your proposal and that's it" -- maybe this is sufficient? COME TO THE MEETINGS COME TO THE MEETINGS COME TO THE FREAKING MEETINGS (also rotate the meetings)
  * Meetings sometimes are hard to get quorum to say yay or nay.
  * Meetings are at ridiculous o'clock (willthames)
* Can we extend the modules process to plugins?
  * shipit+automerge is possible, but it will likely create many of the same problems we currently have with the giant list of modules and expectations. I (jtanner) would like this to be solved with ansible-installer.
  * we can do this with botmeta currently, just need to tag entries
  * toshio: we should use the same workflow, but we should improve the workflow
  * can we just extend metadata to plugins?
* How can we promote a proposal from "good idea" to "on the roadmap"?
  * If we do this:
    * Make it clear what the actual gating requirements are (this is easier for the core team because of the tight knit nature of the team)
  * jimi: Are "approved" proposals something we should be advertising to new contributors looking for something to work on? We have previously talked about adding an "easy" tag for github to indicate something may be good for a beginner to the code base to tackle, perhaps that's something we should do even more so for proposals?
  * Aborted attempt to enhance the proposals process: https://github.com/ansible/proposals/pull/59
  * gregdek: really, we need to tell people how to keep a proposal from being stalled.  Even if it's just, show up at the meetings and discuss it there.
    * Process is important for things that need to scale like module review but proposals can be ad hoc in the meetings.
* What do we mean by "roadmap" -- we know there are core features, but how do we get community features that are not quite as central, on to some kind of roadmap?
  * Roadmap feeding into release notes
  * Process for modules, get enough shipits and it gets in.  Need to also have a process for plugins (and other module-like things)
  * There are things that Ansible is a blocker for getting in.  As long as we block then there needs to be a mechanism to get commitment from Core team to review and merge them
  * Stuff on the roadmap is not always advertised (and may surprise the community just before release, e.g. facts namespacing), more community involvement would produce a better result +1
  * BOTMETA https://github.com/ansible/ansible/blob/devel/.github/BOTMETA.yml

## A new module_utils API (replace basic.py)+1

* https://gist.github.com/abadger/3edc108f5a5b88c1a9a46c4869d778fd
* (Soon to be a proposal? Golly I hope so!)
* A more basic basic? minimal.py ?
* keep basic.py as backwards compatibility, move functionality out to other files but keep reference so custom modules can still work

## A holistic view on facts (gathering, selecting, management, customization) (@dag)

* Various proposals: https://github.com/ansible/proposals/issues/56 and https://github.com/ansible/proposals/issues/17
* https://github.com/ansible/ansible/blob/devel/docs/docsite/rst/roadmap/ROADMAP_2_4.rst#facts
* Fact namespacing: https://github.com/ansible/community/issues/162#issuecomment-319225132

## How to handle encodings for file contents (toshio)

* Will be a proposal, will mostly affect core modules
* Right now we pretend everything is UTF-8 which is fine except when it's not, and since we must accommodate those savages, we should let them do the totally wrong thing and specify an ancient encoding. And even that isn't enough! Sometimes people do truly ridiculous things, and we should accommodate everything?
  * 99% of the time, it works every time
* gdk: or not. -1! -1!
* dag: can we use jinja filters for this? toshio: no.
* bcoca: we still need to solve it, it wont be pretty no matter which option we take
