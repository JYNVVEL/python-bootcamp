from functools import cache
import time

start_time = time.time()

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

end_time = time.time()

print(fibonacci(100))
print(end_time - start_time)
