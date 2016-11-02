#Triage Process
General outline of the Ansible triage process to deal with new tickets.

## Ansibull Bot
Detailing just triage here, it does more things in full life cycle.
 * label/categorize, adds ‘needs_triage’(pending implementation) for new ‘ansible issues’ (open, no label)
 * CC maintainer

## Contributer ticket triage
New tickets that have not had human view them (labeled as 'needs_triage' once implemented)

 * In order of priority (going away after repo merge)
	* ansible/ansible
	* ansible-modules-core
	* ansible-modules-extras ( if time permits )

 * Actions:
	* Check bot labeled tickets correctly
	* ASK IF UNSURE, If it takes more than a few minutes, PUNT
	* Correct title, make more concise, if needed (BAD title: “Fixes 12345”)
	* Request information, if obviously missing
	* Attempt to reproduce/verify/fix ONLY if simple (low hanging fruit)
	* Optionally ping subject matter expert so that they see it
	* Escalate when needed P1-P2 (security issues, widespread breakage, etc). Assign to subject matter expert.
	* Close Ansible versions < (n-2), warn on ansible versions (n-2) - (n-1)
	* FUTURE: populate/point at knowledge base, once we have one
	* remove 'needs_triage' label when done. (this is pending bot adding the label)

## Responding to mailing list
 * Approve/whitelist messages (requires list management permissions)
	* https://groups.google.com/forum/#!pendingmsg/ansible-project
	* https://groups.google.com/forum/#!pendingmsg/ansible-devel 
 * At end of day look for unanswered topics, try to answer or redirect to SME

## Responding to IRC
 * Check for users that are not getting answered or not getting correct answers #ansible and #ansible-devel on freenode
 * Optional: #ansible-meeting, #ansible-container and #ansible-es (Spanish)

## 'shipit'
Examine PRs labeled 'shipit' (until autobotmerge?)
 * Prioritize bug fixes
 * Quick review, might not be ‘shippable’
