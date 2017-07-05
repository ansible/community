# Integration Testing

There are very few integration tests for EC2. Those that
exist are in test/integration/targets

## Expected test criteria

* Resource creation
* Resource creation again
* Resource creation under check mode
* Resource modification
* Resource deletion

When adding new features, those features should have tests.

# Github PRs
There are some PRs with tests:

| Module               | PR                                                     |
|----------------------|--------------------------------------------------------|
| lambda               | [24951](https://github.com/ansible/ansible/pull/24951) |
| rds                  | [25646](https://github.com/ansible/ansible/pull/25646) |
| rds_param_group      | [25345](https://github.com/ansible/ansible/pull/25345) |

# State of the codebase

Existing modules with tests:
* `aws_api_gateway`
* `aws_s3`
* `ec2_ami`
* `ec2_elb_lb`
* `ec2_group`
* `ec2_key`

