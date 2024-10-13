
[https://www.hackerrank.com/challenges/queue-using-two-stacks/problem]

The problem **"Queue using Two Stacks"** on HackerRank asks you to implement a queue using two stacks and handle multiple queries efficiently.

Here is a Python solution based on the input format and problem constraints:

### Problem Explanation:
You need to implement a queue where:
1. **1 x**: Enqueue element `x` into the queue.
2. **2**: Dequeue the element at the front of the queue.
3. **3**: Print the element at the front of the queue.

You must simulate these operations using two stacks, ensuring the queue's first-in-first-out (FIFO) behavior.

### Python Solution:
```python
class QueueUsingTwoStacks:
    def __init__(self):
        self.new_stack = []  # Stack used for enqueue operations
        self.old_stack = []  # Stack used for dequeue and peek operations

    def enqueue(self, value):
        # Push value onto the new stack
        self.new_stack.append(value)

    def dequeue(self):
        # Transfer elements to old_stack if it's empty
        if not self.old_stack:
            while self.new_stack:
                self.old_stack.append(self.new_stack.pop())
        # Remove the element from the front of the queue
        if self.old_stack:
            self.old_stack.pop()

    def peek(self):
        # Transfer elements to old_stack if it's empty
        if not self.old_stack:
            while self.new_stack:
                self.old_stack.append(self.new_stack.pop())
        # Return the front of the queue
        if self.old_stack:
            return self.old_stack[-1]

# Input handling
if __name__ == "__main__":
    q = QueueUsingTwoStacks()
    queries = int(input())
    
    for _ in range(queries):
        operation = list(map(int, input().split()))
        if operation[0] == 1:
            q.enqueue(operation[1])
        elif operation[0] == 2:
            q.dequeue()
        elif operation[0] == 3:
            print(q.peek())
```

### Explanation:
- **Two Stacks Approach**: 
  - Stack `new_stack` is used to push incoming elements during enqueue operations.
  - Stack `old_stack` is used for dequeue and peek operations. When dequeuing or peeking, we transfer elements from `new_stack` to `old_stack` to reverse their order, maintaining the queue's FIFO property.
  
- **Operations**:
  - **Enqueue (1 x)**: Simply append to `new_stack`.
  - **Dequeue (2)**: Transfer elements from `new_stack` to `old_stack` only when `old_stack` is empty, then pop the top of `old_stack`.
  - **Peek (3)**: Ensure `old_stack` has elements and return the top element.

### Time Complexity:
- Enqueue: O(1)
- Dequeue and Peek: Amortized O(1) due to the transfer between stacks happening only when needed.

This approach optimizes the queue operations while using only two stacks, providing a more efficient solution than direct simulation with lists【247†source】【246†source】.

