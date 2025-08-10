import time

start = time.time()

for _ in range(1_000_000):
    x = 10 ** 1000

end = time.time()

print("Execution Time: ", end - start)