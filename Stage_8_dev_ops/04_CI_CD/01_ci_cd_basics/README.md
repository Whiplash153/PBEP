# CI/CD Basics

## Goal

Understand the basic principles of Continuous Integration (CI) and how automated checks work before code reaches production.

In this practice:

- create a simple Python project;
- write automated tests;
- configure GitHub Actions;
- run tests automatically after pushing code.

---

## What is CI?

Continuous Integration (CI) is a development practice where every code change is automatically checked.

Instead of relying only on manual verification, the project runs automated processes:

1. Developer writes code.
2. Developer pushes changes to GitHub.
3. CI pipeline starts automatically.
4. Tests are executed.
5. Developer receives the result.

---

## Why do we need CI?

Without CI:

```
Developer writes code
        ↓
Code is merged
        ↓
Someone finds a bug later
```

With CI:

```
Developer writes code
        ↓
Push to GitHub
        ↓
Automated checks start
        ↓
Tests pass or fail
```

CI helps to:

- detect errors earlier;
- reduce human mistakes;
- keep the project stable when multiple developers work together.

---

## Project Structure

```
demo/
│
├── app/
│   └── calculator.py
│
├── tests/
│   └── test_calculator.py
│
├── requirements.txt
│
└── .github/
    └── workflows/
        └── tests.yml
```

---

## Tools

- Python
- pytest
- GitHub Actions

---

## CI Pipeline

The workflow:

```
Push code to GitHub
        ↓
GitHub Actions starts
        ↓
Install dependencies
        ↓
Run automated tests
        ↓
Success / Failure result
```

---

## Key Concepts

### Continuous Integration

A process where code changes are automatically checked.

### Pipeline

A sequence of automated steps executed after a trigger.

### Workflow

A configuration file that describes what actions should be performed.

### Automated Tests

Code that checks whether application behavior matches expected results.

---

## Result

After completing this task:

- understand the purpose of CI;
- understand the role of tests inside CI;
- know how GitHub Actions can automatically check code changes.