# Dry Run (DP Approach)

## Input

```text id="dp_dry_input"
arr = [1, 6, 11, 5]
```

---

## Step 1: Compute total sum

```text id="dp_dry_sum"
S = 23
target = 11
```

---

## Step 2: Initialize DP

```text id="dp_dry_init"
dp = [True, False, False, False, False, False, False, False, False, False, False, False]
index: 0     1      2      3      4      5      6      7      8      9      10     11
```

---

## Step 3: Process elements

### Using num = 1

```text id="dp_dry_1"
dp[1] = True
```

```text id="dp_dry_1_state"
dp = [T, T, F, F, F, F, F, F, F, F, F, F]
```

---

### Using num = 6

```text id="dp_dry_6"
dp[6] = True
dp[7] = True
```

```text id="dp_dry_6_state"
dp = [T, T, F, F, F, F, T, T, F, F, F, F]
```

---

### Using num = 11

```text id="dp_dry_11"
dp[11] = True
```

```text id="dp_dry_11_state"
dp = [T, T, F, F, F, F, T, T, F, F, F, T]
```

---

### Using num = 5

```text id="dp_dry_5"
dp[5] = True
dp[6] = True
dp[10] = True
dp[11] = True
```

```text id="dp_dry_5_state"
dp = [T, T, F, F, F, T, T, T, F, F, T, T]
```

---

## Step 4: Find closest sum

```text id="dp_dry_pick"
s1 = 11 (since dp[11] = True)
```

---

## Step 5: Final answer

```text id="dp_dry_ans"
difference = 23 - 2 × 11 = 1
```

---

## Result

```text id="dp_dry_result"
Minimum difference = 1
```
