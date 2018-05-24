# Planning for Ansible Contributor Summit, October 2016

* Date: October 10, 2016
* Location: Brooklyn, NY, @Brooklyn Marriott (and also online for remote participants)

## SCHEDULE, Eastern US time

* MORNING TRACK (and breakfast)

  * 09:30 - 10:15 Roadmap Updates: Ansible Core, Galaxy, Ansible Container, Core, Galaxy and Container details: https://public.etherpad-mozilla.org/p/ansible-summit-october-2016-core-update
  * 10:15 - 10:45 Testing Working Group Update - https://public.etherpad-mozilla.org/p/ansible-testing-working-group
  * 10:45 - 12:00 The Future of Module Curation - https://public.etherpad-mozilla.org/p/ansible-summit-october-2016-module-curation

* 12:00 - 13:00 LUNCH
* AFTERNOON TRACK #1

  * 13:00 - 16:00 Ansible CI (Zuul)

    * https://public.etherpad-mozilla.org/p/ansible-summit-october-2016-zuul

* AFTERNOON TRACK #2:

  * 13:30 - 16:00 Docs Sprint (we'll likely start around 13:30 instead of 13:00, but feel free to join us at 13:00)
  * https://public.etherpad-mozilla.org/p/ansible-summit-october-2016-doc-sprint
  * IRC Channel: #ansible-docsprint

## PLANNING DETAILS BELOW

Remember to put your names on the Etherpad! (right-hand side)

## Proposed Topics (please comment or +1 or add your own topics):

* The upcoming roadmap for "curated" vs. "community" modules. Which is which? How do they work? The proposal is here: https://github.com/ansible/proposals/blob/master/modules-management.md
* Update on the testing working group -- how's it going? (Weekly meeting standing agenda: https://github.com/ansible/community/issues/114 )
* The hopefully recent release of Ansible 2.2 (!) and the roadmap for Ansible 2.3!+1
* Update on ansible-container v0.2 -- what needs to be in it?

    * Docker for Mac / Docker for Windows support
    * Galaxy support!

* Galaxy roadmap

    * For open sourcing? Or in general? (both)
    * Galaxy / API + Fedora (robyn, sgallagher?)

* Metrics! Count all the community things. (robyn)+1
* Zuul + CI (mordred, jeblair, robyn, threebean, maxamillion, sgallagh?) <---- need a bunch of time in a room for this, probably adjacent to doc sprint

    * Zuul overview / understanding
    * Ansible CI
    * Zuul + Fedora CI?
    * Zuul and Fedora/RHEL Base Runtime CI
    * Other magic?
    * Factory 2.0 +1

* Proposals review

    * i.e. run through current proposals and suggest what they need next (accept/reject/more info) etc

        * see what people thing about https://github.com/ansible/proposals/issues/31 :-)

* Python 3 module 'porting'

    * It would be great to get some advice from the core team based on their experiences of porting modules so they will run on python 3(.5)

      * There is some here: https://github.com/ansible/ansible/blob/devel/docsite/rst/developing_modules_python3.rst but I have not put all the lessons I've learned there.

    * Ansible 2.2 is Python3 "Tech Preview"

        * 50% of core code is untested - so we don't know how stable that is
        * Test improvements welcome!
        * If you have any spare time, please ping abadger1999 on IRC

  * Ideas/Questions

    * How can we get community involvement

    * Post repo merge can we raise issues against every module that doesn't have tests. Use the py3 label

* Windows support

  * Find out what things are priorities for people

### Proposed Doc Sprint Topics (please comment or +1 or add your own topics):

We're also having our first-ever docs sprint at the Ansible Contributor Summit!

* Improve the modules documentation

  * how? what's needed most? +1+2
  * establish community guidelines for how module documentation is structured
  * how often should we build/push out docs (ad hoc process now) +1
  * Tighten and document how things should be formatted - style guide

    * Full sentences for `description`
    * Use of I(), C(), etc - Currently inconsistent
    * Bulk change to make everything consistent

* release notes for all the things

  * look into Reno for Release Notes - https://github.com/ansible/community/issues/61

* help migrate old .md docs into .rst (and update them if needed)
* How can we improve developing_modules.html

  * https://github.com/alikins/ansible-modules-extras/commit/c87795da5b0c95c67fea1608a5a2a4ec54cb3905


## Testing Working Group Update

* Please see https://public.etherpad-mozilla.org/p/ansible-testing-working-group
* Every Thursday. Started 18th August
