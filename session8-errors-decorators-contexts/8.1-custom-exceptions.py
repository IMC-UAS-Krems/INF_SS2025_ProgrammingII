user_input = input("Enter grades separated by comma: ")
grades = user_input.split(", ")

print("grades", grades)

class InvalidGradeError(Exception):
    """Custom exception for invalid grades."""
    pass

try:
    total = 0
    for i in range(len(grades)):
        total += int(grades[i])
        if int(grades[i]) < 0 or int(grades[i]) > 100:
            raise InvalidGradeError()
    average_grade = total / len(grades)
    print(f"Average grade: {average_grade}")

except InvalidGradeError as e:
    print("Invalid grade entered. Please enter grades between 0 and 100.")

except ValueError as e:
    print("Could not convert (at least) one value to an int.", grades)

except ZeroDivisionError:
    print("No grades were entered.")


