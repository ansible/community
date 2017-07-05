# Refactoring Ansible module

## RDS

The RDS module suffers from two main problems:

* it is non idempotent, so you have to pass `command=create`,
  `command=modify` etc rather than `state=present`.
* there are lots of missing features now, as it is a boto module,
  and needs migrating to boto3 before the features can be implemented.

In [#25646](https://github.com/ansible/ansible/pull/25646),
the RDS module will be split into four:

* `rds_instance`
* `rds_snapshot`
* `rds_instance_facts`
* `rds_snapshot_facts`


## IAM

The current IAM module is a monolith. The intention is to replace it
with

* [ ] `iam_user` - in progress [#26290](https://github.com/ansible/ansible/pull/26290)
* [ ] `iam_role`
* [X] `iam_group`
* [X] `iam_policy`


## EC2

Although the `ec2` module is a bit of a monolith, that monolith does
mean that it's very simple to use - before splitting it up we'd need
to see what the results would look like.

That said, there are the following obvious renames that would make
sense, perhaps at the same time as moving to boto3 (having parallel
modules allows us to break backward compatibility which can really
help with boto3 moves)

* `ec2` → `ec2_instance`
* `ec2_facts` → `ec2_metadata_facts`
* `ec2_remote_facts` → `ec2_instance_facts`

## ELB

Since AWS have introduced Application Load Balancers, there is a need
to distinguish modules that support ALBs and modules that support classic
ELBs

[#25745](https://github.com/ansible/ansible/pull/25745) is a PR to rename
the old ELB modules.
