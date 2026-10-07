import datetime
import math
import random
import time
import uuid

from utility_package import file_utils
from utility_package import math_utils

DIVIDER = "==========================="


def datetime_menu():
    print("Datetime and Time Operations:")
    print("1. Display current date and time")
    print("2. Calculate difference between two dates/times")
    print("3. Format date into custom format")
    print("4. Stopwatch")
    print("5. Countdown Timer")
    print("6. Back to Main Menu")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            print()
            now = datetime.datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            print(f"Current Date and Time: {current_time}")
            print(DIVIDER)

        elif choice == "2":
            print()
            try:
                first_date = input("Enter the first date (YYYY-MM-DD): ")
                second_date = input("Enter the second date (YYYY-MM-DD): ")

                first = datetime.date.fromisoformat(first_date)
                second = datetime.date.fromisoformat(second_date)

                days = abs((second - first).days)
                print(f"Difference: {days} days")
            except ValueError:
                print("Invalid date format!")
            print(DIVIDER)

        elif choice == "3":
            print()
            try:
                date_text = input("Enter date and time (YYYY-MM-DD HH:MM): ")
                date_value = datetime.datetime.strptime(
                    date_text, "%Y-%m-%d %H:%M"
                )

                print("\nExamples:")
                print("%d-%m-%Y")
                print("%B %d, %Y")
                print("%d %B %Y")

                format_text = input("Enter your desired format: ")
                formatted = date_value.strftime(format_text)

                print(f"Formatted Date: {formatted}")
            except ValueError:
                print("Invalid date!")
            print(DIVIDER)

        elif choice == "4":
            print("\nStopwatch")
            input("Press Enter to START...")

            start_time = time.perf_counter()

            input("Press Enter to STOP...")

            stop_time = time.perf_counter()
            elapsed = round(stop_time - start_time, 2)

            print(f"Elapsed Time: {elapsed} seconds")
            print(DIVIDER)

        elif choice == "5":
            print()
            try:
                count = int(input("Enter countdown time in seconds: "))

                while count > 0:
                    print(f"Time Remaining: {count} seconds")
                    time.sleep(1)
                    count -= 1

                print("Time's up!")
            except ValueError:
                print("Please enter a valid number.")
            print(DIVIDER)

        elif choice == "6":
            break

        else:
            print("Invalid choice!")
            print(DIVIDER)


def math_menu():
    print("Mathematical Operations:")
    print("1. Calculate Factorial")
    print("2. Solve Compound Interest")
    print("3. Trigonometric Calculations")
    print("4. Area of Geometric Shapes")
    print("5. Back to Main Menu")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            print()
            try:
                number = int(input("Enter a number: "))
                factorial = math_utils.factorial(number)
                print(f"Factorial: {factorial}")
            except ValueError as error:
                print(error)
            print(DIVIDER)

        elif choice == "2":
            print()
            try:
                principal = float(input("Enter principal amount: "))
                rate = float(input("Enter rate of interest (in %): "))
                years = float(input("Enter time (in years): "))

                result = math_utils.compound_interest(
                    principal, rate, years
                )
                print(f"Compound Interest: {result:.2f}")
            except ValueError:
                print("Invalid input!")
            print(DIVIDER)

        elif choice == "3":
            print()
            try:
                angle = float(input("Enter angle in degrees: "))
                angle_radians = math.radians(angle)

                sine = round(math.sin(angle_radians), 4)
                cosine = round(math.cos(angle_radians), 4)
                tangent = round(math.tan(angle_radians), 4)

                print("sin:", sine)
                print("cos:", cosine)
                print("tan:", tangent)
            except ValueError:
                print("Invalid angle!")
            print(DIVIDER)

        elif choice == "4":
            print("\nGeometric Shapes")
            print("1. Circle")
            print("2. Rectangle")
            print("3. Triangle")

            shape_choice = input("Enter your choice: ")

            try:
                if shape_choice == "1":
                    radius = float(input("Enter radius: "))
                    area = math_utils.circle_area(radius)
                    print(f"Area of Circle: {area}")

                elif shape_choice == "2":
                    length = float(input("Enter length: "))
                    width = float(input("Enter width: "))
                    area = math_utils.rectangle_area(length, width)
                    print(f"Area of Rectangle: {area}")

                elif shape_choice == "3":
                    base = float(input("Enter base: "))
                    height = float(input("Enter height: "))
                    area = math_utils.triangle_area(base, height)
                    print(f"Area of Triangle: {area}")

                else:
                    print("Invalid choice!")

            except ValueError:
                print("Invalid input!")

            print(DIVIDER)

        elif choice == "5":
            break

        else:
            print("Invalid choice!")
            print(DIVIDER)


def random_menu():
    print("Random Data Generation:")
    print("1. Generate Random Number")
    print("2. Generate Random List")
    print("3. Create Random Password")
    print("4. Generate Random OTP")
    print("5. Back to Main Menu")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            print()
            try:
                minimum = int(input("Enter minimum value: "))
                maximum = int(input("Enter maximum value: "))

                random_number = random.randint(minimum, maximum)
                print(f"Random Number: {random_number}")
            except ValueError:
                print("Invalid input!")

            print(DIVIDER)

        elif choice == "2":
            print()
            try:
                size = int(input("Enter list size: "))
                minimum = int(input("Enter minimum value: "))
                maximum = int(input("Enter maximum value: "))

                if size < 0:
                    raise ValueError("List size cannot be negative.")

                numbers = []

                for i in range(size):
                    numbers.append(random.randint(minimum, maximum))

                print("Random List:")
                print(numbers)

            except ValueError as error:
                print(f"Invalid input: {error}")

            print(DIVIDER)

        elif choice == "3":
            print()
            try:
                password_length = int(input("Enter password length: "))
                password = math_utils.generate_password(password_length)

                print(f"Generated Password: {password}")
            except ValueError as error:
                print(error)

            print(DIVIDER)

        elif choice == "4":
            print()
            try:
                otp_length = int(input("Enter OTP length: "))

                if otp_length < 4 or otp_length > 10:
                    print("OTP length must be between 4 and 10.")
                else:
                    otp = ""

                    for i in range(otp_length):
                        otp += str(random.randint(0, 9))

                    print(f"Generated OTP: {otp}")

            except ValueError:
                print("Invalid input!")

            print(DIVIDER)

        elif choice == "5":
            break

        else:
            print("Invalid choice!")
            print(DIVIDER)


def uuid_menu():
    print("Generate Unique Identifiers:")
    print("1. Generate UUID4")
    print("2. Generate Multiple UUIDs")
    print("3. Back to Main Menu")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            print()
            new_uuid = uuid.uuid4()
            print(f"Generated UUID: {new_uuid}")
            print(DIVIDER)

        elif choice == "2":
            print()
            try:
                total = int(input("How many UUIDs? "))

                if total < 1:
                    print("Enter a positive number.")
                else:
                    for i in range(total):
                        print(uuid.uuid4())

            except ValueError:
                print("Invalid number!")

            print(DIVIDER)

        elif choice == "3":
            break

        else:
            print("Invalid choice!")
            print(DIVIDER)


def file_menu():
    print("File Operations:")
    print("1. Create a new file")
    print("2. Write to a file")
    print("3. Read from a file")
    print("4. Append to a file")
    print("5. Back to Main Menu")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            print()
            filename = input("Enter file name: ")

            try:
                file_utils.create_file(filename)
                print("File created successfully!")
            except Exception as error:
                print("Error:", error)

            print(DIVIDER)

        elif choice == "2":
            print()
            filename = input("Enter file name: ")
            data = input("Enter data to write: ")

            try:
                file_utils.write_file(filename, data)
                print("Data written successfully!")
            except Exception as error:
                print("Error:", error)

            print(DIVIDER)

        elif choice == "3":
            print()
            filename = input("Enter file name: ")

            try:
                content = file_utils.read_file(filename)
                print("File Content:")
                print(content)
            except Exception as error:
                print("Error:", error)

            print(DIVIDER)

        elif choice == "4":
            print()
            filename = input("Enter file name: ")
            data = input("Enter data to append: ")

            try:
                file_utils.append_file(filename, data)
                print("Data appended successfully!")
            except Exception as error:
                print("Error:", error)

            print(DIVIDER)

        elif choice == "5":
            break

        else:
            print("Invalid choice!")
            print(DIVIDER)


def explore_module():
    print("Explore Module Attributes:")

    module_name = input("Enter module name to explore: ")

    modules = {
        "math": math,
        "random": random,
        "datetime": datetime,
        "time": time,
        "uuid": uuid,
        "math_utils": math_utils,
        "file_utils": file_utils
    }

    if module_name in modules:
        selected_module = modules[module_name]
        module_attributes = dir(selected_module)

        print(f"Available Attributes in {module_name} module:")
        print(module_attributes)
    else:
        print("Module not available!")

    print(DIVIDER)


def main():
    while True:
        print(DIVIDER)
        print("Welcome to Multi-Utility Toolkit")
        print(DIVIDER)

        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        print(DIVIDER)

        choice = input("Enter your choice: ")

        if choice == "1":
            print()
            datetime_menu()

        elif choice == "2":
            print()
            math_menu()

        elif choice == "3":
            print()
            random_menu()

        elif choice == "4":
            print()
            uuid_menu()

        elif choice == "5":
            print()
            file_menu()

        elif choice == "6":
            print()
            explore_module()

        elif choice == "7":
            print()
            print(DIVIDER)
            print("Thank you for using the Multi-Utility Toolkit!")
            print(DIVIDER)
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()