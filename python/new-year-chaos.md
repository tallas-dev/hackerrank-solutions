
[https://www.hackerrank.com/challenges/new-year-chaos/problem]

The "New Year Chaos" challenge on HackerRank involves determining the minimum number of bribes in a queue where each person can bribe at most two others to move forward. If a person has bribed more than two people, the situation is deemed "Too chaotic." The goal is to calculate how many bribes occurred to reach the current queue state.

### Solution Explanation

The solution involves iterating over the queue and checking how far each person has moved forward. If anyone has moved more than two places forward (i.e., bribed more than two people), the output should be "Too chaotic." Otherwise, you count the number of bribes by checking how many people with a higher number have been overtaken.

Here's the Python3 code for the solution:

```python
def minimumBribes(q):
    bribes = 0
    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1
                
    print(bribes)
```

### Explanation:
1. **Check for chaos:** For each person, calculate how far they've moved from their original position. If anyone has moved more than two places ahead, print "Too chaotic."
2. **Count bribes:** For each person, you only need to check the range between the highest position they could have come from (`q[i] - 2`) and their current position. This avoids unnecessary checks and improves performance.
3. **Complexity:** The time complexity of this solution is \(O(n^2)\), but it’s efficient enough given the constraints.

This approach ensures that the problem is solved efficiently without running into unnecessary iterations, making it suitable for typical inputs seen in competitive programming challenges. For more details on the problem, you can check it out on HackerRank【214†source】【215†source】.

