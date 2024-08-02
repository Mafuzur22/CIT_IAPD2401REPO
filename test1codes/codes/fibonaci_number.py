def fibonacci_sequence(n):
    
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    
    while len(fib_sequence) < n:
        
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence


print(fibonacci_sequence(10))
