## Goal  
Understand how pytest fixtures work and how to reuse shared data across multiple tests.

## What was done  
Created simple fixtures in conftest.py and used them in test functions without direct imports. Verified that pytest injects data into tests based on argument names. Implemented basic tests using shared input data.

## Notes  
Fixtures are registered using @pytest.fixture and injected into tests by name. conftest.py allows sharing fixtures across multiple test files. Fixtures reduce code duplication and simplify test setup.