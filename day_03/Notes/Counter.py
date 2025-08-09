class Counter:
    def __init__(self, value=0):
        self.value = value

counter = Counter()

print(counter.value)

counter.value += 1
print(counter.value)