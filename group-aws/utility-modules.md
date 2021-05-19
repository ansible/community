# Utility modules.


## Introduction

The AWS utility modules provide functions which are designed to be reused between different AWS
modules but not other Ansible modules (in which case the function could be shared in a different
module).

## Criteria for utility functions and classes

* The functions will be copied with every AWS module which includes the utility module so must be kept lightweight.
* Changes made for one module may affect another module which the developer is not using and may not even have the ability to test
* Different modules may use the same utility function in different ways making the development of the functions more subtle and difficult. 

For this reason the utility modules are expected to have a smaller amount of higher quality code. 

Criteria for putting functions into the module_utils/aws directory 

* Used in at least two modules
* Reasonably clear, sensible and agreed upon interface
* Don't know of a reason to think it will become obsolete soon
* 90% or more unit test coverage (line)

## Planned Layout

The layout is subject to change, probably until just before the 2.5 release (at which point there
should be a stable interface document).  Modules included in Ansible will get refactored together
with the change.  Pull requests will have to be refactored before being accepted.  Modules ourside
the main repository which are already using this interface will have to be refactored by their
authors.

    aws/
        core.py - Basic AWS modules 
            class AnsibleAWSModule - class to use for handling module set up'; based off AnsibleModule
	    	.params - returns the parameters of the module (this is @property method)
		.exit_json() - low level module exit function from AnsibleModule
		.fail_json() - low level module exit with failure function from AnsibleModule
		.fail_json_aws(exception, msg=<string>) - higher level function for exiting after exceptions
		.get_aws_connection_info() - return information about AWS connection;  you don't need to call this just to connect
                .get_aws_session() - returns a low level botocore session
                .get_aws_client() - returns a boto3 medium level client *** check this
                .get_aws_resource() - returns a high level boto3 resource
            class AWSRetry (not yet moved in)
            def camel_dict_to_snake_dict(camel_dict)
        direct_connect.py
        iam.py 
            def convert_friendly_names_to_arns
        rds.py (names still subject to change - please comment in [PR](https://github.com/ansible/ansible/pull/26594)) 
		get_rds_instance() -> rds_camel_dictionary
		rds_instance_to_facts(camel_dict) -> rds_facts_snake_dict()
		get_rds_snapshot() -> snapshot_camel_dictionary
		rds_snapshot_to_facts(camel_dict) -> rds_facts_snake_dict()
        resource.py - functions related to any AWS resources
            def wait_for_status(resource, status)
        vpc.py

Please note that various functions not listed above which are included in AnsibleModule may not be
replicated by AnsibleAWSModule.  This is deliberate to allow future simplification of the base
class of AnsibleAWSModule.  If you have a good reason for making other functions available please
discuss this with the AWS working group who should be happy to help or at least explain why the
function isn't available.

## Using the module utilities

*This section is temporary until the module utilities become standard and should be moved to the*
*[AWS module guidelines in the amazon modules directory](https://github.com/ansible/ansible/blob/devel/lib/ansible/modules/cloud/amazon/GUIDELINES.md)*
*once accepted*

Currently the module utilities directory is should be considered preview code.  New modules which
are to be included in Ansible should use the code.  Modules which are published outside the main
ansible repository should _not_ include this code before ansible 2.5

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

Note that, as an "exception" to ansible normal practices, catching `Exception` should be acceptable
here because `fail_json_aws()` should be able to deal with all boto derived exceptions.

In the case where fail_json_aws() gets a non AWS exception it will record a traceback attempt to
convert it to a string and incude that string in the final message.  In most cases this will give a
nice printout.  Beware, though, that there are no rules for python exceptions so if your exceptions
are abnormal (e.g. you need to call the .beam_me_up() message before you can get a string) you
should verify that it works correctly expecially if your exception includes a `response` member.
Please contact the AWS working group with any problematic examples you find.