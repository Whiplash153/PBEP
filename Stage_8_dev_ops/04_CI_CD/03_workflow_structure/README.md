# Workflow Structure

## Goal

Understand the internal structure of GitHub Actions workflow files and learn how different parts of CI/CD pipeline interact with each other.

## What was done

Studied the structure of GitHub Actions workflow:

- `on` — defines events that trigger workflow execution.
- `jobs` — defines independent tasks that workflow performs.
- `runs-on` — defines the virtual machine environment where job runs.
- `steps` — defines sequential actions inside a job.
- `uses` — runs predefined GitHub Actions.
- `run` — executes custom terminal commands.

Analyzed existing CI workflow and created a learning copy:

`.github/workflows/ci_learning.yml`

Added an additional step to check Python version inside GitHub Actions environment.

Verified that:

- `actions/setup-python` prepares Python environment.
- `run: python --version` executes command inside prepared environment.
- GitHub Actions runs independently from local machine environment.

## Notes

GitHub Actions workflow execution flow:

git push

↓

workflow trigger (`on`)

↓

job creation

↓

runner environment (`runs-on`)

↓

services setup (for example PostgreSQL container)

↓

steps execution

↓

tests execution

Important concepts:

- GitHub Actions does not use local computer environment.
- PostgreSQL from `services` creates a temporary database inside GitHub Runner environment.
- `localhost` inside GitHub Actions refers to the Runner environment, not the developer computer.
- Workflow steps execute sequentially from top to bottom.