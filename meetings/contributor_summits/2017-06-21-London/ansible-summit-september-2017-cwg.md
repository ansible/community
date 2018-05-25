# AnsibleFest SF Contributor Summit, Community Working Group Session (9am-11am PDT)

IRC: #ansible-meeting

## Update on community process documentation+1

* GOAL: Get docs updated and centralized -- authoritative source of community docs and process
* http://docs.ansible.com/ansible/latest/community/
* Maaaaybe not as updated as necessary yet ;-)
* WG today will likely slog through the current content and confirm it all.

### Versioned documentation

* We have this for docs in general. Not sure whether we're ready for versioning the community process (first, fix what we have)
* Docs come in a 'devel' and 'current recommended version' for Ansible itself -- relying on search results to some extent to get people to the right thing
* Q.v. Django docs for searching and display of the desired version of docs
  * https://docs.djangoproject.com/en/1.11/intro/overview/
  * Be able to restrict search to version
  * Always visible on the page: a way to change to other versions of the docs
* Devel guide and community guide should default to "devel" (we will zero out the old pages and send links) (or maybe tag in GIANT LETTERS that say THIS COULD BE WRONG)
  * people developing for older versions (but not submitting to Ansible) might still want the old docs
  * (Some discussion about this; debating usefulness of old process guides. That's what we have git for.)
  * (It could be that there's no "devel" at all and the latest is at the top level of docs.ansible.com/community)

## Working Group reporting and coordination+1

* TIME ZONES / meeting rotation
* define success criteria (?)
  * backlog reduction
  * roadmap design
  * centralized communication
  * timely PR reviews
* Any advice from working groups for best practices/features that help Working Groups actually work well
  * Particularly github reporting automation :)
* JBoss: Part of the work for even a lightly active WG is to ensure community members know their plans and active initiatives, so they can avoid duplication of effort or starting off in the wrong direction
* How much to publicize WGs?
  * Will interested people find them on their own? -- don't assume this. But probably a part of News WG work to help spread the word
  * Also celebrate successes across the project: snowball effect
  * Progress toward having at least one committer in a WG -- helps advocate for their work

## Evaluation of Ansibot

* https://github.com/ansible/ansible/blob/devel/.github/BOTMETA.yml
* shipit: why 2? or n% of maintainers?
  * Seems to violate "least surprise" doctrine
  * shipit for new modules
  * debate on whether we should be automerging new modules now or waiting for modules to be split out
  * Argument for merging more:
    * We have people interested in wanting to put new modules in the repo but those PRs are languishing which is bad for community morale
  * Argument for merging less:
    * too many unmaintained drive-by modules
    * Isn't this an argument for reaping them more than an argument for preventing new modules from entering the repo?
* Should require a shipit from somebody OTHER than the author
  * Various consumers of Ansible will be very angry if code is allowed into Ansible without at least ONE non-author review
  * For niche modules, there may not be anyone who uses our github to give feedback on a PR.  That does not mean that we don't want to merge these changes
  * There still needs to be a human other than the author that's looking at the change to sign off on no obvious backdoors or other shenanigans.
  * This is a policy decision, not a "need".
  * Propose a timeout on PRs where it can be automerged if there have been no objections before that timeout
* Zuul?

## AFTERNOON NOTES

### Docs issues with the new community docs

* In this session, we are running down all of the docs issues with the new community docs, and will turn them into a ticket/tickets as appropriate.
* First, the top-level sidebar link from docs.ansible.com ("Community Information and Contributing") is out of date and points to the old docs page instead of the new docs directory.  Note: broken in *both versions*, both stable and devel! (Once you get into the docs site, the sidebar is correct.)
* Q#1: do we actually want the roadmap items to live in docs, as they do now apparently and are linked as such, or do we want to link directly to Github? (jason) (probably the right answer is point directly to Github)
* Add to community maintainers section: how does one become a community maintainer? What is the process?
* Is "ready_for_review" still a valid state? Should it be removed? (We should at least note that it's a legacy state)
* "new_module" is actually pretty good, maybe? We should describe the process here, even if it's just "to speed up potential inclusion, you can always come to the meeting to advocate".
* First four links go to the same page -- is that confusing? It's kind of confusing to me!
* Reporting a bug: add more info about necessity of including component name, since that's how the bot determines who owns the issue
* Reporting a bug: just re-read this generally, a lot of this text is from 3-4 years ago
* "Reporting A Bug" is in caps and should be lower case
* "how_can_I_help.html": "Become a module maintainer" should link to the "module maintainer guidelines"
  * Rework "working group guidelines" to better documentation (maybe "creating a working group" is not actually helpful and we should point to existing working groups as well)
  * Link to Ansible development process isn't marked up correctly in the RST (yup)

### Open Q: should we autoclose PRs that are in needs_revision for a long time? It doesn't hurt to close them, they can be reopened. (gdk will revisit with product management)

#### Module Maintainer Guidelines

* typo: "Thank you for being a maintainer of one Ansible’s community modules!"
* Broken link: "[ansible/ansible](https://github.com/ansible/ansible) repository"
* Broken link: "[contribution guidelines](https://github.com/ansible/ansible/blob/devel/CONTRIBUTING.md),"
* ...and others
* Extras maintainers list should now point to BOTMETA
* Either change or remove "A detailed explanation of the PR workflow can be seen here: https://github.com/ansible/community/blob/master/PR-FLOW.md" (or just point to Sam's page)
* Fix "Change Maintainership" link
  * And add an explicit "orphaning" process (use "ignored"?)
  * Be more explicit about which modules are unmaintained / orphaned
  * If we have an explicit "orphaning" process, that can *also* be an "unresponsive" process as well
  * What are reasonable expectations for orphaning?
* Change "tools and other resources" to point to the "other tools and programs" page
  * Other tools and programs doesn't contain ansibullbot info so that might need adding at the same time
  * Add: Ansible Doctor (https://github.com/ansible/ansible-doctor)
  * Ansible Inventory Grapher: https://github.com/ansible/ansible/pull/29065
  * Review from here: https://tannerjc.net/wiki/index.php?title=Ansible_Community_Projects

#### Other Docs

* Add the Code of Conduct link to the index (http://docs.ansible.com/ansible/devel/community/code_of_conduct.html)
* Is there anything in http://docs.ansible.com/ansible/devel/community.html that should be under http://docs.ansible.com/ansible/devel/community ? (should be sorted as part of the original port)

