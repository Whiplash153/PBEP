# Task 5: Case — Order calculator

**What I did**  
Combined everything learned about functions and modules into one small project: a calculator for orders.

**Key points**  
- Functions can be grouped into a separate module (`order_calc.py`) and reused in the main script.  
- Each function solves a small part of the task:  
  - `subtotal(items)` — calculates the base sum.  
  - `apply_discount(amount, percent)` — applies a discount.  
  - `add_tax(amount, percent)` — adds tax.  
  - `final_total(items, discount_percent, tax_percent)` — combines all steps.  
- This shows how simple functions build up into a practical tool.

**Practice**  
- Created a shopping cart (list of items as `(price, quantity)`).  
- Calculated subtotal, applied discount, added tax step by step.  
- Used one combined function `final_total` to do the same in a single call.  
- Compared both approaches and confirmed results are identical.

**Artifacts**  
- `order_calc.py` — module with functions for calculation  
- `app.py` — main script that uses the module