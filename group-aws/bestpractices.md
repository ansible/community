# Best practices

New modules are already well sanity checked. As
existing modules are updated, we expect significant
changes to also include meeting of the sanity checks.

Changes for existing modules would be:
* Meet the Module Developer Checklist
* Meet the [AWS Guidelines](https://github.com/ansible/ansible/blob/devel/lib/ansible/modules/cloud/amazon/GUIDELINES.md)
  particularly around exception handling
* Pass the ansible test suite
   - python coding standard
   - documentation expectations
* Make better use of built in functions for
  argument checking
* Make better use of the `module_utils` for common
  code such as `compare_aws_tags`,
  `boto3_tag_list_to_ansible_dict` etc.
* Have [integration tests](integration.md)
