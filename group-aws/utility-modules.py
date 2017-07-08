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
        direct_connect 
        iam.py 
            def convert_friendly_names_to_arns
        rds.py
            def get_db_instance(conn, instancename):
            def get_db_snapshot(conn, snapshotid):
            class RDSDBInstance(object):
            class RDSSnapshot(object):
        resource.py
            def wait_for_status(resource, status)
        vpc.py


