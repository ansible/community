# Ansible Contributor Summit PR and Issue Backlog + Metrics
21-06-2017

IRC: #ansible-meeting

Subtopics from original planning etherpad (https://public.etherpad-mozilla.org/p/ansible-summit-june-2017):

## PR / Issue Backlog topics:

* Where are we
* What can be done to assist this
* Increasing maintainers
  * +1 - maybe give more people commit rights (hint hint)
  * +1
  * +1
  * This has been done and only shown very limited short term gains, very few people can deal with the commitment
    * Because there's no reward or we doing it wrong, it's not necessarily a given fact
    * How can we make it rewarding?
  * Automerge has been enabled for 'community' modules with some success, but it still requires people to commit to maintainership and not all modules/sections have enough people dedicated.
  * RH also has been expanding the group non-stop, communication with maintainers and keeping a cohesive set of standards is becoming harder
  * (It has been evoked earlier with SIG creation) Idea: Creating squads of maintainer (for example a FreeBSD squad that would be in charge to review FreeBSD related changes - could work with tags) and report to a committer that the commit is OK, then committer could either review then merge, or blindly merge if she trusts the squad members enough (spredzy)
    * We are doing this for Windows already, just add a group of people to MAINTAINERS.txt for a subset of packages
      * There is no means of creating such "squads", maybe we need to actively encourage this instead ?
      * And need a committer to commit to proxying for each squad
* PR & Issues numbers are discouraging involvement
  * maybe more accurate triage is needed
    * triage is not the problem, it's reviewing and merging that is lacking, even for the most simple PRs
  * maybe not well documented issue need to be closed quickly without response from the reporter
    * currently there is an 'expiration' on needs_info labeled issues(bcoca)
* Establish criteria for:
  * When code is considered oprhaned (no maintainer) (bcoca)
  * Remove orphan plugins/modules
  * Review and merging new modules (there's no maintainer yet, so what can we do here ? subsystem-maintainer shipits ?)
* Lots of PRs that are ready to be merged pile up and require escalation for them to get merged
  * automerge fails to work for the majority of PRs (as there are no 2 active maintainers), maybe change the rules ?
  * Maybe stop developing new stuff, and only fix open issues / review PRs for 2-3 months until the queue is to an "acceptable" level again
  * This is related to community-building: lingering unanswered issues/PRs does not a community build (Yoda-voice)
* How about ansibot commands for proposing yourself as a new maintainer ?
  * e.g. if none of the maintainers were active after X months (and did not respond to ansibot requests), mark the module as effectively unmaintained so users/contributors can take over
  * Ansibot could also be used as a communication-channel for reminding maintainers of their responsibilities (just as it does for reporters/contributors)
* Could ansibot remove old CI comments that are no longer relevant ?
    * They really make it harder to find relevant info in some cases.
    * And could scare away early contributors that need time to adjust (i.e. wall of shame ;-))
* Lot of feature/bugfix PR without any test: this is a problem
    * In most cases, should not bugfix PR contains a new test or an updated one ?
    * New modules without tests should not be accepted

## Metrics Topics

* What should we count, ideas please
  * Some time spans, like https://about.gitlab.com/features/cycle-analytics/
  * issue -> assignee/right flag/maintainer response
  * issue -> PR
  * PR -> merge
* # open issues/PRs per module -> evaluate maintainership (add more?)
* # open issues/PRs per category (e.g. Windows, cloud/vmware, network/nxos, ...)
* # of interactions per issue
* # time between interactions (sometimes maintainer lags, sometimes author)

## IN-ROOM DISCUSSION

### Stats are not detailed enough in the following areas:
* Which PRs specifically are not getting merged, or are getting merged less often?
* Define the workflow and states that a PR goes through and how many PRs are in that state.
* Break this down by area and track monthly trends
  * Time till first human comment
  * Time till first review or shipit
  * Time till 2nd review
  * Time till merge
* Number of PRs raised against modules without maintainers

* Are there sizes of PRs that are failing to be merged?
* Are we dealing with a lot of inactive maintainers?
* How many PRs come from knowledgeable vs. non-knowledgeable, and what are the different paces?
* Is the bot pinging properly?
* We used to have the bot ping for all stalled PRs, are we not doing that now?
* Stats for "maintainers needed"
* Refine a maintainer solicitation based on:
  * Time of open
  * Amount of open
  * Generate a list of modules that "need help" automatically
  * An automated mechanism eases the pressure on contributors who don't know how / are unwilling to ask for help
* Or just say "I need help with my module"
* All of this needs to be documented

