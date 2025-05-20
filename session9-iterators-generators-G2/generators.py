def mygen(param):
    yield param+"C"
    yield param+"G"
    yield param+"A"
    yield param+"T"

gen = mygen("hi")
gen2 = mygen("no")
# print("Gen1", next(gen))
# print("Gen1", next(gen))
# print("Gen1", next(gen))
# print("Gen2", next(gen2))
# print("Gen2", next(gen2))
for c in gen:
    pass
    # print(c)

gen = mygen("")
# print(list(gen))


def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

gen = fibonacci()
for i in range(10):
    pass
    # print(next(gen))


def myrange(start, stop, step):
    current = start
    while current < stop:
        yield current
        current += step

# for c in myrange(0,15,3):
#     print(c)

def myrange_rec(start, stop, step):
    if start > stop:
        return
    yield start

    # this does not work. It yields the generator itself, not its values
    # gen = myrange_rec(start+step, stop, step)
    # yield gen

    # this does work. it iteratively yields the generator's values
    gen = myrange_rec(start+step, stop, step)
    while True:
         yield next(gen)

    # yield from myrange_rec(start+step, stop, step)


gen = myrange_rec(0,15,3)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


