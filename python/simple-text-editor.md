
The "Simple Text Editor" problem on HackerRank is about simulating a basic text editor with four main operations. Here's the task in summary:
[https://www.hackerrank.com/challenges/simple-text-editor/problem]

1. **Append**: Add a string to the end of the existing text.
2. **Delete**: Remove the last `k` characters from the text.
3. **Print**: Print the character at a specific 1-based index in the current text.
4. **Undo**: Revert the text to its previous state before the last modification.

The problem requires you to maintain a history of operations so that you can efficiently undo any previous action.

### Solution in Python3

This solution ensures correct input handling based on the task's description:

```python
class SimpleTextEditor:
    def __init__(self):
        self.text = ""
        self.history = []

    def append(self, w):
        self.history.append(self.text)
        self.text += w

    def delete(self, k):
        self.history.append(self.text)
        self.text = self.text[:-k]

    def print_char(self, k):
        print(self.text[k - 1])

    def undo(self):
        if self.history:
            self.text = self.history.pop()

# Input Handling
if __name__ == "__main__":
    editor = SimpleTextEditor()
    q = int(input())

    for _ in range(q):
        query = input().split()
        command = query[0]

        if command == '1':
            editor.append(query[1])
        elif command == '2':
            editor.delete(int(query[1]))
        elif command == '3':
            editor.print_char(int(query[1]))
        elif command == '4':
            editor.undo()
```

### Explanation

1. **Class Structure**: We use a class to manage the text editor state and history of changes.
2. **History Stack**: Each modification (`append` or `delete`) pushes the previous state onto a stack to support undo operations.
3. **Input Handling**: The solution reads multiple queries and executes the appropriate operation based on the input command.

This implementation runs efficiently, with constant-time complexity for each operation, including undo, thanks to the stack structure.
