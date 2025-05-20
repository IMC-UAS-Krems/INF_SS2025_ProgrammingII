class Range():
    def __init__(self, start, stop, step=1):
        self.n = start
        self.stop = stop
        self.step = step

    def __next__(self):
        self.n += self.step
        if self.n >= self.stop:
            raise StopIteration
        return self.n

    def __iter__(self):
        return self

# for c in Range(0, 10, 3):
#     print(c)

r = Range(0, 10, 3)
ir = iter(r)
print("[IR]", next(ir))
print("[IR]", next(ir))

ir2 = iter(r)
print("[IR2]", next(ir2))


class RangeIterable():
    def __init__(self, start, stop, step=1):
        self.n = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return RangeIterator(self.n, self.stop, self.step)

class RangeIterator():
    def __init__(self, start, stop, step=1):
        self.n = start
        self.stop = stop
        self.step = step

    def __next__(self):
        self.n += self.step
        if self.n >= self.stop:
            raise StopIteration
        return self.n


r = RangeIterable(0, 10, 3)
ir = iter(r)
print("[Split-IR]", next(ir))
print("[Split-IR]", next(ir))

ir2 = iter(r)
print("[Split-IR2]", next(ir2))

