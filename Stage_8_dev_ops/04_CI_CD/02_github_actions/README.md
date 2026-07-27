# GitHub Actions

## Goal

Understand how GitHub Actions works and create a simple CI workflow for a Python project.

The main purpose is to automate code checks after changes are pushed to GitHub.

---

## What is GitHub Actions?

GitHub Actions is a CI/CD platform integrated into GitHub.

It allows developers to create automated workflows that run when specific events happen in a repository.

Examples:

- push to repository
- pull request creation
- manual workflow execution

---

## Workflow Structure

GitHub Actions workflows are stored in:

```
.github/workflows/
```

Example:

```
.github/
└── workflows/
    └── ci.yml
```

A workflow describes what actions GitHub should perform.

---

## Main Components

### Workflow

A complete automation process described in a YAML file.

Example:

```
ci.yml
```

### Event

Defines when the workflow should start.

Example:

```yaml
on:
  push:
  pull_request:
```

In this project the workflow starts after pushing changes or creating a pull request.

### Job

A group of steps that run on a virtual machine.

Example:

```yaml
jobs:
  test:
```

A workflow can contain multiple jobs.

### Runner

A machine where the workflow is executed.

Example:

```yaml
runs-on: ubuntu-latest
```

GitHub provides a temporary Linux environment for running the pipeline.

### Steps

Individual actions performed inside a job.

Example:

```yaml
steps:
  - checkout repository
  - setup Python
  - install dependencies
  - run tests
```

Each step performs one specific operation.

---

## CI Demo

Created a simple Python project:

```
demo_ci_cd/
├── app/
│   └── calculator.py
├── tests/
│   └── test_calculator.py
└── requirements.txt
```

The project contains:

- application code
- automated tests
- dependency list

---

## Created Workflow

Workflow file:

```
.github/workflows/ci.yml
```

Pipeline:

1. GitHub starts the workflow after push
2. Repository code is downloaded
3. Python 3.12 environment is created
4. Dependencies are installed
5. pytest runs automatically
6. GitHub reports success or failure

---

## Problems Solved During Setup

### Workflow Location

Initially the workflow was placed inside the demo project.

Correct location:

```
repository_root/
└── .github/
    └── workflows/
        └── ci.yml
```

GitHub Actions searches for workflows in this directory.

### Import Error

Pytest initially could not find the application module:

```
ModuleNotFoundError: No module named 'app'
```

The test command was configured with:

```bash
PYTHONPATH=demo_ci_cd pytest demo_ci_cd/tests
```

This adds the demo project to Python's module search path.

### Personal Access Token Permissions

GitHub initially rejected a push that modified the workflow because the Personal Access Token did not have permission to update workflow files.

The token permissions were updated and the workflow could then be pushed successfully.

---

## Result

A working CI pipeline was created with GitHub Actions.

Now every push automatically triggers the pipeline:

```
push
  ↓
GitHub Actions
  ↓
checkout repository
  ↓
setup Python
  ↓
install dependencies
  ↓
run pytest
  ↓
success / failure
```

The final workflow completed successfully.