# boto3

So many features are available only for boto3 that we need
to ensure our modules can use it.

The current approach is typically that a contributor notices
a feature that they require, they realise it and:

* Create an [integration test suite](integration.md)
* Let contributors add new features

Once a module has a test suite, it'll be a lot easier to
enforce that new features must have tests.
