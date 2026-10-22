# Contributing

## Branching model (simplified Git Flow)
- `main`: always releasable; protected, only updated via approved PRs
- `develop`: integration branch; protected, PRs only
- `feature/<short-name>`: new work, branched from `develop`
- `bugfix/<short-name>`: fixes, branched from `develop`
- `hotfix/<short-name>`: urgent fixes, branched from `main`

## Commit messages (Conventional Commits)
Format: `type(optional-scope): imperative summary`
Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `ci`
Examples:
- `feat: add /health endpoint`
- `ci: add pytest matrix for Python 3.11 and 3.12`

## Pull requests
1. Open a PR from your feature branch into `develop`.
2. PR title must follow the commit format (checked by CI).
3. Fill out the PR template.
4. CI must pass and one reviewer must approve before merging.
