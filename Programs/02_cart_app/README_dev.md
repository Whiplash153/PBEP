## Cart CLI Application — Developer Documentation

### Architecture Overview

The application follows a layered architecture with clear separation of concerns:

CLI Layer
Handles user input and output.
Responsible for:
	•	Displaying menu
	•	Validating input
	•	Catching domain exceptions
	•	Calling domain operations

Domain Layer
Contains business logic and state management.
Responsible for:
	•	Cart behavior
	•	State transitions
	•	Enforcing business rules
	•	Raising domain-specific errors

Infrastructure Layer (Storage)
Handles persistence.
Responsible for:
	•	Loading cart from JSON
	•	Saving cart to JSON
	•	Creating file if missing

### Core Domain Model

Cart

Main aggregate root.

Attributes:
	•	id
	•	state
	•	items

Business operations:
	•	add_item()
	•	remove_all_items()
	•	start_checkout()
	•	confirm_order()

State transitions are strictly controlled and validated inside the domain layer.

### State Machine

EMPTY → ACTIVE → CHECKOUT → ORDERED

Allowed transitions:
	•	EMPTY → ACTIVE (via add_item)
	•	ACTIVE → EMPTY (via remove_all_items)
	•	ACTIVE → CHECKOUT (via start_checkout)
	•	CHECKOUT → ORDERED (via confirm_order)

Any invalid transition raises OperationNotAllowedError.

### Error Handling Strategy

CLI Input Errors

Handled in CLI:
	•	Invalid menu choice
	•	Empty input
	•	Invalid item value

User is returned to the menu.

Domain Errors

OperationNotAllowedError
	•	Raised in domain
	•	Caught in CLI
	•	Displayed to user

Infrastructure Errors

Not handled:
	•	JSONDecodeError
	•	Corrupted file
	•	Write failure

Program terminates on infrastructure failure.

### Persistence

Cart state is serialized into JSON.

Storage responsibilities:
	•	load() — returns Cart instance
	•	save(cart) — writes Cart state
	•	Creates file automatically if missing

Only a single cart instance is supported.

### Design Principles Applied
	•	Separation of concerns
	•	Explicit state management
	•	Controlled state transitions
	•	Domain-driven error signaling
	•	CLI as orchestration layer only