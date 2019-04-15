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

| Module                       | PR                                                     |
|------------------------------|--------------------------------------------------------|
| ec2_eip                      | [50539](https://github.com/ansible/ansible/pull/50539) |
| ec2_metric_alarm             | [23407](https://github.com/ansible/ansible/pull/23407) |
| ec2_scaling_policy           | [26476](https://github.com/ansible/ansible/pull/26476) |
| ec2_vol                      | [45500](https://github.com/ansible/ansible/pull/45500) |
| ec2_vpc_route_table_facts    | [44966](https://github.com/ansible/ansible/pull/44966) |
| elb_classic_lb               | [45434](https://github.com/ansible/ansible/pull/45434) |
| elb_instance                 | [45434](https://github.com/ansible/ansible/pull/45434) |
| rds_cluster                  | [42128](https://github.com/ansible/ansible/pull/42128) |
| rds_facts                    | [19785](https://github.com/ansible/ansible/pull/19785) |
| rds_snapshot                 | [39994](https://github.com/ansible/ansible/pull/39994) |
| redshift                     | [37052](https://github.com/ansible/ansible/pull/37052) |
| route53_facts                | [31860](https://github.com/ansible/ansible/pull/31860) |
| route53_zone                 | [21646](https://github.com/ansible/ansible/pull/21646) |
| dynamodb_table               | [45402](https://github.com/ansible/ansible/pull/45402) |

TODO: add many more to the above list!

# State of the codebase (As at 2019-04-16)

## Summary

|Description            |Count|
|-----------------------|-----|
|boto3 only modules     |  153|
|boto3 *and* boto2      |    4|
|boto2 only modules     |   26|
|neither boto3 nor boto2|    8|

## boto3 only

* `aws_acm_facts`
* `aws_api_gateway`
* `aws_application_scaling_policy`
* `aws_az_facts`
* `aws_batch_compute_environment`
* `aws_batch_job_definition`
* `aws_batch_job_queue`
* `aws_caller_facts`
* `aws_codecommit`
* `aws_config_aggregation_authorization`
* `aws_config_aggregator`
* `aws_config_delivery_channel`
* `aws_config_recorder`
* `aws_config_rule`
* `aws_direct_connect_connection`
* `aws_direct_connect_gateway`
* `aws_direct_connect_link_aggregation_group`
* `aws_direct_connect_virtual_interface`
* `aws_eks_cluster`
* `aws_elasticbeanstalk_app`
* `aws_glue_connection`
* `aws_glue_job`
* `aws_inspector_target`
* `aws_kms_facts`
* `aws_kms`
* `aws_region_facts`
* `aws_s3_bucket_facts`
* `aws_s3_cors`
* `aws_s3`
* `aws_secret`
* `aws_ses_identity_policy`
* `aws_ses_identity`
* `aws_ses_rule_set`
* `aws_ssm_parameter_store`
* `aws_waf_condition`
* `aws_waf_facts`
* `aws_waf_rule`
* `aws_waf_web_acl`
* `cloudformation_facts`
* `cloudformation`
* `cloudformation_stack_set`
* `cloudfront_distribution`
* `cloudfront_facts`
* `cloudfront_invalidation`
* `cloudfront_origin_access_identity`
* `cloudtrail`
* `cloudwatchevent_rule`
* `cloudwatchlogs_log_group_facts`
* `cloudwatchlogs_log_group`
* `data_pipeline`
* `dynamodb_ttl`
* `ec2_ami_copy`
* `ec2_ami_facts`
* `ec2_ami`
* `ec2_asg_facts`
* `ec2_asg_lifecycle_hook`
* `ec2_asg`
* `ec2_customer_gateway_facts`
* `ec2_customer_gateway`
* `ec2_eip_facts`
* `ec2_eni_facts`
* `ec2_group_facts`
* `ec2_group`
* `ec2_instance_facts`
* `ec2_instance`
* `ec2_key`
* `ec2_launch_template`
* `ec2_lc_facts`
* `ec2_lc_find`
* `ec2_lc`
* `ec2_placement_group_facts`
* `ec2_placement_group`
* `ec2_snapshot_copy`
* `ec2_snapshot_facts`
* `ec2_tag`
* `ec2_transit_gateway_info`
* `ec2_transit_gateway`
* `ec2_vol_facts`
* `ec2_vpc_dhcp_option_facts`
* `ec2_vpc_egress_igw`
* `ec2_vpc_endpoint_facts`
* `ec2_vpc_endpoint`
* `ec2_vpc_igw_facts`
* `ec2_vpc_igw`
* `ec2_vpc_nacl_facts`
* `ec2_vpc_nacl`
* `ec2_vpc_nat_gateway_facts`
* `ec2_vpc_nat_gateway`
* `ec2_vpc_net_facts`
* `ec2_vpc_net`
* `ec2_vpc_peering_facts`
* `ec2_vpc_peer`
* `ec2_vpc_route_table`
* `ec2_vpc_subnet_facts`
* `ec2_vpc_subnet`
* `ec2_vpc_vgw_facts`
* `ec2_vpc_vgw`
* `ec2_vpc_vpn_facts`
* `ec2_vpc_vpn`
* `ecs_attribute`
* `ecs_cluster`
* `ecs_ecr`
* `ecs_service_facts`
* `ecs_service`
* `ecs_taskdefinition_facts`
* `ecs_taskdefinition`
* `ecs_task`
* `efs_facts`
* `efs`
* `elasticache_facts`
* `elasticache_parameter_group`
* `elasticache`
* `elasticache_snapshot`
* `elb_application_lb_facts`
* `elb_application_lb`
* `elb_classic_lb_facts`
* `elb_network_lb`
* `elb_target_facts`
* `elb_target_group_facts`
* `elb_target_group`
* `elb_target`
* `execute_lambda`
* `_iam_cert_facts`
* `iam_group`
* `iam_managed_policy`
* `iam_mfa_device_facts`
* `iam_password_policy`
* `iam_role_facts`
* `iam_role`
* `iam_server_certificate_facts`
* `iam_user`
* `kinesis_stream`
* `lambda_alias`
* `lambda_event`
* `lambda_facts`
* `lambda_policy`
* `lambda`
* `lightsail`
* `rds_instance_facts`
* `rds_instance`
* `rds_param_group`
* `rds_snapshot_facts`
* `redshift_cross_region_snapshots`
* `redshift_facts`
* `redshift`
* `route53_zone`
* `s3_lifecycle`
* `s3_sync`
* `s3_website`
* `sns`
* `sns_topic`
* `sts_assume_role`
* `sts_session_token`

## boto3 *and* boto

`aws_sgw_facts` and `s3_bucket` are false positives here. They are completely boto3 but an error message contains the string `boto.`.

* `aws_sgw_facts`
* `dynamodb_table`
* `route53_facts`
* `s3_bucket`

## boto only

* `ec2_eip`
* `ec2_elb_facts`
* `ec2_elb_lb`
* `ec2_elb`
* `ec2_eni`
* `ec2_metric_alarm`
* `ec2`
* `ec2_scaling_policy`
* `ec2_snapshot`
* `ec2_vol`
* `ec2_vpc_dhcp_option`
* `ec2_vpc_route_table_facts`
* `ec2_win_password`
* `elasticache_subnet_group`
* `elb_classic_lb`
* `elb_instance`
* `iam_cert`
* `iam_policy`
* `iam`
* `rds`
* `rds_subnet_group`
* `redshift_subnet_group`
* `route53_health_check`
* `route53`
* `s3_logging`
* `sqs_queue`

### Neither boto nor boto3

* `_ec2_ami_find`
* `_ec2_ami_search`
* `_ec2_facts`
* `ec2_metadata_facts`
* `_ec2_remote_facts`
* `_ec2_vpc`
* `__init__`
* `_s3`

## Commands for the above list

### boto3 only

```
for f in `grep -lE 'import boto3|import botocore|from botocore|AnsibleAWSModule' *.py`; do
  grep -Eq 'import boto[^3c_]|import boto$|from boto[ .]' $f || echo $f
done | sed 's/\(.*\)\.py$/* `\1`/'
```

### boto3 and boto2

```
grep -lE 'import boto[^3c_]|import boto$|from boto[. ]' *.py | xargs grep -lE 'import boto3|import botocore|from botocore' | sed 's/\(.*\)\.py$/* `\1`/'
```

### boto only
```
for f in `grep -lE 'import boto[^3c_]|import boto$|from boto[ .]|ec2_connect' *.py`; do
  grep -qE 'import boto3|import botocore|from botocore' $f || echo $f
done | sed 's/\(.*\)\.py$/* `\1`/'
```

### Neither boto nor boto3

```
for f in *.py; do grep -qE 'ec2_connect|import boto|from botocore|AnsibleAWSModule' $f || echo $f ; done | sed 's/\(.*\)\.py$/* `\1`/' | sort -f -n
```
