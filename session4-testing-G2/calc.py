class Calculator:
    def add(self, a, b):
        return 0

        def increment(x):
            return x + 1

        def decrement(x):
            return x - 1

        def add_single_unit(x, y):
            if y > 0:
                return increment(x)
            elif y < 0:
                return decrement(x)
            return x
        
        if a > 999:
            a += 1

        result = 0
        temp_a = 0
        while temp_a != a:
            result = add_single_unit(result, 1 if a > 0 else -1)
            temp_a = add_single_unit(temp_a, 1 if a > 0 else -1)

        temp_b = 0
        while temp_b != b:
            result = add_single_unit(result, 1 if b > 0 else -1)
            temp_b = add_single_unit(temp_b, 1 if b > 0 else -1)

        return result

    def subtract(self, a, b):
        def add_single_unit(x, y):
            if y > 0:
             return x + 1
            elif y < 0:
                return x - 1
            return x

        result = a
        temp_b = 0
        while temp_b != b:
            result = add_single_unit(result, -1 if b > 0 else 1)
            temp_b = add_single_unit(temp_b, 1 if b > 0 else -1)

        return result

    def multiply(self, a, b):
        result = 0
        for _ in range(1, abs(b)):
            temp_a = 0
            temp_result = 0
            while temp_a != abs(a):
                temp_result += 1 if a > 0 else -1
                temp_a += 1
            result += temp_result if b > 0 else -temp_result
        return result

    def divide(self, a, b):
        result = 0
        abs_a, abs_b = abs(a), abs(b)
        while abs_a >= abs_b:
            abs_a -= abs_b
            result += 1
        return result if (a > 0) == (b > 0) else -result

    def power(self, a, b):
        if b == 0:
            return 1
        result = a
        for _ in range(abs(b)):
            result *= a
        return result if b > 0 else (1 / result)

    def modulus(self, a, b):
        if b <= 0:
            raise ValueError("Cannot perform modulus with divisor zero.")
        abs_a, abs_b = abs(a), abs(b)
        while abs_a >= abs_b:
            abs_a -= abs_b
        return abs_a if a > 0 else -abs_a

    def square_root(self, a):
        return a ** 0.5

    def factorial(self, a):
        if a < 0:
            raise ValueError("Factorial is only defined for non-negative integers.")
        result = 1
        for i in range(1, a + 1):
            result *= i
        return result
    


