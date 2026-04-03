# GitHub Settings

These settings are not enforced from local code. Configure them on GitHub for the repository.

## Recommended repository setup

- Visibility: `Public`
- Issues: `Enabled`
- Pull requests: `Enabled`
- Wiki: optional
- Discussions: optional

## Branch protection for `main`

In GitHub:

1. Open repository `Settings`.
2. Open `Branches`.
3. Add a branch protection rule for `main`.

Recommended rule settings:

- require a pull request before merging
- disallow force pushes
- disallow deletion
- require approvals if you later want review gates
- require status checks once CI exists
- restrict who can push if you add collaborators later

## Collaborator policy

Recommended default:

- no outside direct collaborators
- outside users contribute through forks and pull requests
- add direct collaborators only if you trust them to work close to `main`

## Suggested maintainer workflow

1. Users fork the repo.
2. Users open PRs.
3. You review and merge manually.
4. You keep final control of what lands on `main`.
