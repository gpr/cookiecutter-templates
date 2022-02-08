# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}.

## Quick Start

```console
helm install -g --post-renderer tools/bin/kustomize.sh .
```

## Contribute

You must first install the system pre-requisites (see References):

- kubectl: run commands against Kubernetes clusters
- helm: manage Kubernetes applications
- kustomize: customize Kubernetes application
- kubeval: validate Kubernetes configuration files
- pre-commit: framework for managing and maintaining pre-commit hooks
- bump2version: Version-bumping
- git-chglog: CHANGELOG generator

Finally setup pre-commit:

```console
pre-commit install --install-hooks
```

See [Contribution Guide](CONTRIBUTING.md) for development rules and
also [the Code of Conduct](CODE_OF_CONDUCT.md).

### Checking the code

```console
helm template . | kubeval --strict
```

## References

- kubectl: [https://kubernetes.io/docs/tasks/tools/](https://kubernetes.io/docs/tasks/tools/)
- kustomize: [https://kustomize.io/](https://kustomize.io/)
- helm: [https://helm.sh/docs/intro/quickstart/](https://helm.sh/docs/intro/quickstart/)
- kubeval: [https://www.kubeval.com/](https://www.kubeval.com/)
- pre-commit: [https://pre-commit.com/](https://pre-commit.com/)
- bump2version: [https://pypi.org/project/bump2version/](https://pypi.org/project/bump2version/)
- git-chglog: [https://github.com/git-chglog/git-chglog](https://github.com/git-chglog/git-chglog)
