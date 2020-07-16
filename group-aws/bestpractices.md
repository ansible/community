# Best practices

New modules are already well sanity checked. As
existing modules are updated, we expect significant
changes to also include meeting of the sanity checks.

Changes for existing modules would be:
* Meet the Module Developer Checklist
* Meet the [AWS Guidelines](https://github.com/ansible/ansible/blob/devel/docs/docsite/rst/dev_guide/platforms/aws_guidelines.rst)
  particularly around exception handling
* Pass the ansible test suite
   - python coding standard
   - documentation expectations
* Make better use of built in functions for
  argument checking
* Make better use of the `module_utils` for common code such as `compare_aws_tags`,
  `boto3_tag_list_to_ansible_dict` etc.  Preferably use the [new utility modules](utility-modules.md)
* Have [integration tests](integration.md)
* Work with `--check` ([check mode](http://docs.ansible.com/ansible/latest/playbooks_checkmode.html#check-mode-dry-run)) and provide useful information under `--diff`


### Supporting documentation

Practical instructions/best-practice documentation to support developers wanting to add improvements such as the `--check` and `--diff` features.
