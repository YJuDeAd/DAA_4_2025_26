def digitSum(x):
    if x < 10:
        return x
    
    total_sum = 0
    while x > 0:
        total_sum += x % 10
        x //= 10
        
    return digitSum(total_sum)

def superDigit(n, k):
    initial_sum = 0

    for c in n:
        initial_sum += int(c)
        
    initial_sum *= k
    
    return digitSum(initial_sum)