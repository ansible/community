# Creating an Ansible Working Group

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

Anyone can request to start a Working Group, for any reason. 

Cut and paste the following text into an issue, and replace the examples in brackets
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

We will ask you a few more questions if anything is unclear.

Once we have enough information, we will set up the following infrastructure:
* An IRC channel on freenode named "#ansible-yourgroupname", properly registered and op'd;
  * `*!*@ansible/owner/*    +AORefiorstv`
  * `!*@ansible/staff/*    +Oo`
* A working group directory for your use;
* Membership in the ansible/community GitHub repo for working group members;
* A label in the issue tracker to identify issues/PRs for your working group;
* Dedicated wiki space.
