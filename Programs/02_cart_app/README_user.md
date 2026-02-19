## Cart CLI Application

### Overview

Cart CLI Application is a console-based program that simulates a simple online shopping cart.
It allows users to add items, manage the cart, and complete an order while preserving state between program runs.

### Features
	•	Add items to the cart
	•	View current cart contents
	•	Clear all items
	•	Start checkout process
	•	Confirm order
	•	Persist cart state between sessions

### Cart Lifecycle

The cart can be in one of the following states:

EMPTY — the cart has no items
ACTIVE — the cart contains items
CHECKOUT — checkout process has started
ORDERED — order has been confirmed

State transitions occur automatically based on user actions.

### Available Commands
	1.	Show cart — display current cart state and items
	2.	Add item — add a new item to the cart
	3.	Clear cart — remove all items
	4.	Start checkout — initiate checkout process
	5.	Confirm order — confirm and complete the order
	6.	Quit — exit the application

### How It Works

After launching the application, a menu is displayed.
The user selects an action by entering the corresponding number.

The application automatically saves the cart state after each modification.

### Data Persistence

Cart data is stored in a JSON file.
When the program starts, the previous state is restored automatically if the file exists.

### Limitations
	•	Only one cart is supported
	•	No database integration
	•	No multi-user support
	•	No undo functionality
	•	Infrastructure errors are not handled gracefully