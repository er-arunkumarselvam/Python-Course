# Print 1-10 using the recursive function

def countdown(n):
    if n == 0:
        return 
    else: 
        countdown(n-1)
    print(n)

countdown(5)