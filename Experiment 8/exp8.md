# Experiment 8

## A. Experimental Procedure

### Step 1: Implementation

#### 1. Binary Search
Binary Search is an efficient searching algorithm that operates on a **sorted array**. It repeatedly divides the search interval in half:
- Compare the target with the middle element
- If equal → element found
- If smaller → search left half
- If larger → search right half

**Key Points:**
- Requires sorted input
- Time Complexity: **O(log n)**
- Handles edge cases like empty array, single element, and element not present

---

#### 2. Subset Sum Problem

##### (a) Decision Version
Determines whether there exists a subset of a given set whose sum equals a target value.

- Input: Set of integers and a target sum
- Output: **Yes/No**

##### (b) Verification Version
Given a subset, verify whether its sum equals the target.

- Input: A subset and target sum
- Output: Check if sum is correct

**Key Points:**
- Decision version is computationally hard
- Verification is straightforward and efficient
- Time Complexity (Decision): **O(2ⁿ)**
- Time Complexity (Verification): **O(n)**

---

#### 3. Traveling Salesman Problem (Brute Force)

The Traveling Salesman Problem (TSP) finds the shortest route that:
- Visits each city exactly once
- Returns to the starting city

**Brute Force Approach:**
- Generate all possible permutations of cities
- Calculate total distance for each route
- Select the minimum

**Key Points:**
- Guarantees optimal solution
- Time Complexity: **O(n!)**
- Becomes impractical for larger inputs

---

### Step 2: Measure Metrics

For each algorithm execution, the following metrics should be recorded:

- **Execution Time:** Time taken to complete execution
- **Approximate Number of Operations:** Based on theoretical complexity
- **Feasibility Status:**
  - Completed → Execution finished within acceptable time
  - Timeout → Execution exceeded time limits

**Structured Log Example:**

| Algorithm | Input Size (n) | Execution Time | Operations Estimate | Status |
|----------|---------------|----------------|---------------------|--------|
| Binary Search | 1000 | Very Low | log n | Completed |
| Subset Sum | 20 | High | 2ⁿ | Completed |
| TSP | 12 | Very High | n! | Timeout |

---

## B. Analysis Tasks

### 1. Why Binary Search is Efficient

Binary Search demonstrates consistent efficiency because it reduces the problem size by half at each step.

- Time Complexity: **O(log n)**
- Growth is very slow even for large inputs

**Explanation:**
For very large datasets, the number of operations remains small because each step eliminates half of the remaining elements.

---

### 2. Why Subset Sum is Hard to Solve but Easy to Verify

- **Solving:** Requires checking all possible subsets → **O(2ⁿ)** (exponential)
- **Verifying:** Simply add elements of a given subset → **O(n)** (linear)

**Conclusion:**
The difficulty lies in finding the correct subset, not in checking it.

---

### 3. When TSP Becomes Infeasible

TSP becomes infeasible typically around **n ≥ 12–15** (depending on system performance).

**Reason:**
- Time Complexity: **O(n!)**
- Factorial growth increases extremely rapidly

**Example Growth:**
- n = 10 → ~362,880 routes
- n = 15 → ~87 billion routes

Thus, brute force becomes impractical beyond small input sizes.

---

### 4. Difference Between Solving and Verifying

| Aspect | Solving | Verifying |
|------|--------|----------|
| Definition | Finding a solution | Checking correctness |
| Complexity | Often high | Usually low |
| Example (Subset Sum) | Find subset → hard | Check sum → easy |
| Example (TSP) | Find shortest route → hard | Check route length → easy |

---

### 5. Why NP-Complete Problems are Most Challenging

NP-Complete problems are the hardest problems in NP because:

- They can be verified in polynomial time
- Every NP problem can be reduced to them

**Implications:**
- If one NP-Complete problem is solved efficiently, all NP problems can be solved efficiently

**Examples:**
- Subset Sum
- Traveling Salesman Problem
- Boolean Satisfiability (SAT)

**Conclusion:**
They represent the most computationally difficult problems known in theoretical computer science.

---

## Final Conclusion

- Binary Search is efficient due to logarithmic complexity
- Subset Sum highlights the gap between solving and verifying
- TSP demonstrates rapid growth in computational difficulty
- NP-Complete problems define the limits of efficient computation
