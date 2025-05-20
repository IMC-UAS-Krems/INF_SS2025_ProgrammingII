

class Range():
    def __init__(self, start, end, step):
        self.n = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.n += self.step
        if self.n >= self.end:
            raise StopIteration
        return self.n



class RangeIterable():
    def __init__(self, start, end, step):
        self.n = start
        self.end = end
        self.step = step

    def __iter__(self):
        return RangeIterator(start=self.n, end=self.end, step=self.step)


class RangeIterator():
    def __init__(self, start, end, step):
        self.n = start
        self.end = end
        self.step = step

    def __next__(self):
        self.n += self.step
        if self.n >= self.end:
            raise StopIteration
        return self.n

range = RangeIterable(0, 10, 3)

rangeit = iter(range)
print("first", next(rangeit))
print("first", next(rangeit))
rangeit2 = iter(range)
print("second", next(rangeit2))
print("second", next(rangeit2))

# for c in range:
#     print("first", c)
#
# for c in range:
#     print("second", c)