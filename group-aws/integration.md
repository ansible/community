# Integration Testing

There are very few integration tests for EC2. Those that
exist are in test/integration/targets

## Policy

Following the 2.4 release, all modules marked `stableinterface`
MUST have integration tests for new features. Upgrading to boto3
shall be considered a feature request.

Following the 2.5 release, all new modules MUST have integration
tests.

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

# State of the codebase (at 2019/09/05)

Existing test suites:

* `aws_api_gateway`
* `aws_caller_info`
* `aws_codebuild`
* `aws_codecommit`
* `aws_codepipeline`
* `aws_config`
* `aws_eks`
* `aws_elasticbeanstalk_app`
* `aws_glue_connection`
* `aws_inspector`
* `aws_kms`
* `aws_lambda`
* `aws_s3`
* `aws_secret`
* `aws_ses_identity`
* `aws_ses_identity_policy`
* `aws_ses_rule_set`
* `aws_ssm_parameters`
* `aws_waf_web_acl`
* `cloudformation_stack_set`
* `cloudformation_stack_set`
* `cloudfront_distribution`
* `ec2_ami`
* `ec2_asg`
* `ec2_eip`
* `ec2_elb_lb`
* `ec2_group`
* `ec2_instance`
* `ec2_key`
* `ec2_launch_template`
* `ec2_tag`
* `ec2_transit_gateway`
* `ec2_vol_info`
* `ec2_vpc_egress_igw`
* `ec2_vpc_igw`
* `ec2_vpc_nat_gateway`
* `ec2_vpc_net`
* `ec2_vpc_route_table`
* `ec2_vpc_subnet`
* `ec2_vpc_vgw`
* `ec2_vpc_vpn_facts`
* `ecs_cluster`
* `ecs_ecr`
* `elb_application_lb`
* `elb_classic_lb`
* `elb_network_lb`
* `elb_target`
* `elb_target_info`
* `lambda_policy`
* `rds_instance`
* `rds_param_group`

Note that the above list is not exhaustive because some targets contain test suites for
other modules (e.g. the `aws_waf_web_acl` test suite also contains tests for `aws_waf_condition`
 and `aws_waf_rule` modules)

List generated with:

```
echo {cloudf,ec2,aws,lambda,elb,ecs,rds}*{/tasks/main.yml,/runme.sh} aws*/tasks/main.yaml  | xargs -n1 wc -l | awk '$1 > 2 {print $2}' | awk -F/ '{printf("* `%s`\n", $1)}' | sort
```

(the `$1 > 2` test avoids two test suites with a two line tasks/main.yml. The `echo | xargs -n1` avoids the `total` printed when `wc`ing multiple files.)

Modules with no tests:

* `aws_acm_info`
* `aws_application_scaling_policy`
* `aws_az_info`
* `aws_batch_compute_environment`
* `aws_batch_job_definition`
* `aws_batch_job_queue`
* `aws_direct_connect_connection`
* `aws_direct_connect_gateway`
* `aws_direct_connect_link_aggregation_group`
* `aws_direct_connect_virtual_interface`
* `aws_glue_job`
* `aws_region_info`
* `aws_s3_cors`
* `aws_sgw_info`
* `cloudformation_info`
* `cloudfront_info`
* `cloudfront_invalidation`
* `cloudfront_origin_access_identity`
* `cloudtrail`
* `cloudwatchevent_rule`
* `data_pipeline`
* `dynamodb_table`
* `dynamodb_ttl`
* `ec2_ami_copy`
* `ec2_asg_lifecycle_hook`
* `ec2_customer_gateway_info`
* `ec2_eip_info`
* `ec2_elb_info`
* `ec2_lc_find`
* `ec2_lc_info`
* `ec2_metadata_facts`
* `ec2_metric_alarm`
* `ec2_placement_group_info`
* `ec2_placement_group`
* `ec2_scaling_policy`
* `ec2_snapshot_copy`
* `ec2_vpc_dhcp_option_info`
* `ec2_vpc_igw_info`
* `ec2_vpc_nacl_info`
* `ec2_vpc_nacl`
* `ec2_vpc_nat_gateway_info`
* `ec2_vpc_net_info`
* `ec2_vpc_peering_info`
* `ec2_vpc_vgw_info`
* `ec2_win_password`
* `ecs_attribute`
* `elasticache_info`
* `elasticache_parameter_group`
* `elasticache`
* `elasticache_snapshot`
* `elasticache_subnet_group`
* `elb_application_lb_info`
* `elb_classic_lb_info`
* `elb_instance`
* `elb_target_group_info`
* `iam_mfa_device_info`
* `iam_server_certificate_info`
* `kinesis_stream`
* `lambda_event`
* `lightsail`
* `rds_instance_info`
* `rds_subnet_group`
* `redshift_cross_region_snapshots`
* `redshift_info`
* `redshift_subnet_group`
* `route53_health_check`
* `s3_logging`
* `s3_sync`
* `s3_website`
* `sts_session_token`

Note that the above list only covers modules for which no usage whatsoever exists in any test suite.  Some modules may have usages in the targets for another module, but not themsleves have dedicated tests nor adequate coverage.

List generated with:

```
lib/ansible/modules/cloud/amazon$ for i in `ls| awk -F'.' '/py/ && !/^_/ {print $1}'`; do grep -rq ${i} ../../../../../test/integration/targets/ ; if [ $? -ne 0 ]; then echo ${i}; fi ; done
```

