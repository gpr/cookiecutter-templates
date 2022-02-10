# Testing

Testing is performed on Virtualbox VM's managed with Vagrant and automatised
with Kitchen.

## Pre-requisites

Install manually Vagrant and Virtualbox then:

```shell
vagrant plugin install vagrant-vbguest
bundle install
```

## Launch tests

The following command will execute the test on all platforms:

```shell
bundle exec kitchen test
```

Every kitchen command can target a specific platform, to get the platforms list:

```console
$ bundle exec kitchen list
Instance          Driver   Provisioner  Verifier  Transport  Last Action    Last Error
ubuntu-focal64    Vagrant  AnsiblePush  Busser    Ssh        <Not Created>  <None>
debian-buster64   Vagrant  AnsiblePush  Busser    Ssh        <Not Created>  <None>
```

If the test fails you can login to the related VM:

```shell
bundle exec kitchen login ubuntu-focal64
```

## References

- [https://www.vagrantup.com](https://www.vagrantup.com)
- [https://www.virtualbox.org](https://www.virtualbox.org)
- [https://kitchen.ci](https://kitchen.ci)
- [https://rvm.io](https://rvm.io)
