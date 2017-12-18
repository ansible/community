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
| ec2_metric_alarm     | [23407](https://github.com/ansible/ansible/pull/23407) |
| ec2_scaling_policy   | [26476](https://github.com/ansible/ansible/pull/26476) |
| ec2_vpc_net_facts    | [25375](https://github.com/ansible/ansible/pull/25375) |
| elb_classic_lb_facts | [27435](https://github.com/ansible/ansible/pull/27435) |
| rds                  | [25646](https://github.com/ansible/ansible/pull/25646) |

TODO: add many more to the above list!

# State of the codebase (As at 2017-12-06)

## boto3 only

* `_ec2_vpc_dhcp_options_facts`
* `_iam_cert_facts`
* `_s3`
* `aws_acm_facts`
* `aws_api_gateway`
* `aws_direct_connect_connection`
* `aws_direct_connect_link_aggregation_group`
* `aws_kms`
* `aws_kms_facts`
* `aws_s3`
* `aws_s3_bucket_facts`
* `aws_ssm_parameter_store`
* `aws_waf_facts`
* `cloudformation`
* `cloudformation_facts`
* `cloudfront_facts`
* `cloudtrail`
* `cloudwatchevent_rule`
* `data_pipeline`
* `dynamodb_ttl`
* `ec2_ami`
* `ec2_ami_facts`
* `ec2_asg`
* `ec2_asg_facts`
* `ec2_customer_gateway`
* `ec2_group`
* `ec2_group_facts`
* `ec2_instance_facts`
* `ec2_lc`
* `ec2_lc_facts`
* `ec2_lc_find`
* `ec2_snapshot_copy`
* `ec2_snapshot_facts`
* `ec2_vpc_dhcp_option_facts`
* `ec2_vpc_endpoint`
* `ec2_vpc_endpoint_facts`
* `ec2_vpc_igw_facts`
* `ec2_vpc_nacl`
* `ec2_vpc_nacl_facts`
* `ec2_vpc_nat_gateway`
* `ec2_vpc_nat_gateway_facts`
* `ec2_vpc_net_facts`
* `ec2_vpc_peer`
* `ec2_vpc_peering_facts`
* `ec2_vpc_subnet`
* `ec2_vpc_subnet_facts`
* `ec2_vpc_vgw`
* `ec2_vpc_vgw_facts`
* `ec2_vpc_vpn`
* `ecs_attribute`
* `ecs_ecr`
* `ecs_taskdefinition_facts`
* `efs_facts`
* `elasticache`
* `elasticache_facts`
* `elasticache_parameter_group`
* `elasticache_snapshot`
* `elb_application_lb`
* `elb_application_lb_facts`
* `elb_target_group`
* `elb_target_group_facts`
* `execute_lambda`
* `iam_group`
* `iam_managed_policy`
* `iam_mfa_device_facts`
* `iam_role`
* `iam_server_certificate_facts`
* `kinesis_stream`
* `lambda`
* `lambda_alias`
* `lambda_event`
* `lambda_facts`
* `lambda_policy`
* `lightsail`
* `rds_param_group`
* `redshift_facts`
* `s3_sync`
* `s3_website`
* `sts_session_token`

## boto3 *and* boto

* `dynamodb_table`
* `ec2_ami_copy`
* `ec2_eni_facts`
* `ecs_cluster`
* `ecs_service`
* `ecs_service_facts`
* `ecs_task`
* `ecs_taskdefinition`
* `efs`
* `route53_facts`

## boto only

* `_ec2_ami_find`
* `_ec2_remote_facts`
* `_ec2_vpc`
* `_ec2_vpc_dhcp_options`
* `ec2`
* `ec2_eip`
* `ec2_elb`
* `ec2_elb_facts`
* `ec2_elb_lb`
* `ec2_eni`
* `ec2_key`
* `ec2_metric_alarm`
* `ec2_scaling_policy`
* `ec2_snapshot`
* `ec2_tag`
* `ec2_vol`
* `ec2_vol_facts`
* `ec2_vpc_dhcp_option`
* `ec2_vpc_igw`
* `ec2_vpc_net`
* `ec2_vpc_route_table`
* `ec2_vpc_route_table_facts`
* `ec2_win_password`
* `elasticache_subnet_group`
* `elb_classic_lb`
* `elb_classic_lb_facts`
* `elb_instance`
* `iam`
* `iam_cert`
* `iam_policy`
* `rds`
* `rds_subnet_group`
* `redshift`
* `redshift_subnet_group`
* `route53`
* `route53_health_check`
* `route53_zone`
* `s3_bucket`
* `s3_lifecycle`
* `s3_logging`
* `sns`
* `sns_topic`
* `sqs_queue`
* `sts_assume_role`

### Neither boto nor boto3

* `__init__`
* `_ec2_ami_search`
* `_ec2_facts`
* `ec2_metadata_facts`

## Commands for the above list

### boto3 only

```
for f in `grep -lE 'import boto3|import botocore|from botocore' *.py`; do
  grep -Eq 'import boto[^3c_]|import boto$|from boto[ .]' $f || echo $f
done | sed 's/\(.*\)\.py$/* `\1`/'
```

### boto3 and boto2

```
grep -lE 'import boto[^3c_]|import boto$|from boto[. ]' *.py | xargs grep -lE 'import boto3|import botocore|from botocore' | sed 's/\(.*\)\.py$/* `\1`/'
```

Note the above finds `ec2_ami_copy` too but that's an unused import

### boto only
```
for f in `grep -lE 'import boto[^3c_]|import boto$|from boto[ .]|ec2_connect' *.py`; do
  grep -qE 'import boto3|import botocore|from botocore' $f || echo $f
done | sed 's/\(.*\)\.py$/* `\1`/'
```

### Neither boto nor boto3

```
for f in *.py; do grep -qE 'import boto|from botocore' $f || echo $f ; done | sed 's/\(.*\)\.py$/* `\1`/'
```
