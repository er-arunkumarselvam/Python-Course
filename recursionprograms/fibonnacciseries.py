# Fibonacci Sequence
# Fibonacci Sequence = (n-1) + (n-2)
# 0, 1, 1, 2, 3, 5, 8, ...

def fibo(n):
    if n <=1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

n=10

if n <= 0:
  print("Invalid input ! Please input a positive value")
else:
  print("Fibonacci series:")
for i in range(n):
    print(fibo(i))