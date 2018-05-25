# Ansible Contributor Summit Ansible and Containers
21-06-2017


Subtopics from original planning etherpad (https://public.etherpad-mozilla.org/p/ansible-summit-june-2017):

Ansible-container
Ansible + Other Containers
Ansible + Kubernetes / Helm
https://github.com/ansible/ansible-kubernetes-modules
https://github.com/ansible/ansible/pull/24883

## IN-ROOM DISCUSSION

* Ansible-Container: Need to get into 1.0:
  * Prebaked conductor images: right now, every build does a rebuild of the conductor container, which is 2 network connections. We've got a branch for pre-baking the 11 most common conductor versions, so you never have to pull it again. Then you build a layer on top.
    * Community can help keep these pre-baked images up to date, and we have scripts to build/rebuild/test against/push them.
    * Need to figure out what's going on with the test matrix in Travis.
  * Solve the Python 3 problem. At present, we bring the Python 2.7 from conductor into targets. If you're building Python 3 in the target, we set the PYTHONPATH env variable, but this is not versioned, so Python 3 tries to source the Python 2.7 libraries. Possible solution: we could use the User's PYTHONPATH /sitepackages instead, except for Ubuntu, which uses /distpackages. Also can't do virtualenv for same problem. So instead shim around Python itself for the Ansible Python version in the conductors, and we set the environment variable for just the conductor process.
  *  Happy path continues to be Docker on the desktop, then push to Openshift/Kubernetes.
  * Will need mechanisms for multiple people to commit changes
  * If we're prebaking conductors, we need to update every time Docker does a release, but this is pretty simple to do it (maybe an automatic travis job)
    * Do we always need latest Docker?
  * We will set up an ansible-container SIG to carry this work forward (gregdek)
* Kubernetes modules:
  * We have kube modules in Galaxy presently
  * Include the roles in your playbook currently
  * Do we want Kubernetes modules in Ansible itself?
    * No, especially with potential changes coming, we'll leave the Kube modules where they are
* Helm module
  * Landed today
  * Flavio is delighted
* Reach out to the folks filing big bugs
  * EdX guy
  * Eric Helms is already working on stuff

## ACTION ITEMS

