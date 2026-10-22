# CI Midterm App

![CI](https://github.com/salasyo/cicd-midterm-project/actions/workflows/ci.yml/badge.svg)

A small Flask web app used to demonstrate a Continuous Integration "commit stage":
automated lint, test, and build on every push and pull request.

## Project structure
```
.
├── app.py                      # Flask application
├── test_app.py                 # pytest tests
├── requirements.txt            # dependencies
├── setup.py                    # packaging config
├── .flake8                     # lint rules
├── .gitignore
├── CONTRIBUTING.md             # branching + commit standards
└── .github/
    ├── workflows/ci.yml        # CI pipeline
    └── pull_request_template.md
```

## Run locally
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py            # http://localhost:5000
flake8 .                 # lint
pytest -v                # tests
pip install build && python -m build   # package
```

## Workflow
**Branching (simplified Git Flow):** `main` (stable) <- `develop` (integration) <- `feature/*`, `bugfix/*`.
Hotfixes branch from `main`. Details in [CONTRIBUTING.md](CONTRIBUTING.md).

**Day-to-day:**
1. `git checkout develop && git pull`
2. `git checkout -b feature/my-change`
3. Commit using Conventional Commits (`feat: ...`)
4. Push; CI runs automatically
5. Open a PR into `develop`; CI + one approving review required
6. Merge with a merge commit (keeps branch history visible); when ready, PR `develop` into `main`

## CI pipeline (`.github/workflows/ci.yml`)
**Triggers:** push to `main`, `develop`, `feature/**`, `bugfix/**`, `hotfix/**`; and every PR into `main` or `develop`.

| Job | What it does |
|-----|--------------|
| `lint` | Runs flake8 |
| `test` | Runs pytest on Python 3.11 and 3.12 |
| `build` | Builds sdist + wheel, installs the wheel, smoke-tests the import, uploads `dist/` artifact |
| `pr-title-check` | (PRs only) enforces the PR title convention |

## Branch protection
`main` and `develop` require a PR, one approval, and passing CI checks before merge.
