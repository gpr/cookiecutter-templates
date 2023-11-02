# Contribution Guide

## Workflow

  1. Create your feature branch or checkout (`git checkout -b <branch-name>
     origin/master`)
  2. Commit your changes (`git commit -m '<type>(<scope>): summary'`)
  3. Push your branch (`git push --set-upstream origin <branch-name>`)
  4. Create a new _Merge Request_

## Commit Message Convention

The format of the commit message must be:

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

Any line of the commit message should not be longer 100 characters!

### Subject

The subject contains a succinct description of the change:

 * use the imperative, present tense: "change", not "changed" nor "changes"
 * don't capitalize the first letter
 * no dot (.) at the end

#### Scope

The `<scope>` is optional and it should be the name of the high level component
affected by the change.

#### Type

The `<type>` must be one of the following:

 * feat: A new feature (appear in changelog)
 * fix: A fix for a known bug affecting a release (appear in changelog)
 * perf: Performance improvement
 * docs: Documentation only changes
 * style: Changes that do not affect the meaning of the code (white-space,
          formatting, missing semi-colons, etc)
 * refactor: any code change that neither fixes a known bug nor adds a feature
 * test: Adding tests
 * chore: Changes to the build process or auxiliary tools and libraries such as
          documentation generation
 * auto: Automatic commit performed by tools

### Body

The body is optional it must be used when a detailed description is required or
to provide any useful information.

### Footer

The footer should contain any information about Breaking Changes, deprecation
warning and is also the place to reference Gitlab/Jira issues that this commit
closes.

Breaking Changes should start with the word `BREAKING CHANGE:` with a space or
two newlines. The rest of the commit message is then used for this.

Deprecation warning should start with the word `DEPRECATED:` with a space or
two newlines. The rest of the commit message is then used for this.
