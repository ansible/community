# Utility modules.

## Introduction

The AWS utility modules provide functions which are designed to be
reused between different AWS modules but not other Ansible modules (in
which case the function could be shared in a different module)

## Criteria for utility functions and classes

* The functions will be copied with every AWS module which includes the utility module so must be kept lightweight.
* Changes made for one module may affect another module which the developer is not using and may not even have the ability to test
* Different modules may use the same utility function in different ways making the development of the functions more subtle and difficult. 

For this reason the utility modules are expected to have a smaller amount of higher quality code. 

Criteria for putting functions into the module_utils/aws directory 

* Used in at least two modules
* Reasonably clear, sensible agreed interface
* Don't know of a reason to think it will become obsolete soon
* 90% or more unit test coverage (line)

## Planned Layout

This is the planned layout.  

    aws/
        core.py - Basic AWS modules 
            class AnsibleAWSModule
                .connect
                .fail_json_aws
            class AWSRetry
            def camel_dict_to_snake_dict(camel_dict)
        direct_connect.py
        iam.py 
            def convert_friendly_names_to_arns
        rds.py
            def get_db_instance(conn, instancename):
            def get_db_snapshot(conn, snapshotid):
            class RDSDBInstance(object):
            class RDSSnapshot(object):
        resource.py - functions related to any AWS resources
            def wait_for_status(resource, status)
        vpc.py


## Using the module utilities

:*This section is temporary until the module utilities become standard.  It should be moved to the [AWS module guildelines in the amazon modules directory](https://github.com/ansible/ansible/blob/devel/lib/ansible/modules/cloud/amazon/GUIDELINES.md) once accepted*

Currently the module utilities directory is experimental.  The
functions should only be used in ansible modules which are merged with
Ansible can easily be updated or in private modules being developed
with support from the AWS working group.

All modules are expected to include the core module.

    from ansible.module_utils.aws.core import AnsibleAWSModule

    argument_spec = dict(
        name=dict(required=True),
        state=dict(default='present', choices=['present', 'absent']),
    )

    module = AnsibleAWSModule(argument_spec=argument_spec,
                              supports_check_mode=True,
                              mutually_exclusive=mutually_exclusive,
                              required_together=required_together,
                              required_if=required_if)

    check_mode = module.check_mode

    try:
        client = module.connect(resource='lambda') 
    except Exception as e:
        module.fail_json_aws(e, msg="Trying to connect to AWS")

    # do other things using the client we now have. 

Note that, as an "exception" to ansible normal practices, catching
`Exception` should be acceptable here because `fail_json_aws()` should
be able to deal with all boto derived exceptions.
