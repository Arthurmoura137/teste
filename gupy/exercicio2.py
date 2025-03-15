def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence
def is_fibonacci_number(n):
    fib_sequence = fibonacci_sequence(n)
    return n in fib_sequence
number = 21
if is_fibonacci_number(number):
    print(f"{number} pertence à sequência de Fibonacci.")
else:
    print(f"{number} não pertence à sequência de Fibonacci.")