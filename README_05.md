# Python Fundamentals

Practice exercises written by hand, no AI.

## Error log

### 01_greeting.py
- Error: The program crashed with a `ValueError` when the user typed letters instead of numbers for the age.
- Cause: The `int()` function cannot convert text into an integer, and there is no validation to handle non-numeric input.

### 05_guess.py
- Error: The `else` block was dead code because the `while` loop condition prevented it from ever running.
- Cause: The logic of the loop already handled the exit condition, making the `else` redundant.