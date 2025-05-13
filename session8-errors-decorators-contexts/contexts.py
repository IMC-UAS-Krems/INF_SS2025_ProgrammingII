# fh = None
# file_open = False
# try:
#     fh = open('test.txt', 'w')
#     file_open = True
#     data = fh.read()
# except IOError:
#     print('IOError')
# finally:
#     if file_open and fh:
#         fh.close()



class this_file_reader():
    # def __init__(self, filename = None):
    #     if filename == None:
    #         self.filename = __file__
    #     else:
    #         self.filename = filename
    #     self.numlines = None

    def __enter__(self):
        self.filehandle = open(__file__, "r")
        return self.filehandle

    def __exit__(self, exception, value, trace):
        if exception is not None:
            if isinstance(exception, MyDBException):
                print("Couldn't connect to database")
                return True
            else:
                # something bad happened...
                print("bad stuff, error correction...")
                return False

        print("exiting context")
        self.filehandle.close()
        return True  # this is to suppress the exception raising
    #
    # def read(self):
    #     print("we will now read from the file")
    #     data = self.filehandle.read()
    #     self.numlines = len(data.splitlines())
    #     return data


with this_file_reader() as fm:
    print(fm)
    print(fm.read())

print("Code after context manager")

ex = None
value = None
trace = None

ctx = this_file_reader()
fm = ctx.__enter__()
try:
    print(fm)
    raise Exception("Mean Person raises")
    print(fm.read())
except Exception as e:
    ex = e
    value = get_value(e)   # not sure how value is actually caluclated internally
    trace = e.__traceback__
finally:
    ret_val = fm.__exit__(ex, value, trace)
    if ex is not None and ret_val is False:
        raise ex