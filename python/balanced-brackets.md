
The "Balanced Brackets" problem on HackerRank is a task where you are given multiple strings containing different types of brackets: `()`, `{}`, and `[]`. Your goal is to determine whether each string of brackets is balanced.

A string of brackets is considered balanced if:
1. Every opening bracket has a corresponding closing bracket of the same type.
2. Brackets are closed in the correct order (i.e., a closing bracket only closes the most recent unmatched opening bracket of the same type).

### Example:
- Input:
  ```
  3
  {[()]}
  {[(])}
  {{[[(())]]}}
  ```
- Output:
  ```
  YES
  NO
  YES
  ```

### Explanation:
1. The string `{[()]}` is balanced, so the output is "YES".
2. The string `{[(])}` is not balanced, as the brackets are mismatched, so the output is "NO".
3. The string `{{[[(())]]}}` is balanced, so the output is "YES".

### Solution in Python:
Here's a Python solution using a stack to check for balanced brackets:

```python
def isBalanced(s):
    stack = []
    pairs = {"{": "}", "[": "]", "(": ")"}

    for char in s:
        if char in pairs:  # opening brackets
            stack.append(char)
        elif stack and char == pairs[stack[-1]]:  # closing brackets with matching pair
            stack.pop()
        else:
            return "NO"  # unmatched closing bracket

    return "YES" if not stack else "NO"

# Input handling
n = int(input())  # number of strings
for _ in range(n):
    s = input()
    print(isBalanced(s))
```

### How it works:
- A stack is used to keep track of opening brackets.
- For each character in the string:
  - If it's an opening bracket, it's pushed onto the stack.
  - If it's a closing bracket, the top of the stack is checked for a matching opening bracket.
  - If there's a mismatch or unbalanced bracket, the function returns "NO".
- If the stack is empty after processing the string, it means the string is balanced, and we return "YES".

This solution runs in O(n) time for each string, where n is the length of the string.
