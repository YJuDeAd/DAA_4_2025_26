'''
Master Theorem:
T(n) = Θ(n^1.5)
'''

import time

start_time = time.perf_counter()

count = 0
maxDepth = 0

def complexRec(n, depth):
    global maxDepth, count
    maxDepth = max(maxDepth, depth)

    if n <= 2:
        return

    p = n
    while p > 0:
        temp = [0] * n
        for i in range(n):
            temp[i] = i ^ p
            count += 1
        p >>= 1

    small = [0] * n
    for i in range(n):
        small[i] = i * i
        count += 1

    if n % 3 == 0:
        small.reverse()
    else:
        small.reverse()

    complexRec(n // 2, depth + 1)
    complexRec(n // 2, depth + 1)
    complexRec(n // 2, depth + 1)


if __name__ == "__main__":
    complexRec(16, 1)

    print(f"Operation: {count}")
    print(f"Depth: {maxDepth}")

    end_time = time.perf_counter()

    exection_time = (end_time - start_time) * 1000

    print(f"Exection Time: {exection_time:.4f} milliseconds")