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

