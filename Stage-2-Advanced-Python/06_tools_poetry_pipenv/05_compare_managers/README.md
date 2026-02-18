# Task 5 — Poetry vs Pipenv

### Goal
Compare two environment and dependency managers — **Poetry** and **Pipenv**.

---

### Comparison

| Aspect | Poetry | Pipenv |
|--------|---------|--------|
| Config files | `pyproject.toml` + `poetry.lock` | `Pipfile` + `Pipfile.lock` |
| Virtual environment | Creates automatically in cache | Tends to use or create local venvs |
| Install dependencies | `poetry add package` | `pipenv install package` |
| Run scripts | `poetry run python file.py` | `pipenv run python file.py` |
| Build package | `poetry build` (creates wheel & tar.gz) | Not supported |
| Export to requirements | via plugin (`poetry-plugin-export`) | built-in (`pipenv lock -r`) |
| Output files | clean structure | creates extra files when nested |

---

### Observations
Both tools automate dependency and environment management.  
However, **Poetry** gives cleaner control, integrates with modern tooling, and fits better for scalable projects.  
**Pipenv** feels simpler but behaves inconsistently inside another virtual environment.

---

### Conclusion
Poetry is more predictable and modular for long-term development.  
In this test, both worked — but Poetry kept the workspace cleaner.