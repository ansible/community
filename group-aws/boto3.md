# boto3

So many features are available only for boto3 that we need
to ensure our modules can use it.

The current approach is typically that a contributor notices
a feature that they require, they realise it's only in boto3,
and they port the module to boto3.

The above is mostly fine, but a better approach for modules
likely to be ported (unpopular modules, which we have no real
way of determining, are likely best just left alone) is as
follows:

* Create an [integration test suite](integration.md)
* Port the existing functionality to boto3
* Let contributors add new features

Once a module has a test suite, it'll be a lot easier to
enforce that new features must have tests.

# Github PRs that move to boto3

| Module               | PR                                                     |
|----------------------|--------------------------------------------------------|
| ec2_group            | [25340](https://github.com/ansible/ansible/pull/25340) |
| ec2_metric_alarm     | [23407](https://github.com/ansible/ansible/pull/23407) |
| ec2_vpc_net_facts    | [25375](https://github.com/ansible/ansible/pull/25375) |
| ec2_vpc_subnet_facts | [25374](https://github.com/ansible/ansible/pull/25374) |
| rds                  | [25646](https://github.com/ansible/ansible/pull/25646) |
| rds_param_group      | [25345](https://github.com/ansible/ansible/pull/25345) |

TODO: add many more to the above list!

# State of the codebase

## boto3

* `cloudformation_facts`
* `cloudformation`
* `cloudfront_facts`
* `cloudtrail`
* `ec2_ami_copy`
* `ec2_asg`
* `ec2_customer_gateway`
* `ec2_eni_facts`
* `ec2_lc_facts`
* `ec2_snapshot_facts`
* `ec2_vpc_igw_facts`
* `ec2_vpc_nacl`
* `ec2_vpc_peer`
* `ec2_vpc_vgw_facts`
* `ec2_vpc_vgw`
* `ecs_cluster`
* `ecs_ecr`
* `ecs_service_facts`
* `ecs_service`
* `ecs_taskdefinition`
* `ecs_task`
* `efs_facts`
* `efs`
* `elasticache_parameter_group`
* `elasticache_snapshot`
* `elb_application_lb`
* `elb_target_group_facts`
* `elb_target_group`
* `execute_lambda`
* `iam_managed_policy`
* `iam_mfa_device_facts`
* `iam_server_certificate_facts`
* `kinesis_stream`
* `lambda_alias`
* `lambda_event`
* `lambda_facts`
* `lambda`
* `lightsail`
* `route53_facts`
* `s3_website`
* `sts_session_token`

## boto3 *and* boto

* `eni_facts`

## boto

* `aws_api_gateway`
* `dynamodb_table`
* `ec2_ami_copy`
* `ec2_ami_find`
* `ec2_ami`
* `ec2_eip`
* `ec2_elb_facts`
* `ec2_elb_lb`
* `ec2_elb`
* `ec2_eni_facts`
* `ec2_eni`
* `ec2_group`
* `ec2_key`
* `ec2_lc`
* `ec2_metric_alarm`
* `ec2`
* `ec2_remote_facts`
* `ec2_scaling_policy`
* `ec2_snapshot`
* `ec2_tag`
* `ec2_vol_facts`
* `ec2_vol`
* `ec2_vpc_dhcp_options`
* `ec2_vpc_igw`
* `ec2_vpc_net_facts`
* `ec2_vpc_net`
* `_ec2_vpc`
* `ec2_vpc_route_table_facts`
* `ec2_vpc_route_table`
* `ec2_vpc_subnet_facts`
* `ec2_vpc_subnet`
* `ec2_win_password`
* `ecs_cluster`
* `ecs_service_facts`
* `ecs_service`
* `ecs_taskdefinition`
* `ecs_task`
* `elasticache`
* `elasticache_subnet_group`
* `iam_cert`
* `iam_policy`
* `iam`
* `rds_param_group`
* `rds`
* `rds_subnet_group`
* `redshift`
* `redshift_subnet_group`
* `route53_facts`
* `route53_health_check`
* `route53`
* `route53_zone`
* `s3_bucket`
* `s3_lifecycle`
* `s3_logging`
* `s3`
* `sns`
* `sns_topic`
* `sqs_queue`
* `sts_assume_role`

## Commands for the above list

### boto3

```
grep -l 'import boto3' *.py | sed 's/\(.*\)\.py$/* `\1`/'
```

### boto3 and boto2

```
grep -l 'import boto3' *.py | xargs grep 'import boto\.'
```

Note the above finds `ec2_ami_copy` too but that's an unused import

### boto
```
grep -l 'boto\.' *.py | xargs grep -lv 'import boto3' | sed 's/\(.*\)\.py$/* `\1`/'
```
