
class FibSequence():
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.a = 1  # first value
        self.b = 1  # second value

    def __next__(self):
        x = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        if self.count >= self.n:
            raise StopIteration
        return x

    def __iter__(self):
        return self


fib = FibSequence(10)
print (next (fib) )
print (next (fib) )
print (next (fib) )


for c in FibSequence(10):
    print (c)

