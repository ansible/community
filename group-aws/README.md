# Amazon Web Services Working Group

The AWS Working Group focuses on delivering modules and features to
Ansible to support working with Amazon Web Services.

## Meetings

There are currently no regular meetings held. The IRC channel is the
main and official place to contact the members. For specific issues and
feature requests, follow the standard Ansible issues/PRs workflow.

## Working Group Goals

* [Review PRs and Issues](review.md) with a view to reducing the number of open
  PRs and Issues. Numbers going up is not a failure, it might just
  be due to additional contributors.
* [Refactor problematic modules](refactor.md) - the key problem areas
  are `rds` and `iam`. Some minor renaming will also fall under this.
* [Move to boto3](boto3.md) - all AWS modules should move to boto3, rather
  than boto. This is happening organically, especially as newer features
  typically exist in boto3 only, but we might want to improve this.
* [Integration tests](integration.md) - all AWS modules should have integration
  tests so that we can update them with confidence that we won't break
  other people's stuff
* [Best practices](bestpractices.md) - all modules should meet the Ansible best
  practices, such as python coding standards, documentation.
* Improve simplify and expand the [AWS module utilities](utility-modules.md) and module
  utilities generally to make it easier to both write and maintain modules

## Collaboration

Apart from IRC The AWS Working Group collaborates via tickets and pull
requests in the main Ansible repository.
* [Tickets](https://github.com/ansible/ansible/issues?utf8=%E2%9C%93&q=is%3Aissue%20is%3Aopen%20label%3Aaws)
* [Pull-requests](https://github.com/ansible/ansible/pulls?q=is%3Apr+is%3Aopen%20label%3Aaws)

## Leads
Leads are still to be agreed.

## Active Members
* [Sloane Hertel](https://github.com/s-hertel), shertel
* [Ryan Brown](https://github.com/ryansb), ryansb
* [Michael De La Rue](https://github.com/mikedlr), mikedlr
* [William Thames](https://github.com/willthames), willthames

## Contact
* [#ansible-aws IRC channel](https://webchat.freenode.net/?channels=ansible-aws) on Freenode.net
* For security-related concerns email security@ansible.com and see our
    [security disclosure](https://www.ansible.com/security) for more
    information.
* For other urgent or sensitive issues contact shertel@redhat.com or
    ryansb@redhat.com
