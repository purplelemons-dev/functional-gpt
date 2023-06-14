"""
Makes using GPT-4's Function calling easier.

Example:
```py

import fgpt, openai
openai.api_key = "..."

@fgpt
def your_function(*args, **kwargs):
    "Function docstring required"
    # Your code here
```

This will allow 
"""

__dev_version__ = "0.0.1"
__version__ = __dev_version__


