# Refactoring Ansible module

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
