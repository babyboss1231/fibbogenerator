# fibbogenerator
#This program generates the first n Fibonacci numbers. You can change the value of n to get as many numbers as you'd like.
def fibonacci_series(n):
    fib_sequence = []
    a, b = 0, 1
    for i in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

#n = int(input("Enter the number of terms: "))
#print(fibonacci_series(n))
