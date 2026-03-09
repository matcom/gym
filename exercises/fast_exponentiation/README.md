# Fast Exponentiation

## Background
Calculating $a^n$ sequentially takes $O(n)$ multiplications. However, by using the property $a^n = (a^{n/2})^2$ for even $n$, and $a^n = a \cdot a^{n-1}$ for odd $n$, we can solve this using Divide and Conquer. This brings the time complexity down to $O(\log n)$, which is significantly faster for large powers.

## Task
Calculate $a^n$ using the fast exponentiation algorithm (Divide and Conquer).

## Specifications
- **Input:** Two integers `a` (base) and `n` (exponent, where $n \ge 0$).
- **Output:** The result of $a^n$.

## Constraints
- The function must be recursive.
- Do not use iterative loops.
- Do not use Python's built-in `**` operator or `pow()` function for the main calculation (you can use `*` for multiplication).

## Example
```python
>>> fast_exponentiation(2, 10)
1024
>>> fast_exponentiation(3, 3)
27
```

## Instructions
1. Implement the `fast_exponentiation` function.
2. Define the base case when $n = 0$.
3. Handle the recursive logic differently depending on whether $n$ is even or odd.
4. Validate your code with the provided tests.

[Solve Online](https://github.dev/matcom/gym/blob/main/exercises/fast_exponentiation/solution.py), | [Leer en Español](README.es.md)
