# Contributing

This project is open source, but the default workflow is controlled by the repository owner.

## Default contribution model

- Fork the repository.
- Create a feature branch in your fork.
- Open a pull request back to `main`.
- Do not expect direct write access unless the owner explicitly adds you as a collaborator.

## Code changes

Before opening a pull request:

```bash
source .venv/bin/activate
python -m tenta_flash validate
python -m pytest
```

Keep pull requests small and focused. If you change behavior, update the docs in the same PR.

## Course content changes

If you want to add a new course or exam set:

1. Follow [Adding courses](/Users/edwind/tenta_flash/docs/adding-courses.md).
2. Validate the JSON content locally.
3. Confirm the course loads in the app.
4. Mention the course code, examiner, and exam dates in the PR description.

## Issues

Use issues for:

- bugs
- content requests
- usability problems
- suggestions for new study flows

## Owner-controlled access

The repository owner should keep `main` protected and only add trusted collaborators deliberately. Public users should work through forks and pull requests.
