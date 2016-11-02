# Merge Workflow
Normal git/github workflow for the Ansible project for those with committer permissions.
Before reading this document you should already be familiar with the general release process.

## Merge into devel
Once happy with the PR

 * Use rebase unless multiple commits (git pull --rebase && git push --ff-only)
 * Use squash option when multiple commits  (git rebase)
 * Merge is last resort, it is normally better to cherry pick locally
 * Update CHANGELOG.md if new plugin/feature has been added, removed or deprecated

This is done to make history flat for readability and bisect easier.

## Backporting into stable-x.y

* No merging features into stable-x.y; only bugfixes should be added
* cherry-pick -x to keep attribution
* Additional criteria during alpha/beta/RC
	* When in doubt, discuss with the team in #ansible-devel
	* If we are planning another RC:
	* Avoid large refactoring
	* merge small fixes you are reasonably confident make the code less buggy
	* Prioritize fixes for bugs and regressions introduced by the release

	* If this is the last RC before actual release
		* Only release required or trivial fixes (changelog, docs, packaging, etc)
		* Raise any BLOCKERS for release. If the team decides to merge the fix for that into stable-x.y it triggers a new RC

	* Any fixes not merged above, merge into the temp-staging-x.y branch so it will be added to stable-x.y AFTER final release (for possible x.y.z+1 future release)
