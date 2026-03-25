import os
from os.path import exists

print("=== OS Environment Variables ===")

print("Total environment variables:", len(os.environ))

print("Current USER:", os.environ.get("USER", "unknown"))
print("Home directory:", os.environ.get("HOME", "noе found"))

print("\nPath variable")
print(os.environ.get("PATH", ""))

os.environ["MY_PROJECT_MODE"] = "development"
print("\nCustom variable set:", os.environ["MY_PROJECT_MODE"])

if "MY_PROJECT_MODE" in os.environ:
    print("MY_PROJECT_MODE exists in environment!")

del os.environ["MY_PROJECT_MODE"]
print("Custom variable deleted:", "MY_PROJECT_MODE" not in os.environ)

print("\n=== DONE ===")