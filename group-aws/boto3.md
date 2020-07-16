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

Modules which still use boto and need to be ported are tracked
on the [AWS Project Board](https://github.com/orgs/ansible-collections/projects/4#column-9964369)

