# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Install

To install this role in `$HOME/.ansible/roles`:

```console
ansible-galaxy install git+ssh://git@github.io/{{ cookiecutter.github_namespace }}/{{ cookiecutter.project_slug }}.git,master
```

You can also add this role in a `requirements.yml` file:

```YAML
- src: git@github.io/{{ cookiecutter.github_namespace }}/{{ cookiecutter.project_slug }}.git
  scm: git
  version: master
```

**NOTE**: You can replace _master_ reference by any valid branch or tag name.

## Requirements

> Any pre-requisites that may not be covered by Ansible itself or the role
should be mentioned here. For instance, if the role uses the EC2 module, it may
be a good idea to mention in this section that the boto package is required.

## Role Variables

> A description of the settable variables for this role should go here,
including any variables that are in defaults/main.yml, vars/main.yml, and any
variables that can/should be set via parameters to the role. Any variables that
are read from other roles and/or the global scope (ie. hostvars, group vars,
etc.) should be mentioned here as well.

## Dependencies

> A list of other roles hosted on Galaxy should go here, plus any details in
regards to parameters that may need to be set for other roles, or variables that
are used from other roles.

## Example Playbook

> Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

```yaml
    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }
```

## Contribute

See [CONTRIBUTING](CONTRIBUTING.md).

## License

See [LICENSE.txt](LICENSE.txt).
