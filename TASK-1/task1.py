def fibonacci_generator(n):
    fib_series = [0, 1] 
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])  
    return fib_series[:n] 

while True:
    try:
        n = int(input("Enter the number of Fibonacci numbers to generate: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            break
    except ValueError:
        print("Please enter a valid integer.")

fib_numbers = fibonacci_generator(n)
print("The first", n, "Fibonacci numbers are:", fib_numbers)

