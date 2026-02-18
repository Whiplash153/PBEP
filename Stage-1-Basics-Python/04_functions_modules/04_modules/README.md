# Task 4: Modules

**What I did**  
Learned how to put functions into a separate file (module) and import them into other scripts.

**Key points**  
- A module in Python is just a `.py` file with functions or variables.  
- `import mymath` imports the whole module → use functions with the prefix: `mymath.add(…)`.  
- `from mymath import add, div` imports specific functions → can call them directly.  
- Functions can also be imported with aliases, e.g. `from mymath import div as divide`.  
- Modules can be imported if they are:  
  - in the same folder as the script,  
  - in a package (folder with `__init__.py`),  
  - installed in the environment (`site-packages`).

**Practice**  
- Wrote a simple module `mymath.py` with functions: add, sub, mul, div.  
- Imported the module as a whole and used its functions.  
- Imported only specific functions and used an alias.  
- In practice, combined results of functions to calculate `(5 + 3) * (10 - 2)` and divided `100 / 4`.  

**Artifacts**  
- `mymath.py` — module with math functions  
- `use_module.py` — import whole module  
- `use_from.py` — import specific functions with alias  
- `task.py` — mini-practice with module functions