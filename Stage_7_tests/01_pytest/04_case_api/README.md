## Goal  
Apply pytest features (fixtures and parametrize) to test a simple API-like system.

## What was done  
Implemented a simple user API using functions (create, get, delete). Wrote tests to verify user creation, retrieval, and deletion. Used fixtures to reset state before each test and parametrize to test multiple input values.

## Notes  
Tests simulate API behavior without a real framework. Fixtures ensure clean state between tests. Parametrize allows testing multiple scenarios with minimal code.