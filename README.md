# Rule Engine with AST


## Overview
This project implements a Rule Engine using an Abstract Syntax Tree (AST) to evaluate user eligibility based on dynamic rules. The system allows for rule creation, combination, modification, and evaluation against user data.

## Features
- **AST Structure**: A data structure for representing rules as an Abstract Syntax Tree.
- **API Endpoints**:
  - `create_rule(rule_string)`: Parses a rule string and constructs the corresponding AST.
  - `combine_rules(rules)`: Combines multiple ASTs into a single tree for complex rule evaluation.
  - `evaluate_rule(json_data)`: Evaluates the combined AST against user data to determine eligibility.
- **Input Validation**: Robust handling of invalid inputs with clear error messages.
- **Test Cases**: Comprehensive tests to verify the functionality and reliability of the rule engine.

## Data Structure
### Node Class
The `Node` class represents a node in the AST, supporting different types of operations and conditions.

```python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value  # The operator or condition
        self.left = left    # Left child node
        self.right = right   # Right child node
