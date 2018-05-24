# Ansible Contributor Summit Windows

IRC: #ansible-windows

Subtopics from original planning etherpad (https://public.etherpad-mozilla.org/p/ansible-summit-june-2017):

* Collaborate/track progress using Wiki ? (instead of abusing issue tracker or the Etherpad chaos)
  * +1 (jhawkesworth) - lets decide some top level pages - I can see this being useful to ansible contributors and ansible users
* Open items
  * https://public.etherpad-mozilla.org/p/Ansible_Windows_Community_Plan
    * perhaps too much to talk through in the plan (above) and some overlap with suggestions here.  I think priority things should be those that most enable contributors and aid end users, specifically - for contributors .
    * good powershell resources
    * coding standard (below)
    * example module selected
    * .. for users
    * community wiki (above)
  * https://github.com/ansible/community/issues/153#issuecomment-286751848
* Decide on a Powershell coding standard -> https://github.com/ansible/community/issues/153#issuecomment-291019646 (https://github.com/ansible/proposals/issues/63) + 1
  * +1 (jhawkesworth)
* I think Ansible Team need to support WSL (integrated ubuntu in Windows10), linux console should not be a prerequisite if you want more Windows users.
  * for now this won't be a priority.
  * hard to commit to support  running on a product not itself supported
  * agreed.  In my experience it works fine for playbook development but use real linux for production (jhawkesworth)
  * Yeah, I wouldn't expect to see any significant movement here within the next few releases beyond what we're already stating . If Microsoft changes their support policy for WSL (and makes it usable from CI), we *might* consider "fully" supporting it at some point. A supported native Win32 Ansible is still a long way off, if ever, though it's something we do talk with customers about, and appetite for it is growing slowly.
* Official DSC support plan (Trond will be in the room, so we can discuss win_dsc "in the box" and other thoughts)
  * +1 (Trond :-) )
  * +1 (jhawkesworth)
* How about using SSH/Powershell on Unix/Linux, with DSC ?
* How are we wanting to support newer version of Powershell (5.0 and above). Do we maintain compatibility with older versions/when do we drop support for them?
  * +1 (jhawkesworth).  Forces on this - MS own support. Existing statements.  Support provided in other tools.
* live windows module code reviews ( would need making known in advance if this happens so that people can rebase PRs and fix up any older PRs).
* Revise 'committers' list, remove inactive, propose people from community to add
* Do we want to have an Ansible-powered alternative to Group Policies, or a way to drive GPO ?
  * How about a solution for standalone systems (that have no AD or Group Policies), Ansible seems well-suited for this
* A lot of configuration is done through the registry, but custom modules for registry entries is NOT the future
  * See discussion: https://github.com/ansible/ansible/pull/20992#issuecomment-277385149
  * A custom module or role for doing a set of known/working registry changes would be very useful
    * This could be organized according to target audience (e.g. standalone desktop, enterprise, ...)
* Now that we have integration tests for almost all Windows modules, can we adopt a integration-test-mandatory-rule for merging new modules/parameters ?


## IN-ROOM DISCUSSION

## ACTION ITEMS
Changed win-sig meeting time to 20:00 UTC every week, first meeting on June 27th

