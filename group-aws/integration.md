# Integration Testing

Integration tests for AWS are in
tests/integration/targets/ in the relevant collection repository.

## Policy

All modules MUST have integration tests for new features.
All new modules MUST have integration tests.

Bug fixes for modules that currently have integration tests SHOULD
have tests added. Depending upon the urgency of the bug fix, we may
accept bug fixes without tests.

Where integration tests are impractical due to the need for non-AWS resources,
unit tests can be used instead. The `placebo` Python library provides a nice
mechanism for recording and mocking boto3 API responses and is preferred to
writing and maintaining AWS fixtures when possible.

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

Where modules have multiple parameters we recommend running through the 4-step
modification cycle for each parameter the module accepts, as well as a
modification cycle where as most, if not all, parameters are modified at the
same time.

Modules which still use boto and need to be ported are tracked
on the [AWS Project Board](https://github.com/orgs/ansible-collections/projects/4#column-9963846).
.
