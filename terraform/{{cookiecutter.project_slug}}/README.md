# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Quick Start

### Pre-requisites

Install Terraform (see [Terraform documentation][6]).

Set the providers parameters.

If you use [direnv][6] you can create a `.envrc` file (see [.envrc.template](/.envrc.template)).

Init the project:

```console
terraform init
```

### Deploy the infrastructure

With the same environment variables set during init:

```console
terraform plan -input=false -out=snapshot.tfplan
terraform apply -auto-approve -input=false snapshot.tfplan
```

<!-- BEGINNING OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
## Requirements

| Name                                                                      | Version |
|---------------------------------------------------------------------------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | ~> 0.14 |

## Providers

No providers.

## Modules

No modules.

## Resources

No resources.

## Inputs

No inputs.

## Outputs

No outputs.
<!-- END OF PRE-COMMIT-TERRAFORM DOCS HOOK -->

## Contributing

You must first install the system pre-requisites:

- [pre-commit][1]: enforce coding rules and tool usage
- [bump2version][2]: manager component version
- [markdownlint][3]: check markdown files and flag style issues
- [git-chglog][4]: generate changlog from git commits
- [direnv][5]: set automatically environment variables
- [terraform][6]: Terraform CLI
- [checkov][7]: security scanner
- [tflint][8]: terraform linter
- [tfsec][9]: terraform security checker
- [terraform-docs][10]: generate/update the Terraform docs

See [Contribution Guide](CONTRIBUTING.md) for development rules.

<!-- References -->
[1]: https://pre-commit.com/
[2]: https://pypi.org/project/bump2version/
[3]: https://github.com/markdownlint/markdownlint
[4]: https://github.com/git-chglog/git-chglog
[5]: https://direnv.net
[6]: https://learn.hashicorp.com/terraform/getting-started/install.html
[7]: https://github.com/bridgecrewio/checkov
[8]: https://github.com/terraform-linters/tflint
[9]: https://github.com/tfsec/tfsec
[10]: https://github.com/terraform-docs/terraform-docs
