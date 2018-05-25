# Ansible Contributor Summit Testing

21-06-2017

Topic: Testing

IRC: #ansible-meeting

Subtopics from original planning etherpad (https://public.etherpad-mozilla.org/p/ansible-summit-june-2017):

## Testing topics

* Mini-Zuul Update. No more than 10 minutes.
* Note: Beat Monty with Squirrels if he goes over time (Like seriously, 10 minutes. tops.)
* Content pasted in at bottom of etherpad
* Talk about upcoming next-steps for starting to run Zuul v3 jobs against ansible/ansible. Possible quick overview of status/shape - but more focused on "things potentially likely to happen in the next month or two" (mordred) (jlk)
* Other testing things

### Gundalow to do give quick overview of changes done

* 2.3 -> devel
* Integration tests +40% modules tested in CI
* Unit tests: +120%
* ansible-test
* Code Coverage
* AWS Tests
* CloudStack
* Network tests
* validate-modules (DOCUMENTATION & RETURNS)
* Raising the bar in 2.4
* All network modules MUST have tests
* How do we increase test coverage
* Looking for help with achieving this
* How to distribute the work to module maintainers (more integration tests, cleanup of modules)
* Document the priority
* PRs that add/update tests label:test_pull_requests
* Maybe initially filter out new modules, to increase existing coverage
* Table of all modules and which require external resources to test
* Tests that don't require external resources are much easier to test <- Work on these
* Core modules without tests
* module_utils with unit tests
* Test stability
* List tests that use external resources and document how to move to httptester (or equivalent)

How to consume functional test results from partner test infra in house. For example, I have a lot of existing test harnesses in house that I would like to report functional tests runs for because the modules I work on are for a product that is not free. I want to be able to send my results somewhere, even if it's not real-time.
+1 (spredzy)
+1 (alikins)

### Reference tests

Select reference integration tests and annotate them, so we can point to them from documentation and keep these in perfect shape (at all times)

* Standard: stat (though may updating)?
* Network: ?
* AWS: ?
* Windows: win_environment https://github.com/ansible/ansible/issues/20505
* Unit Tests:
* module_utils
* Action plugins

Do we need a simple example plus Something that shows how to do the complex bits like how to setup environment +1 (bjolivot)


* Don't let Shippable fail (and let ansibot sent out error information) for files that are not part of your PR
  * We now often get PEP8/sanity errors on files that are not even part of the commit, breaking everyone's workflow because someone pushed breakage directly to the devel branch (pretty frustrating)
  * Maybe everyone should be forced to work via PRs rather than push directly to the devel branch (+1 willthames) (+1 gundalow) (+1 alikins)
  * Integration tests as a way of doing proof of concept / verification of needed functionality ./ justifying it to your boss & client  - Michael
  * In my experience Shippable is having issues in almost 50% of the cases lately (docker issues, FreeBSD/MacOSX issues, one-off issues on a single target)
  * Users cannot trigger Shippable runs, so they have to close/re-open PRs or push amend-commits
  * The biggest frustration here is that it takes a lot of time for Shippable to finish and to find out why something failed (wading through Shippable targets and expanding logs)
  * Pro Tip: Click the "Test" tab on the left of Shippable, rather than looking at the "Console" tab
  * Maybe run sanity tests and PEP8 separate from the integration tests (e.g. Travis vs Shippable), so the feedback comes in quicker ?  (+1 alikins)
* Testing on Windows 10 and Windows 2016
* Show and tell
* Testing Docs
* Shippable Testing Tab
* Testing Working Group^W^WSIG

QUESTIONS:
* What are the pain points
* What would can we do to help

* Maybe talk about jctanner’s ansibot automerge: is it working well?  What in code or policy needs to be improved?  (For instance, sounds like two shipits by a maintainer might be a high bar)
* automerge CI tested modules? Based on coverage? Maintainer decision?  (resmo)
* CI is not enough to automerge, for me. I want to know code works, but sometimes there is a question as to whether code is even needed, or whether it's the right code. I'd be happy with CI being a vote towards merge, along with a trusted contributors 'shipit' (willthames)

  * +1
  * +1

* Zuul introduces capabilities that can lead to auto merge but still require both "CI" vote and a human approval. We should talk about this (we already have this topic listed above) (jlk)
* Let's be clear, if maintainers could influence automerge, a lot of issues (and some PRs) would not be created because the issue is fixed in devel and users would be happier overall. For (community) modules I don't see a good reason for not allowing this.
* isn't 'shipit' how maintainers influcence automerge?
* No, because there is no automerge atm, or at least it isn't working...
* (bcoca) afaik it is working, when x2 'shipit' from 'maintainers' for an PR it gets merged (owner/maintainer being author of PR counts as 1 already), non maintainers for that file do not get counted.
* Most modules do not have 2 active maintainers, it's hard to get one maintainer to sign off, so it isn't working in practice
* Better documentation about the CI (see https://github.com/ansible/ansibullbot/blob/master/ISSUE_HELP.md and https://github.com/ansible/community/blob/master/PR-FLOW.md)
* Pro Tip: Have you seen http://docs.ansible.com/ansible/dev_guide/testing.html
* Core supported modules vs purely community supported; do we need to do more?
* +1 (resmo)
* Is there a real difference between them ?
* mostly automerge enabled or not (bcoca)

* Have basic unit testing
  * +1 (resmo)
* Gundalow: From 2.4 all Core modules MUST have unit or integration tests. We are working through the backlog
* unit testing is not as important in modules, it just reflects consistency in the internal methods, the module is used as a full unit, not shared code. Integration/end to end testing is much more desirable and would actually reflect how people see/use modules.
*  module_utils on the other hand is the exact opposite, this is where i would require unit testing (bcoca)
* Agreed: For Networking Unit testing makes sense as most of the code is shared, and the modules themselfves are small
* For most modules integration tests are the best fit
* Unit tests are good for non-Modules
* Unit tests are good for functions in modules.  I also found them useful for building modules which were impractical to integration test properly.
* See mock based unit tests used in API Gateway module where typically you can only do one test every two minutes!! [mikedlr]
* Integration testing (if possible)
  * +1 (resmo)
  * +2 - it's a must, even if they can't be run during actual CI.  This documents how the module was expected to work.
  * +1 - Enabling Third Party CI might be a plus (spredzy)
* Support contract signed by partner
* Core engineers sign off for code quality

## Mini-Zuul Update

Seriously. No more than 10 minutes.

(We'll discuss in more depth 2:45-3:45 in Track 2)

### 3 Second Overview of Zuul

* New Ansible-based version of OpenStack's Gating Engine

  * Currently handles ~1800 repos / 2000 Jobs per Hour

* Multi-node, multi-repo, multi-cloud, multi-tenant
* Rich support for gating
* Jobs are all written in Ansible!
* Jobs are directly shareable (important for partner efforts)

### Zuul v3 is Alive

* OpenStack Infra running one
* BonnyCI
* BMW
* Software Factory patches written

PS: It's all Python 3!

### Multi-Repo Tests

* Functional tests for openstack modules are in shade:

  * https://github.com/openstack-infra/shade/tree/master/shade/tests/ansible
  * https://review.openstack.org/#/c/475986/
  * http://logs.openstack.org/86/475986/1/check/gate-shade-ansible/8e3cb9e/

* Functional tests require a working OpenStack
* OpenStack's Infra knows how to create one of those
* In Zuul v3:

  * PR against ansible/ansible:lib/modules/cloud/openstack
  * Triggers OpenStack Infra gate-shade-ansible job
  * Ansible PR can 'Depends-On' proposed patch in shade
  * Tests are run as-if proposed patch has landed

### Ansible Rollout

* GitHub Support has landed! (thanks jlk, BonnyCI and GoodData)
* GitHub App named "OpenStack Zuul"
* Add "OpenStack Zuul" to ansible/ansible:

  * Run Zuul's test suite on PRs to Ansible
  * Give ansible community exposure to zuul
  * Run shade's test suite on PRs to Ansible OpenStack Modules

* Spin up "Ansible Zuul" GitHub App
* Write/port jobs
* Joy!

