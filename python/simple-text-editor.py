
# Enter your code here. Read input from STDIN. Print output to STDOUT
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

