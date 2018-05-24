# Ansible Contributor Summit 21-06-2017 Contributor Involvement

IRC: #ansible-meeting

Subtopics from original planning etherpad (https://public.etherpad-mozilla.org/p/ansible-summit-june-2017):

## What do we have today for contributor involvement / onramps? (Greg to write this up)

* onramp resources

  * http://tannerjc.net/wiki/index.php?title=Ansible_Developer_Lightbulb

* Survey?
* What are the pain points for (new) contributors

  * What issues do you still face today
* How did you (contributor) get as involved as you are today

  * How can we get extra people to your level

* Mass survey of all contributors

  * How can we make your live better
  * Top three things to address
  * Should also detail what's been done to-date
* Community: How to strengthen & communicate

## Create a list of actions anyone can help with (e.g. add missing integration/unit tests, bug triage, etc...) and a contact-person for each
* Create a list of actions anyone can help with (e.g. add missing integration/unit tests, bug triage, etc...) and a contact-person for each
* Add a slide in every Ansible presentation how people can help (related to the slide's topic) with specific actions and the link to the above
* This could also be related to missing functionality in existing modules (e.g. coming from open issues)
* You could add difficulty and priority level for issue/ new ideas
* [Akasurde] Adding special tags like "easy_fix", "low_hanging_fruit", "good_to_have", "needs_contributor", "needs_tester"
* this will attract more first-time-contributor and will reduce burden of core team members
* 'waiting_on_contributor' exists already and does not seem to have many pickups
* waiting_on_contributor does not show that the fix is easy; some curated label for first-time contributors would help imo

  * "easyfix" is very much in the eye of the beholder, but perhaps better than no effort at all
* Ideas

  * Modules that need tests adding (priority order based on if they require external resources to test)
  * Module_utils that require unit tests
  * Link to PRs that need testing, perhaps ones with testing_pull_request
  * PRs that need revieing
  * Linking to prsbyfile allows people to find PRs that a contributor may be interested in
  * Mix of coding and non-coding tasks

## Module Maintainers

* Ansible will document the expectations here and send a PR out for review
* Therefore lets wait for the PR and discussion can take place there
* For reference the discussion was:

  * Documented process to become a maintainer (resmo)
  * Expectations for maintainers - Need to define and document
  * Unowned/orphaned modules throw a wrench into things?
  * List of unmaintained modules?

    * Possibly option to ansible-doc or hacking/meta-data to generate?
  * Clearly state what is expected from module owners/maintainers, so contributors can opt-in/opt-out to responsibilities
  * https://github.com/ansible/ansible/blob/devel/MODULE_GUIDELINES.md#maintainer-responsibilities (should probably be moved into documentation)

    * +1 (resmo)
    * +1 (willthames) - also, be clearer on when people with write access can accept changes. I see lots of people saying 'Approved' or 'shipit', when they have the rights to actually ship it
    * +1 bjolivot

  * maintainer and author
    * The module documentation does not highlight the author, nor the maintainer(s), and often one of the driving factors is attribution (and if your name is put on it, you want to show quality)
    * they do appear in ansible-doc but that does not seem to match acutal maintainer
    * add name of developer/maintainer in http://docs.ansible.com/ for each module
    * author info is kept in module but maintainer is external to modules and in different repo
    * Is the `authors:` list even useful?
    * Gundalow Maybe we need to tell developers they should add their name to the `authors:` list when they work on a module. Most don't
    * there used to be 'maintainers' field supported, but it was never used, resurrecting it would allow existing community maintainers to expand/pass the torch w/o core involvment (bcoca)

## IN-ROOM DISCUSSION:

* Nested groups and read-only collaborators in Github might be super useful to help with the "BSD" problem (spread out modules that aren't well namespaced but need a group of collaborators to help fix) (Matt is going to fix this for us!)

  * Robyn provides link to old words from a while ago: https://www.redhat.com/archives/fedora-advisory-board/2006-April/msg00220.html
* (how do we make sure this is the bat signal and not the "everybody gets pinged all the time" thing)   (https://github.com/blog/2378-nested-teams-add-depth-to-your-team-structure)
*  Do we want to turn on wikis?  SI SE PUEDE
* OK, here is the proposal (that has been "unanimously accepted")
  * Make it SUPER CLEAR that it's easy to get write access to ansible/community
  * Recreate the kubernetes/community structure for SIGs within ansible/community
  * Turn on wikis in that space

    * If we're doing wikis, make sure that the page is valuable, and there's some kind of "garbage collector"
  * Identify owners of the wikis so they don't end up filled with crap
    * Do we have to opt in? Like, let's say the AIX folks don't want to have a wiki and would prefer something ... else? elsewhere? in tha land of AIX? does that prevent other people from coming and making their own magical AIX space?
    * Greg says "lightweight stuff" and uh....
* Do a big survey of all contributors of all kinds with a comprehensive SurveyMonkey survey
* Onboarding help at the SIG level

  * Every SIG has a "how to join and do cool stuff"
  * Each SIG is responsible for bringing contributors up their own pyramid

ACTION ITEMS:

