# Ansible Summit October 2016 Docs Sprint

 Copied over from https://public.etherpad-mozilla.org/p/ansible-summit-october-2016

IRC Channel: #ansible-docsprint

Leaders from Ansible:

* Sandra Wills (aka, Sam or docschick)
* Scott Butler (aka, dharmabumstead -- joining remotely)

## Starting off with
    Introductions
    Polling about what we want to docsprint around the most
    Deeper dives into the docs ...

## Proposed Doc Sprint Topics (please comment or +1 or add your own topics)

### Improve the modules documentation

* how? what's needed most? +1
* establish community guidelines for how module documentation is structured
* how often should we build/push out docs (ad hoc process now)
* Tighten and document how things should be formatted - style guide

  * Full sentences for `description`
  * Use of I(), C(), etc - Currently inconsistent
  * Bulk change to make everything consistent
  * key=value or key:value -- are we standardized on this and how prominent is it in the docs?
  * tooling to help people validate it would be good (tom of google)
  * getting best practices in sync with docs
  * syntax coloring for examples? -- throughout docs, not just style guide -- syntax highlighting (native yaml), as a way of validating code/examples

* How can we improve developing_modules.html

  * https://github.com/alikins/ansible-modules-extras/commit/c87795da5b0c95c67fea1608a5a2a4ec54cb3905

    * This PR seems to be duplicating information, rather than adding extra details
    * I believe splitting the developing_modules.html up will make this more readable

Full IRC logs from the meeting https://meetbot.fedoraproject.org/ansible-docsprint/2016-10-10/docs_sprint.2016-10-10-15.57.log.html
ansible-examples doesn't have an owner... mperz is volunteering, tima is co-volunteering


## Agreed

*  When refactoring mode development items out of rst into rst/dev_guide
*  Generate a list of the specific issue with having docs in the core repo
*  Generate a style guide, initially for modules
* mperz and tima to own ansible-examples ( https://github.com/ansible/ansible-examples )
* Split out developing_modules.html

## What are pain points?
    mperz: new modules from devel branch being in main docs that aren't out yet .. and don't understand how or why to use them, or why they don't work
    versioning the docs ??+1+1
live docs should cover what it is use, not w
 /join #ansible-dochat's in devel
minimum "stable" and "devel" version
developer guides need more content and support (which scott is working hard to improve with a separate developer guide, among other improvements)

     gabe: search isn't tuned into the latest docs
     search via google seems better
     Toshio: Search is easier to use than browse.  Would love better organization to make browse better

     tima: pet peeve: specific to modules doc, layout of the options, getting hard to read
       example module docs where options layout breakdown:
           http://docs.ansible.com/ansible/ec2_module.html
           http://docs.ansible.com/ansible/synchronize_module.html
        its hard to identify which params are required. bold required parameters? separate required and optional options section?
        If a module has "extends_documentation_fragment" (e.g. comment docs across all azure module) split those out to make it more readable
        finding things in core that aren't documented enough or at all, maybe that folks don't know it's there (more devel side than user space)


    cruze: tables, formatting differences, or the translation of yaml to html, embedded in the rst

    misc: start with a long list of argument, while people might prefer example to see what the module can do, and later dive in the details

    gundalow: Split developing_modules.html into multiple pages (see developing_modules.html section)

    Someone commented that a QA doc would be interested -- that tells contributors and bleeding edge users how to test release cnadidates.
Core release notifications needs to link to this new page

   mperz and tima asked about  API docs.
      * Using the API to replace the CLI isn't supported yet (API is unstable) so this will be a while
      * Most users seem to be asking for module_utils docs.  That is stable and we need to document that +1+1
      * dharmabumstead to work on pushing an rst skeleton into the dev guide that will use sphinx autodoc to pull the information out of module_utils
      * tima and mperz can ping abadger1999 (toshio) to add docstrings for the most needed functions.


## Windows docs

lots of parts seem missing... matt davis needs to be pulled into this
(it is in progress, but we need to get in it sooner than later) -- rough docs are better than no docs

## moving the non-module docs out of the main repo and into a separate repo
the good/bad/ugly?

- it would mean we can't verify that a feature is documented along the PR
- and we can't snapshot/tag both of them
- new env variables, new features of playbook lang, etc. -- all go with the version of ansible
 (version control docs along side of the release as a option?)
     - gundalow saying that one danger is that versions are no longer automatically synced.
     - 2:05 PM misc says it means that we can't verify that the docs are updated when the code is updated.
     misc> Michael Scherer we have separate repo for glsuter, and so we can't refuse PR because they do add a feature that is not documented (or rather, that's not as seamless as it would with a merged repo)
2:07 PM
<bcoca> Brian Coca one thing i wanted to add is autogenerate code for all plugins like we do in modules, so lookup, callback, filter, etc
2:07 PM
<abadger1999> Toshio Kuratomi dharmabumstead brings up that currently the jenkins doc build tests the code and therefore docs build can fail due to code changes.
2:07 PM
<bcoca> Brian Coca as for rest of docs, we dont guarantee that they are in sync, but much easier to keep in sync vs having 2 PRs to 2 diff repos (core/extras anyone?)

## developing_modules.html

To avoid duplication the suggestions have been moved back to https://public.etherpad-mozilla.org/p/ansible-testing-working-group

