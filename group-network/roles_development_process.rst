********************************
Network Roles Development Process
********************************

.. contents:: Topics

Overview
========

This document is intended to outline the *development process* for Ansible Network Roles.

If you are an end user and wish to use the roles, please see the module list on `Ansible Galaxy <https://galaxy.ansible.com/ansible-network/>`_.



Versioning
==========

Ansible Network Roles are designed and tested to follow the stable Ansible releases.

They are not to be used with the `devel` version of Ansible.

Example 1
---------

`network-engine` release 2.5.3

* Supports Ansible 2.5.*
* Is the 3rd update to this role since supporting Ansible 2.5

Process when Ansible branches stable-x.y
----------------------------------------

Aim: Ensure that all Network Application Roles are tested against `devel` and the next `stable-x.y` branch

* Add tests for py2 and py3 to https://github.com/ansible-network/ansible-zuul-jobs/blob/master/zuul.d/jobs.yaml
* Update https://github.com/ansible-network/network-engine/blob/devel/.zuul.yaml so the new version of Ansible is tested on the `devel` branch of the role

* Add new `ansible-role-tests-2.6-py2` test to https://github.com/ansible-network/ansible-zuul-jobs/blob/master/zuul.d/jobs.yaml
* https://github.com/ansible-network/network-engine/blob/devel/.zuul.yaml
* https://github.com/ansible-network/ansible-zuul-jobs/blob/master/zuul.d/jobs.yaml - Update `override-checkout:` to current latest stable
* Do a `recheck` on all open PRs on all repos under `gh/ansible-network`


Release Procedure
=================

To version the roles in Galaxy we use Git Tags

* Ensure your local branch has no local changes and uptodate with upstream
* Ensure ``changelog/fragments/*.yml`` are up to date and contain details for new features
* ``git tag -a v2.5.x`` tag (notice leading v)

  * Reno uses git tags to work out the version, so we need to locally update the tag to allow the correct titles to be generated, we do **not** want to push this

* ``pip install reno`` (if not already installed)
* ``reno -d changelogs/ report --title 'Ansible Network network-engine' --no-show-source --output CHANGELOG.rst`` (replace ``network-engine`` as needed)
* ``git diff CHANGELOG.rst`` # If changed then we want to commit them

  * Check content + version headers
  * If the anchors are not generated update the version of reno you are using
 
* git checkout -b changelogupdates-foo-bar
* ``git commit CHANGELOG.rst``
* ``git push origin changelogupdates-foo-bar``
* Review PR, use GitHub's UI to ensure RST is rendered correctly
* Merge PR
* Tag

  * Ensure on devel and synced
  * ``git tag -a v2.5.x``
  * ``git push --tags ansible``

* `Galaxy upload <vhttps://galaxy.ansible.com/my-imports?namespace=ansible-network&selected=265187&page_size=10>`_

  * Review errors

* Check latest version is shown on `Galaxy list <https://galaxy.ansible.com/ansible-network>`_

  * Ensure "Version History" is updated
  * Ensure "README" has been updated"




Process for Ansible major version update
----------------------------------------

When the next major version of Ansible is released the following process needs to happen

Using the release of Ansible 2.6.0 as an example:

* Ensure the current `network-engine` integration tests pass when run against Ansible 2.6.0 - If not fix in `devel` (remembering to update changelog if there are bug fixes (rather than test fixes))
* Branch `stable-2.5` from `devel` - We don't expect this branch to change unless critial bugs are found.
* Ensure branch is protected in GitHub (this allows Zuul to run)
* If required, restrict who can commit
* network-engine's `devel` branch is now for the current stable Ansible release. 
* Create ``changelog/fragments/v260-initial.yml`` with `major_changes` entry
* ``git add changelog/fragments/v260-initial.yml && git commit changelog/fragments/v260-initial.yml``
* ``meta/main.yml`` update to be ``min_ansible_version: 2.6``
* Ensure local changes are committed
* ``git tag -a v2.6.0``
* Follow Role release procedure


New role
========

To ensure consistency when creating a new role the following needs to be done:

* GH Repo

  * `Description` Should link to Galaxy
  * `devel` should be the main branch
  * Branch Protections ``https://github.com/ansible-network/{REPO}/settings/branches`` - Required for Zuul and general good practice (no force pushes or accidental deletion of branches)
  
    * Add New Rule

      * Applies to: ``*``
      * Include administrators: Checked

    (If you get a 404 on ``{REPO}/settings/branches``, request GitHub Admin permissions for that repo)

  * Allow `Allow merge commits` on ``https://github.com/ansible-network/{REPO}/settings/`` - Needed for Zuul Gate.
  * Create new label ``https://github.com/ansible-network/{REPO}/labels``
  
    * Name: `mergeit`
    * Description: `Zuul to merge when Green and +1`
    * Color: `#0e8a16`
    
  * Copy ``changelogs/config.yaml`` from network-engine
  * Create ``changelogs/fragments/v0-initial-release.yaml``, see network-engine for example
  * Copy layout of ``README.md`` from `network-engine's README.md <https://github.com/ansible-network/network-engine/blob/devel/README.md>`_ (Links to Galaxy, how to install, etc)
* ``meta/main.yml`` update to be ``min_ansible_version: 2.6`` (Current major stable release of Ansible)



Adding & Enabling Zuul
-----------------------

* Ensure GitHub setup has been completed as detailed in "New role" above, without this Zuul will not process PRs
* PR1:

  * Clone SF config repo: ``git clone https://softwarefactory-project.io/r/config``
  * Add repo to  `resources/tenant-ansible.yaml <https://softwarefactory-project.io/r/#/c/13403/>`_
  * Git work flow: `Software Factory Git Process <https://review.rdoproject.org/docs/user/short_git.html>`_
  * `Install git-review & setup SSH Key <https://softwarefactory-project.io/docs/user/contribute.html#create-a-new-code-review>`_
  * Once PR is raised ask in `#softwarefactory` for review & merge

* PR2: ``.zuul.d`` add `ansible-test-sanity` + fix any failing tests - Backport to stable branch(es)
* PR3: Integration tests `ansible-role-tests*` + How that works  - Backport to stable branch(es)

Troubleshooting: Check branch permissions, ask in `#softwarefactory`
