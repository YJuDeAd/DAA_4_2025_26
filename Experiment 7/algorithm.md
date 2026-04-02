## Algorithm (Bellman-Ford with Stop Constraint)

1. Initialize a distance array `dist` of size `n`:
   - Set all values to `∞`
   - Set `dist[src] = 0`

2. Repeat the following process **k + 1 times**:
   - Create a temporary copy `temp` of `dist`
   - For each flight `[u, v, price]`:
     - If `dist[u]` is not `∞`:
       - Update `temp[v] = min(temp[v], dist[u] + price)`
   - Replace `dist` with `temp`

3. After all iterations:
   - If `dist[dst]` is still `∞`, return `-1`
   - Otherwise, return `dist[dst]`

---

## Key Idea

- Each iteration allows paths with **one more edge**
- Running it **k + 1 times** ensures:
  - Only paths with **at most k stops** are considered
- Using a temporary array prevents using updated values in the same iteration

---

## Complexity Analysis

### Time Complexity
- Outer loop runs **k + 1 times**
- Inner loop processes all flights → `E` edges  

- Time complexity: O((k + 1) * E) ≈ O(kE)

---

### Space Complexity
- Distance array of size `n`
- Temporary array of size `n`

- Space Complexity: O(n)

---

## Important Note

- Do **not** update the `dist` array directly within the same iteration  
- Always use a temporary copy (`temp`) to enforce the stop constraint correctly
