# WE WANT PULL REQUESTS FOR ANSIBLE NETWORKING DOCUMENTATION

## 5 pull requests == 1 t-shirt shipped to your house

![t-shirt](https://lf.staplespromotionalproducts.com/lf?set=scale[1200],env[live],output_format[png],sku_number[200284094],sku_dir[200284],view_code[F1]%26call=url[file:san/com/sku.chain])

- keep pull requests simple
- keep pull requests small
- keep pull requests succinct

Documentation pull requests can be a 1-task example... in fact we encourage very simple 1-task examples!

## RULES

- must be a PR for Ansible Networking modules that are already part of the project: http://docs.ansible.com/ansible/latest/modules/list_of_network_modules.html
- submit PR against this issue-> https://github.com/ansible/ansible/issues/40323
- email ansible-network@redhat.com after you reach 5 pull request with your t-shirt size

## EXAMPLE PULL REQUEST

https://github.com/ansible/ansible/pull/40021

All I did for the [ios_l3_interface](https://docs.ansible.com/ansible/devel/modules/ios_l3_interface_module.html) module was add this example to the documentation after testing it on my own Cisco switch

```
- name: Set interface Vlan1 (SVI) IPv4 address
  ios_l3_interface:
    name: Vlan1
    ipv4: 192.168.0.5/24
```

**HINT** you can probably steal my pull request above for other vendor interface modules, e.g. eos_l3_interface, junos_l3_interface, etc, just test it out and make sure it works on your equipment/vms

## HOW? HOW DO I DO IT?

1) Create a fork!
Create a fork on your own Github personal space
[Github Documentation on Forking a repo](https://help.github.com/articles/fork-a-repo/)

Ensure your fork is upto date http://docs.ansible.com/ansible/latest/dev_guide/developing_rebasing.html

2) Configuring Your Remotes
Configure github.com/ansible/ansible as your upstream so you can stay in sync
`git remote add upstream https://github.com/ansible/ansible.git`

3) Rebasing Your Branch
`git pull --rebase upstream master`

## CREATE THE PULL REQUEST

https://help.github.com/articles/creating-a-pull-request/

Please comment here if you have questions or we need more documentation to make this process easy!

