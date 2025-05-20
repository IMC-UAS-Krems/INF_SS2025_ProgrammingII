def mygen():
    yield "C"
    yield "G"
    yield "A"
    yield "T"

gen = mygen()
gen2 = mygen()
print("Gen", next(gen))
print("Gen", next(gen))
print("Gen2", next(gen2))
print("Gen2", next(gen2))


for c in gen:
    print(c)

# print(next(gen))

print("\n" * 3, "myrange generator")

def myrange(start, stop, step):
    current = start
    while current < stop:
        yield current
        current += step

for c in myrange(0,15,3):
    print (c)

# List comprehension... unroll all elements in the generator
print( [i for i in myrange(0,15,3)])
# Generator expression. Does not unroll... ("lazy evaluation")
print( i for i in myrange(0,15,3))

print( list(i for i in myrange(0,15,3)))




""" Implementing myrange using recursion"""
def myrange(start, stop, step):
    if start >= stop:
        return
    yield (start)

    for i in myrange(start + step, stop, step)
        yield i
    # this is equivalent to the above
    yield from myrange(start + step, stop, step)