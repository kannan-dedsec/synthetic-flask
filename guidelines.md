```markdown
# Flask Project Coding Guidelines

## Code Style
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code style.
- Use 4 spaces per indentation level; do not use tabs.
- Limit lines to a maximum of 79 characters.
- Use blank lines to separate functions and classes, and larger blocks of code inside functions.

## Import Organization
- Group imports in the following order:
  1. Standard library imports
  2. Related third-party imports
  3. Local application/library-specific imports
- Each group should be separated by a blank line.
- Use absolute imports whenever possible.
  
Example:
```python
import os
import sys

from flask import Flask, jsonify
from yourapp.models import User
```

## Naming Conventions
- Use `snake_case` for function and variable names.
- Use `CamelCase` for class names.
- Use all uppercase letters with underscores for constants (e.g., `MAX_CONNECTIONS`).
- Prefix private variables and methods with a single underscore (e.g., `_private_var`).
- Avoid single character variable names except for counters or iterators (e.g., `i`, `j`).

## Documentation
- Use docstrings to describe all public modules, classes, methods, and functions.
- Follow the [Google style guide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) for docstrings:
  - Use triple quotes for multi-line docstrings.
  - Include a brief description, parameters, and return types.
  
Example:
```python
def get_user(user_id):
    """Fetch a user by ID.

    Args:
        user_id (int): The ID of the user to fetch.

    Returns:
        User: The user object if found, None otherwise.
    """
    pass
```

## Common Pitfalls (Mutable Defaults)
- Avoid using mutable default arguments (e.g., lists, dictionaries) in function definitions.
- Instead, use `None` as a default and initialize the mutable object inside the function.

Example of a pitfall:
```python
def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list
```

Correct approach:
```python
def append_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list
```

## Conclusion
Adhering to these guidelines will help maintain code readability, consistency, and quality in your Flask project. Regularly review and refactor code to ensure compliance with these standards.
```
