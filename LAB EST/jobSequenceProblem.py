def job_scheduling(deadline, profit):
    n = len(deadline)
    jobs = list(zip(deadline, profit))
    jobs.sort(key=lambda x: x[1], reverse=True)
    max_deadline = max(deadline) if deadline else 0
    slots = [False] * max_deadline

    count = 0
    max_profit = 0

    for i in range(n):
        job_deadline = jobs[i][0]
        job_profit = jobs[i][1]

        for j in range(min(max_deadline, job_deadline) - 1, -1, -1):
            if not slots[j]:
                slots[j] = True
                count += 1
                max_profit += job_profit
                break

    return [count, max_profit]

deadline = [4, 1, 1, 1]
profit = [20, 10, 40, 30]

print(job_scheduling(deadline, profit))
