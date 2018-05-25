## 2017 is the year of Zuul on the Desktop

[Monty' Sides](http://inaugust.com/talks/test-it-like-you-deploy-it.html)

[Link to the Zuul v3 source](https://git.openstack.org/cgit/openstack-infra/zuul)

freenode: `#zuul`  - talk to jeblair - he knows all of the things

Support for Ansible Tower in v3?

* Support for co-dependent changes? (easier than fixing python-requests)

  * not built in currently, but should not be terribly difficult to implement
  * this is required for the packaging use-case (imagine python requests / urllib3 which need to be upgraded together)

Support for asynchronous execution?

What will the name be when Netflix sues? https://github.com/Netflix/zuul

* Probably the movie studio would do that to both projects first :) But also: hooray for glossing over legal questions in places! :)
* "There is no Dana, only Zuul." Project Dana?

Support for third-party CI?

Future of provisioning nodes across infrastructures and the like. Pluggable alternatives?

https://github.com/CentOS-PaaS-SIG/linch-pin

How will Zuul help run CI tests locally before submitting a PR, if possible?

http://git.openstack.org/cgit/openstack-infra/zuul/tree/TESTING.rst

http://specs.openstack.org/openstack-infra/infra-specs/specs/zuulv3.html

https://review.openstack.org/#/q/project:openstack-infra/infra-specs+status:open -- look for ones that mention Zuul v3

https://storyboard.openstack.org/#!/project/679

## Things to talk about on Tuesday  -- 9am in Park Slope (the room, not the neighbourhood) south tower

* Async task execution with Fedora / How modular/separable is it / Taskotron - 9 - 11
* Crazy kubernetes guy whiteboard from Intel - 3-5
* Galaxy / associating zuul with roles in galaxy - 11-12
* linch-pin / provisioning - 1-3
