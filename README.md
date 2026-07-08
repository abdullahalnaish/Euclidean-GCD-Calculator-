# Euclidean-GCD-Calculator-
A lightweight Python lab application that implements the algorithm to calculate the greatest common divisor. It features iterative implementation.

# Euclidean GCD Calculator Lab

## Lab Objectives
- Understand the mathematical concepts of the Euclidean algorithm
- Implement iterative and recursive approaches in Python
- Verify code correctness using automated Unit Tests

## Prerequisites
- Python 3.x installed

## Project Structure
- gcd_calculator.py: Core functions
- test_gcd.py: Automation suite
- README.md: Lab documentation

## Implementation Tasks

### Task 1 Implementation
Open gcd_calculator.py and complete the functions.

Iterative Version:
```python
def gcd_iterative(a, b):
    while b != 0:
        a, b = b, a % b
    return a
