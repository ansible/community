# 2016-02-17: Ansible Contributor Summit 1 (Part of AnsibleFest 2016 London)

* [Etherpad, with summary and pre-planning](https://public.etherpad-mozilla.org/p/ansible-summit)
* [IRC log](https://gist.github.com/gregdek/4ed5bd745881570a17db)

* [Video 1](https://www.youtube.com/watch?v=l7v7RSHwGhk)
* [Video 2](https://www.youtube.com/watch?v=47vidc1P-ZE)
* [Video 3](https://www.youtube.com/watch?v=c3WNhsHW7Xc)
* [Video 4](https://www.youtube.com/watch?v=qPuQ-UToen0)
* [Original BlueJeans Videos](https://bluejeans.com/playback/s/ZwEk1KT2CFZ3crqndexDVXeqGDwrEGAJXLxWrykZ8FvwxzjfqVlYuzBkTuwr2XhR)

##ACTION ITEMS

Testing:

    * bcoca owns separating current module-related tests into the module repos
    * bcoca owns creating the makefile to run those tests and discover new tests

Galaxy:

    * bcoca set up working group to sort out versioning and download
    * robyn will actually own the "figuring out open source galaxy" question

Ansible Core Contribution:

    * gregdek we need a "thou shalt not" list for core contributors

PR / issue workflow:

    * gregdek will figure out how we make sivel's excellent pr/issue tool a more well known part of the ansible workflow

Architecture:

    * gregdek will set up a docs sprint led by docschick and involving crab and core folks documenting architecture
    * gregdek will add a template for new proposals to ansible/ansible/docs/proposals

Extras New Modules:

    * gregdek will set up the Extras New Module review process and ask for volunteers to staff it :)

Other:

    * gregdek will find someone to document the addition (getting started) of our "best friend" tools
    * gregdek will have a bot added to #ansible-devel and #ansible-meeting
    * gregdek will send a detailed instruction guide for ansibullbot and that it actually exists


## ORIGINAL ETHERPAD DOC FOLLOWS

 CONTRIBUTOR SUMMIT DETAILS

When: Wednesday, February 17, 10AM-5PM (GMT) (Convert to your time zone here: http://bit.ly/1V1v1P4)
Location:

    InterContinental London - The O2
    1 Waterview Dr, London SE10 0TW, United Kingdom
    in the InterContinental Meeting Room - Arcadia Two
    (closest tube stop: North Greenwich)

Flow of day:

* 9-10AM: Breakfast and registration
* 12-1PM: Lunch in the Cutty Sark Room
* 2:45-3PM: Afternoon break
* 5PM: End of event and leave for Ansible Social (will provide directions)
* Precise agenda TBD: see topics below

Top sessions with votes:

    * Testing (+10)
    * New modules in extras (+8)
    * PR Process for Ansible/ansible - +7
    * Roadmap +7
    * Issue triage +7
    * Galaxy (+8)
    * Technical board (+5)

Loose schedule: (5.75 hours)

* 10-12 (3 topics)
    * Intro: Why we're here, and what we're gonna do about things (15m)
    * Roadmap https://github.com/ansible/ansible/blob/devel/ROADMAP.md
    * Testing
    * PR Process for Ansible/Ansible
* 12-1 lunch
* 1- 2:45 (3 topics)
    * Galaxy
    * Issue Triage
    * New Modules in Extras
* 2:45-3 is a snack break
    * 3-5 (Technical board discussion, open floor & wrapup)



----------------------------------------------------------------------------------------------------------------------

## TOPICS FOR DISCUSSION AT ANSIBLE CONTRIBUTOR SUMMIT

(Please give +1 next to the topics you most want to discuss, add your topics at the bottom below.)

### PR PROCESS FOR ANSIBLE/ANSIBLE.  (+7 votes)

We have a more-or-less functional method for allowing community ownership of modules. Can we have a similar process for ansible/ansible? Should we use a similar process as for modules, with by-file or by-directory co-maintainers? Should we just give more people direct commit access?

* +1 (jlk)
* +1 (resmo)
* +1 (dag)
* +1 (willthames)
* +1 (AMS)
* +1 (svg)
* +1 (TonK)
* +1 (jhawkesworth)
* +1 (jmunhoz)

### ROADMAP.  (+7 votes)

Jason McKerr of Ansible will run this. What would you like to see here? How should we communicate the roadmap, and how should the community participate in the direction of the roadmap?

* +1 (robyn)
* +1 (mordred)
* +1 (dag)
* +1 (geerlingguy)
* +1 (AMS)
* +1 (svg - A recent example: I recently "found out" from irc and mails that Ansible as an API (as a library if you will) is not something that is supported - aside of discussing whether that is a good thing or not, this is one of the things that were never formally explained, imho. )+1
* +1 (wimnat) can we clearly document when dicussions have taken place, what the outcome was and when the issue should be reviewed.  For example, Ansible support for python 2.4.  The last dicussion was on x/x/xx.  The outcome was xxxx.  It will be re-reviewed on xxx +1+1
* +1 (jmunhoz)
* +1 (vincentvdk)

### ADMITTING NEW MODULES TO EXTRAS. (+8 votes)

We've got a large backlog of new modules. How to handle? A couple of proposals: #1. all new modules get checked for syntactical correctness, and if they are correct, they are merged into extras without further review. (sivel’s linter.)  #2: namespaces (windows/rackspace/docker/etc.) have their own approval processes with some kind of approval board. Namespaces without explicit approval processes could default to #1.

* +1 (robyn)
* +1 (jlk)
* +1 (resmo) fastrack for modules with integration tests?
* +1 (sivel)
* +1 (bassie)
* +1 (misc)
* +1 (wimnat)

    * I am not at all keen to just merge in extras modules as long as they an syntactically correct because I feel many modules miss some of the main goals of ansible, for example indempotency.  This is possible because Ansible does not clearly state things like this.  Also, only earlier this year we had 3 PRs for a module that did the same thing but were named differently.  What would prevent all 3 of these being merged if they were all syntactically correct?

* +1 (TonK)
* +1 (jhawkesworth)
* +1 (jmunhoz)

### ADMITTING NEW MODULES IN CORE.  (+3 votes)

The current rule is "it goes in when Ansible says so," because these are ultimately the modules that Ansible will be on the hook for supporting customers for. Should we have other criteria, and if so, what should they be?

* +1 (mordred)
* +1 (sivel)
* +1 (misc)
* +1 (jmunhoz)

maybe we could mail a formal request on ansible-devel together with the right justification to request the inclusion. this simple step could help to understand and speed up its inclusion by the core team

### ISSUE TRIAGE.  (+7 votes)

They're out of control and difficult to triage. Current proposal: all issues must adhere to a strict set of fields to be checked by a bot. Aggressive auto-closure of non-conforming issues. Potentially including open issues to be refiled. If the issue does not have those fields, they will be put into needs_info. If the issue stays in needs_info for X days, it will be auto-closed.

* +1 (robyn)
* +1 (dag - maybe have some bug-hunting days, would be useful to learn more about Ansible by learning from the experts)
* +1 (geerlingguy)
* +1 (willthames - much more transparent, streamlined review process - having to rebase multiple times between reviews is frustrating)
* +1 (AMS)
* +1 (svg a more formal review process, consider tools outside github, have a look at openstack review process - which is too heavy, but has some good principles -  and get the best ideas from there)
* +1 (TonK: This could also be a good idea for Meetups and Coder Dojo's)
* +1 (jhawkesworth) - The issue template is kind of buried in the community section of the site at the moment.  github not (yet) able to help with issue routing, labelling but is there any mileage in making a 'issue wizard' which would at least route issues to correct project and get issue creators to label (from a controlled list) issues.
* +1 (jmunhoz)
* +1 (vincentvdk - We did that during an ansible meetup in Utrecht (@TonK) which i found a good idea. But we need a minimal 'getting started' guide which explains how to work on an issue.

### EXTRAS MODULE ADOPTION PROCESS

How do we get modules without maintainers adopted by maintainers?

jmunhoz: when you receive a PR to include code we are aware of this person has the right skills to understand that module. Moreover this person should understand the contributing proccess more or less. Maybe in this point, suggesting the adoption of a similar module could work. It would require having the current modules classified with some similarity criteria.

### EXTRAS DEPRECATION PROCESS.

What are the criteria for deprecating modules? Do we deprecate modules without maintainters, or do we indicate somehow in Ansible that these modules are unmaintainted?

jmunhoz: I guess the first step could be writting down 'unmaintained' under the author field. This way, the contributor has not to wait a prudential time to know the module is not maintained and it is just a non responsive or busy author.

### DOCS LOCALIZATION

Can we enable this? We've got teams that have done some localization work, but because we have no policy recommendations, those efforts don't go very far. Should we provide guidelines? Say, fork the docs at a particular version, and we provide links to forks? How do we deal with localization of module docs -- can we even do that?

## TESTING.  (+10 votes)

Everyone agrees we need more testing. How do we do it? How do we plug into external CIs? Should passing tests be a criteria of core inclusion?

* +1 (robyn)
* +1 (jlk)
* +1 (mordred - also have some possibilities to offer here)
* +1 (resmo)  also, do new modules with integration tests require human testing?
* +1 (sivel)
* +1 (bassie)
* +1 (geerlingguy)
* +1 (AMS)
* +1 (svg - start with focus on testing lots of syntax things, avoid the accidental features and typical things that keep regressing e.g. yaml octal notations)+1
* +1 (TonK Agree with SVG)
* +1 (jmunhoz)
* +1 (vincentvdk)

### TECHNICAL BOARD.  (+5 votes)

Do we need a body of experts to discuss technical changes outside of GitHub? Is ansible-devel sufficient or do we need a separate mechanism for technical decision making? If such a board exists, how is it populated?

* +1 (jlk)
* +1 (dag - I would like a PEP like mechanism for ideas and feature development, with an authoritative voice giving advice)
* +1 (willthames - I like dag's idea)
* +1 (AMS)
* +1 (svg - more formal procedures for at least some things might help; also, this is related with roadmap stuff)
* +1 (jmunhoz - my opinion sits down with the svg one here)

### AMBASSADORS (+2)

We have 115 dedicated Ansible meetups around the world, plus countless people talking about Ansible at other events. How can we best share expertise and resources to make sure that everyone who wants to learn more about Ansible has that opportunity?
+1 (dag - It would be nice if there were sessions/documentation related to how the internals work, or maybe better documented internals)
+1 (TonK: Would be nice if we would be more active. Myself included. Better coorporation between Ambassadors would be a big plus)

### GALAXY.  (+7 votes)

What should be next on the Galaxy road map?

* +1 (mordred)
* +1 (drybjed - support for GitLab as alternative to GitHub?)+1(bcoca)+1(jmunhoz)+1(vincentvdk)
* +1 (jlk - improvements to galaxy cli commands to deal with shared roles and refreshing) +1 (drybjed)(+1 jmunhoz)
* +1 (bassie - developer mode - for instance extra flags to clone the source of roles for PRs)
* +1 (misc)
* +1 (geerlingguy - Also supporting BitBucket, GitLab (as drybjed suggested), and fix https://github.com/ansible/ansible/issues/11266 / https://github.com/ansible/galaxy-issues/issues/49)
* +1 (willthames - direct integration of roles installation into ansible-playbook, merging some of my open pull requests ;))
* +1 (chouseknecht - can we simplify or elimate Platforms in meta/main.yml. The list is long and a PITA to maintain.
* no plus one, just an idea: leverage Galaxy to also allow publishing modules - could bean alternative for the "extra's" - presumably a skeleton role would suffice for this since roles can include modules? yes they can, not only modules but all plugins (bcoca)
* wrapper roles? be able to layer a hierarchy of roles so that you can include say an upstream postgresql role but then replace a few defaults and a template file (for example) for internal use.
(TonK: A decent search function will be a big improvement. Also some kind of rating system, as discussed at CfgMgmtCamp will make it better)
* Make it possible to run my own galaxy server. I.e. open-source the server component, or at least document the most critical API endpoints - for what purpose? If just for internal roles hosting, simply point your rolesfiles at git/hg repos at a location of your choice (willthames)
* vincentvdk - Role versioning / on-premise deploy

### OTHER TOPICS. (svg-  I don't think we should discuss specific ansible features here ) (gdk - perhaps this points out the need for an architecture board +1)
If you have topics, please add them here!

* Strategies for supporting shared roles, plugins, modules, etc.. across multiple teams / playbook repos.(jlk) +1 (drybjed) +1 (misc) +1 (geerlingguy)
* Performance improvements (not large scale hosts, large scale tasks) (jlk)
* drybjed - support for signed local facts and their validation on ansible controller, this allows idempotent and trusted facts kept on remote hosts
* drybjed - update the official documentation to promote YAML syntax instead of inline syntax (could avoid issues like bare variables in the future) (+1 wimnat)
* drybjed - support for 'conf.d'-style playbooks/ directory, with files inside read alphabetically a'la run-parts, makes creation of shared environments easier. Problems with conflicting files: use special --playbook-dir option?
* misc - add more cows(+1 bcoca) what aboud bulls?
* More systematic commit/bugfix process for ansible/ansible (including commit messages, tests)
* svg: I'm missing some more fundamental topics here - most of the things here seem to focus on current work flows (PR process, issue trial) whilst we might want to question those to start with? (gdk +1 -- I agree with this. I wanted to focus on particular proposals, but if people think we're solving the wrong problems, then I'm open. Just want to make sure we don't end up with too much open-ended conversation that isn't actionable.)

    * Ansible is often said to be a victim of its own success - the overwhelming number of PR's as the obvious effect - perhaps the simple Github PR model is broken and is too easy and accessible for a successfull project like ansible.
overall design decisions: which by who and how? (see technical board ?)
    * How do we improve and then keep a watch on quality? (maybe dovetails with testing -- any specific proposal?)
development work flow issues - we need to stop with quick commits and even quicker reverts, committig code needs to be more formal, need a review process, need better ways to track issues, sometimes in multiple versions; instead of discussing who get's committ access, I'd argue no-one should have the right to commit to "master", consider making that a process (for ansible/ansible or modules or both?) (willthames: both - as svg says and AMS alludes to, everyone should be following a more rigorous approach, including core team)
    * Extra's module: some ideas - perhaps consider putting them in a separate package - perhaps allow new modules to start a life in Galaxy? (Extras will be in a separate package, hopefully in the 2.1 timeframe)
* wimnat - agree with svg above.  Address some of the more fundamentals.  What are the design principles of Ansible?  It seems some Ansible users would love one big complex module to do everything.  I'm personally against this and would prefer 5 modules to do 5 simple tasks rather than 1 complex module.  However, is this actually Ansible's stand point and where is it documented?(+1 bcoca)
* Any interest in Ansible taking over ansible-lint or ansible-inventory-grapher? i've 'wishlisted' ansible-inventory which should include grapher, lint is something we have been building into ansible-playbook(bcoca). You haven't though, not really - people want to be able to run ansible-lint for CI purposes and be able to turn on and off specific rules, and add their own inhouse rules. ansible-inventory sounds interesting, not sure why no-one has mentioned it to me.
ansible dot com vs. ansible dot org
* vincentvdk - Ansible scalability. I currently have no need for this, but it might be interesting for other people. something like having multiple ansible hosts from where you can trigger playbooks each targetting a certain part of your infra (this is just something i have been thinking about).  More documentation around this topic might be interesting..

### CLI - ansible and ansible-playbook

* Support for custom hook scripts before/after ansible-playbook starts, could be used to generate configuration
* drybjed - ansible and ansible-playbook use system-wide /etc/ansible/ by default, how about using $HOME/.ansible/ or even ./.ansible/ (a'la git)? (geerlingguy +1) (svg +1 but I don't think we should discuss specific ansible features here :) )(gdk +1)it already uses ~/.ansible.cfg by default (bcoca)
* confirg_merge = yes (default no) for ansible.cfg to allow a precedent config to read 'the next' one and use it for defaults it overwrites (~/.ansible.cfg has 3 settings takes rest from /etc/ansible/ansible.cfg)(drybjed - no, this will mess up a lot of configuration patterns like replacing group_vars/all/ variables with group_vars/group_name/ ones. Besides, there is a combine() filter now which can be used for the same purpose)
* vincentvdk - show diffs in ansible output for things like files/templates as an option.



