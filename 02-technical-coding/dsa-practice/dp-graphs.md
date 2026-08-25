# DSA Practice: Dynamic Programming & Graphs

Core concepts and solutions for high-frequency placement questions on Dynamic Programming and Graph Algorithms.

---

## Pattern 1: Dynamic Programming (0/1 Knapsack Problem)

- **Problem**: Given weights and values of $N$ items, put these items in a knapsack of capacity $W$ to get maximum total value.
- **Time Complexity**: $O(N 	imes W)$
- **Space Complexity**: $O(W)$
- **Code Solution (Python)**:
```python
def knapsack(W, wt, val, n):
    dp = [0] * (W + 1)
    for i in range(n):
        for w in range(W, wt[i] - 1, -1):
            dp[w] = max(dp[w], val[i] + dp[w - wt[i]])
    return dp[W]
```

---

## Pattern 2: Graph Traversal (Breadth-First Search - BFS)

- **Problem**: Traverse a graph level-by-level starting from a source node using a Queue.
- **Time Complexity**: $O(V + E)$
- **Space Complexity**: $O(V)$
- **Code Solution (Python)**:
```python
from collections import deque

def bfs(graph, start_node):
    visited = set([start_node])
    queue = deque([start_node])
    traversal = []

    while queue:
        node = queue.popleft()
        traversal.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return traversal
```
