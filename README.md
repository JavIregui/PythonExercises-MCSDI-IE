# Python Exercises · MCSDI @ IE

A living compilation of Python exercises completed as part of the **Programming with Python** course in the **Master in Computer Science & Digital Innovation (MCSDI)** at **IE University**.

Each session has its own directory so that examples, experiments, and solutions remain easy to find and run independently while sharing one Python environment.

## Exercise index

| Session | Exercises                                                                   | Location                                       |
| ------- | --------------------------------------------------------------------------- | ---------------------------------------------- |
| S1      | Interactive calculator: addition, subtraction, multiplication, and division | [`S1/src/calculator.py`](S1/src/calculator.py) |

## Project structure

```text
.
├── S1/                         # Session 1 exercises
│   └── src/
│       └── calculator.py
├── pyproject.toml               # Python and uv project configuration
├── uv.lock                      # Reproducible dependency versions
└── README.md
```

New classwork should normally follow the same convention:

```text
S<number>/
└── src/
    └── exercise_name.py
```

## Prerequisites

- [Git](https://git-scm.com/downloads)
- A Python version compatible with this project (currently Python 3.14 or newer)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Access to the GitHub repository

Check that the tools are available:

```bash
git --version
uv --version
python --version
```

## Run an exercise with uv

From the repository root, create or update the local virtual environment from the locked project configuration:

```bash
uv sync
```

Then run an exercise from the root:

```bash
uv run python S1/src/calculator.py
```

You can also work directly from an individual session directory:

```bash
cd S1
uv run python src/calculator.py
```

`uv` searches parent directories for `pyproject.toml`, so it still uses this repository's configuration and environment. In addition, this setting in `pyproject.toml`:

```toml
[tool.uv]
package = false
```

marks the repository as an application/exercises project rather than a distributable Python package. Therefore uv does not need to build or install a project package before running scripts; this keeps the session-level command above straightforward.

When dependencies are added or `pyproject.toml` / `uv.lock` changes, run `uv sync` again. Do not commit `.venv/`; it is machine-specific and can always be recreated with `uv sync`.

## Work from another computer

The source code and dependency lockfile belong in Git; each computer creates its own `.venv` locally.

### First time on a computer

Clone the repository, enter it, and recreate the environment:

```bash
git clone https://github.com/JavIregui/PythonExercises-MCSDI-IE.git
cd PythonExercises-MCSDI-IE
uv sync
```

You can now run any exercise, for example:

```bash
cd S1
uv run python src/calculator.py
```

### When switching computers later

Before starting work, retrieve the latest shared changes and synchronise the local environment:

```bash
git switch main
git pull --ff-only origin main
uv sync
```

`git pull --ff-only` deliberately stops instead of creating an unexpected merge commit. If it reports local work, commit or stash that work before pulling. Run `uv sync` after pulling whenever the dependency files may have changed; it is safe to run even when they have not.

At the end of a work session, use one of the workflows below to send your changes to GitHub before moving to the other computer.

## Git workflows

Run these commands from the repository root. Start either workflow by checking what changed:

```bash
git status
```

### Workflow A: one commit per day

Use this for small, self-contained daily additions. Work directly on `main`.

```bash
git switch main
git pull --ff-only origin main
git add S1 README.md                 # Replace with the files changed today
git commit -m "Add S1 calculator exercise"
git push origin main
```

On the other computer, run:

```bash
git switch main
git pull --ff-only origin main
uv sync
```

Avoid `git add .` unless you have reviewed `git status` and intentionally want to include every changed file.

### Workflow B: one branch per session or feature

Use this when an exercise spans multiple edits, a whole class session, or you want to keep `main` stable until the work is ready.

Create a descriptive branch from an up-to-date `main`:

```bash
git switch main
git pull --ff-only origin main
git switch -c s2-lists-and-loops
```

Commit work as you progress and push the branch so it is available from the other computer:

```bash
git add S2 README.md                  # Replace with the files changed
git commit -m "Add S2 list exercises"
git push -u origin s2-lists-and-loops
```

To continue this branch from another computer:

```bash
git fetch origin
git switch s2-lists-and-loops
git pull --ff-only origin s2-lists-and-loops
uv sync
```

When the work is complete, merge it into `main` locally and publish the result:

```bash
git switch main
git pull --ff-only origin main
git merge --no-ff s2-lists-and-loops -m "Merge S2 exercises"
git push origin main
```

Then clean up the branch after confirming that the merge was pushed:

```bash
git branch -d s2-lists-and-loops
git push origin --delete s2-lists-and-loops
```

Alternatively, open a GitHub pull request from the branch to `main`, merge it on GitHub, then update your local `main` with `git pull --ff-only origin main`.

## Useful checks

```bash
git status                         # See the current branch and local changes
git log --oneline --decorate -10   # See recent commits
uv sync                            # Reconcile the local environment with uv.lock
```

Keep commits focused, use meaningful messages, and push completed work before changing computers. This makes the repository both a reliable backup and a clear record of the course progression.
