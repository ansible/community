# Creating an Ansible Working Group

## What are Working Groups


Working Groups are a way for Ansible community members to self-organize around particular topics of interest.

The basic components of a working group:
* A group name and charter (why the group exists);
* A registered IRC channel on freenode (will usually be #ansible-groupname);
* A group of users (at least two!) who will be driving the agenda of the working group;
* Dedicated wiki space.

The basic responsibilities of a working group:
* Be responsive on your IRC channel;
* Report semi-regularly on the cool stuff that your working group is working on;
* Keep your wiki space clean!

## Requesting a Working Group

Anyone can request to start a Working Group, for any reason. 

Cut and paste the following text into an [Community Issue](https://github.com/ansible/community/issues/new), and replace the examples in brackets
with your own working group info:

```
WORKING GROUP NAME:    [ Example: unicorn   ]

WORKING GROUP PURPOSE:
[ Example: This working group is to review  ]
[ all Unicorn-related modules               ]
[                                           ]
(keep it short and sweet)

AT LEAST TWO INITIAL WORKING GROUP MEMBERS:
[ IRC: gregdek / GitHub: @gregdek           ]
[ IRC: rbergeron / GitHub: @robynbergeron   ]
[                                           ]
(provide the IRC nicks AND GitHub IDs of your working group members, one name per line please)
```



## Process for Ansible Staff

We will ask you a few more questions if anything is unclear via the GitHub issue created above.

Once we have enough information, we will set up the following infrastructure:
* An IRC channel on freenode named "#ansible-yourgroupname", properly registered and op'd;
  * `*!*@ansible/owner/*    +AORefiorstv`
  * `*!*@ansible/staff/*    +Oo`
  * Group Contact set - via Jimi-C
* github.com/community
  * Create `group-` topic [directory](https://github.com/ansible/community/tree/master/) and `README.md`
  * [Index page](https://github.com/ansible/community/blob/master/README.md) list Group & IRC Channel
* A working group directory for your use;
* Membership in the ansible/community GitHub repo for working group members;
* A label in the issue tracker to identify issues/PRs for your working group;
* Dedicated wiki space.
* ansible/community: Agenda & label
* a/a label - update BotMeta
* Update [README.md](https://github.com/ansible/community/edit/master/README.md)
* [Ansibullbot](https://github.com/ansible/ansibullbot/blob/master/ansibullbot/triagers/plugins/community_workgroups.py) to know about new Working Group
* Publicise
  * Internal Email & Slack
  * IRC: `#ansible-devel`  `#ansible` 
  * https://github.com/ansible/community/issues/346
  * Google Groups: `ansible-project` & `ansible-devel`

## Help!

If you get stuck or want to know more join us in `#ansible-community` on Freenode
