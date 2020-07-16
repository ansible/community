# Integration Testing

There are very few integration tests for EC2. Those that
exist are in test/integration/targets

## Policy

Following the 2.4 release, all modules marked `stableinterface`
MUST have integration tests for new features. Upgrading to boto3
shall be considered a feature request.

Following the 2.5 release, all new modules MUST have integration
tests.

Following the 2.10 release, all modules MUST have integration tests.

Bug fixes for modules that currently have integration tests SHOULD
have tests added. Depending upon the urgency of the bug fix, we may
accept bug fixes without tests.

## Expected test criteria

* Resource creation under check mode
* Resource creation
* Resource creation again (idempotency) under check mode
* Resource creation again (idempotency)
* Resource modification under check mode
* Resource modification
* Resource modification again (idempotency) under check mode
* Resource modification again (idempotency)
* Resource deletion under check mode
* Resource deletion
* Resource deletion (of a non-existent resource) under check mode
* Resource deletion (of a non-existent resource)


Modules which still use boto and need to be ported are tracked
on the [AWS Project Board](https://github.com/orgs/ansible-collections/projects/4#column-9963846).
.
