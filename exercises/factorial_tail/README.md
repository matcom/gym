# Tail Recursive Factorial

## Background
Factorial computations are a classic way to demonstrate recursion. However, standard recursion can lead to a stack overflow for large numbers. Tail recursion solves this by passing an accumulator (the state) in the recursive call, allowing compilers/interpreters to optimize the stack (though Python doesn't do this natively, it's still an important algorithmic pattern).

## Task
Calculate the factorial of $n$ ($n!$) using a tail-recursive function.

## Specifications
- **Input:** An integer `n`.
- **Output:** The factorial of `n`.

## Constraints
- The function must be recursive.
- The recursive call must be the very last operation in the function (tail recursion).
- Do not use iterative loops like `for` or `while`.
- You must use an accumulator argument.

## Example
```python
>>> factorial_tail(5)
120
>>> factorial_tail(0)
1
```

## Instructions
1. Implement the `factorial_tail` function using the tail-recursion paradigm.
2. Initialize the accumulator appropriately.
3. Validate your code with the provided tests.

[Solve Online](https://github.dev/matcom/gym/blob/main/exercises/factorial_tail/solution.py), | [Leer en Español](README.es.md)
