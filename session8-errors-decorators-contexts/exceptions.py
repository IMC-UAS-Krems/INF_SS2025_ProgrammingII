# import NetworkError from ...
import sys
import traceback

try:
    print(1 / 1)
    # some more code
    # ...
    # conctact spotify servers
    # ...
    raise TypeError("Some more information")
except ZeroDivisionError as exc:
    # print(ex, type(ex))
    # ex_type, ex, tb = sys.exc_info()
    # traceback.print_tb(tb)
    print("Cannot divide by zero")
# except NetworkError:
#     print("Couldn't contact Spotify")
except TypeError as exc:
    print(exc)
    print("The datatype that Spotify returned is weird")

except Exception:
    print("General Exception")
