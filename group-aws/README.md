# Amazon Web Services Working Group

There are two related collections containing AWS content (modules and plugins).

## amazon.aws
This collection contains the `module_utils` (shared libraries) used by both collections.
Content in this collection is included downstream in Red Hat Ansible Automation Platform.

Code standards, test coverage, and other supportability criteria may be higher in this collection.

The `amazon.aws` collection is an [Ansible-maintained collection](https://docs.ansible.com/ansible/devel/community/contributing_maintained_collections.html).

## community.aws
This collection contains modules and plugins contributed and maintained by the Ansible AWS
community.  The `community.aws` collection is tested and generally assured to work in
conjunction with `amazon.aws`.

New modules and plugins developed by the community should be proposed to `community.aws`.
Content in this collection that is stable and meets other acceptance criteria has the potential
to be promoted and migrated into `amazon.aws`.

## Meetings

There are currently no regular meetings held. The IRC channel is the
main and official place to contact the members. For specific issues and
feature requests, follow the standard Ansible issues/PRs workflow.

## Working Group Goals

* Review PRs and Issues with a view to reducing the number of open
  PRs and Issues. Numbers going up is not a failure, it might just
  be due to additional contributors.
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
requests in the collection repositories.
* `amazon.aws` [Tickets](https://github.com/ansible-collections/amazon.aws/issues?utf8=%E2%9C%93&q=is%3Aissue%20is%3Aopen%20label%3Aaws)
* `amazon.aws` [Pull-requests](https://github.com/ansible-collections/amazon.aws/pulls?q=is%3Apr+is%3Aopen%20label%3Aaws)
* `community.aws` [Tickets](https://github.com/ansible-collections/community.aws/issues?utf8=%E2%9C%93&q=is%3Aissue%20is%3Aopen%20label%3Aaws)
* `community.aws` [Pull-requests](https://github.com/ansible-collections/community.aws/pulls?q=is%3Apr+is%3Aopen%20label%3Aaws)

Planned work for both collections is tracked in the [AWS Project Board](https://github.com/orgs/ansible-collections/projects/4).
## Contact
* [#ansible-aws IRC channel](https://webchat.freenode.net/?channels=ansible-aws) on Freenode.net
* For security-related concerns email security@ansible.com and see our
    [security disclosure](https://www.ansible.com/security) for more
    information.
* For other urgent or sensitive issues contact shertel@redhat.com or
    jillr@redhat.com
