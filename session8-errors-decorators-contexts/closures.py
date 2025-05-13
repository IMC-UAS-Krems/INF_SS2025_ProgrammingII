

# This creates and returns a function, that adds a specific constant value
def add_constant(value):
    """ This is the function we call later with an argument"""
    def wrapper(arg):
        return value + arg

    return wrapper


add_five = add_constant(5)
add_ten = add_constant(10)

print(add_five(2), add_ten(2))
print(add_five(10), add_ten(20))

# print("hello world")
# my_print = print
# my_print("hello from myprint")
# print("hello from original")

# def create_printer1():
# def printer1(arg):
#     print("[Printer1]", arg)
#
# def printer2(arg):
#     print("[Printer2]", arg)

#
# printer1 = create_printer1()

def create_printer(printername):
    def nested(arg, arg2):
        print(f"[{printername}] {arg} and {arg2}")

    return nested
# print("create_printer name:", create_printer.__name__)
#
# func_alias = create_printer
# print("func_alias name:", func_alias.__name__)

# print("is alias the same as the original?", func_alias == create_printer)


printer1 = create_printer("Printer1")
printer2 = create_printer("Printer2")

print(printer1.__name__)
print(printer2.__name__)

printer1("This is an output", "Print something else")
printer2("This is an output", "Print something else")

# printer1.__name__ = "MyPrinter1"
# printer2.__name__ = "MyPrinter2"
#
# print(printer1.__name__)
# print(printer2.__name__)


# print(printer1 == printer2)
# print(printer1 is printer2)
