# DP Algorithm (Minimum Subset Sum Difference)

## Idea

Find a subset whose sum is as close as possible to half of the total sum.

---

## Steps

1. Compute total sum `S`
2. Set target = `S // 2`
3. Create a DP array `dp` of size `target + 1`

   * `dp[i] = True` if subset sum `i` is achievable
4. Initialize:

   * `dp[0] = True`
5. For each element `num` in array:

   * Traverse `j` from `target` down to `num`
   * Update:

     * `dp[j] = dp[j] OR dp[j - num]`
6. Find the largest `s1 ≤ target` such that `dp[s1] == True`
7. Answer = `S - 2 * s1`

---

## Pseudocode

```id="dp_algo_file"
function minSubsetSumDifference(arr):
    S = sum(arr)
    target = S // 2

    dp = array of size (target + 1) filled with False
    dp[0] = True

    for num in arr:
        for j from target down to num:
            dp[j] = dp[j] OR dp[j - num]

    for s1 from target down to 0:
        if dp[s1] == True:
            return S - 2 * s1
```

---

## Complexity

* Time: **O(n × S)**
* Space: **O(S)**
