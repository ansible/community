# Integration Testing

There are very few integration tests for EC2. Those that
exist are in test/integration/targets

## Policy

Following the 2.4 release, all modules marked `stableinterface`
MUST have integration tests for new features. Upgrading to boto3
shall be considered a feature request.

Modules marked `preview` SHOULD have integration tests for new
features.

Bug fixes for modules that currently have integration tests SHOULD
have tests added. Depending upon the urgency of the bug fix, we may
accept bug fixes without tests.

## Expected test criteria

* Resource creation
* Resource creation again
* Resource creation under check mode
* Resource modification
* Resource deletion

# Github PRs
There are some PRs with tests:

| Module               | PR                                                     |
|----------------------|--------------------------------------------------------|
| rds                  | [25646](https://github.com/ansible/ansible/pull/25646) |
| rds_param_group      | [25345](https://github.com/ansible/ansible/pull/25345) |

# State of the codebase

Existing modules with tests:
* `aws_api_gateway`
* `aws_lambda`
* `aws_s3`
* `ec2_ami`
* `ec2_classic_lb`
* `ec2_group`
* `ec2_key`
* `ecs_ecr`
* `elb_classic_lb`
