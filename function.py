def function_name(parameters):
    """
    Optional docstring to describe the function's purpose.
    """
    # Function body (indented code block)
    # Perform operations
    return value # Optional: returns a value to the caller

# def: This reserved keyword indicates the start of a function definition.
# function_name: A unique name (using snake_case is a common convention) that allows you to identify and call the function later.
# parameters: These are placeholders for input values the function can accept when called. They are enclosed in parentheses and separated by commas, and are optional.
# :: A colon marks the end of the function header and the beginning of the function body.
# Indentation: The code within the function must be indented (usually four spaces or a tab) to tell Python it belongs to the function's body.
# return: The return statement is used to send a value back to the part of the program that called the function. If omitted, the function automatically returns None. 

# Calling a Function
# Calling a function tells Python to run the code that was defined within it. A function must be defined before it can be called. 
# To call a function, use its name followed by parentheses. If the function expects arguments, provide them inside the parentheses, matching the order of the parameters in the definition. 



def greet():
    print("Hello, World!")

# Calling the function
greet() 
# Output: Hello, World!

def add_numbers(a, b):
    """Adds two numbers and returns the sum."""
    result = a + b
    return result

# Calling the function and storing the result
sum_result = add_numbers(5, 3)

# Printing the result
print(f"The sum is: {sum_result}") 
# Output: The sum is: 8

# Calling the function with different arguments
another_sum = add_numbers(10, 20)
print(f"Another sum is: {another_sum}")
# Output: Another sum is: 30


# - Variable scope (local, global)
# In Python, variable scope determines where in a program a variable is accessible. The two primary types of variable scope are local and global.
# Local Variables:
# A variable defined inside a function is a local variable.
# Local variables are only accessible within the function where they are defined.
# They cease to exist once the function execution completes.
# If a local variable has the same name as a global variable, the local variable takes precedence within the function, effectively "shadowing" the global variable in that specific scope. 

def my_function():
    local_var = "I am local"
    print(local_var)

# Attempting to access local_var outside the function will result in an error
# print(local_var)  # This would raise a NameError




# # Global Variables:
# A variable defined outside of any function, at the module level, is a global variable.
# Global variables are accessible from anywhere in the program, including inside functions.
# To modify a global variable from within a function, the global keyword must be used to explicitly indicate that the variable being referenced is the global one, not a new local variable with the same name.


global_var = "I am global"

def another_function():
    print(global_var)  # Accessing the global variable

def modify_global():
    global global_var  # Declare intent to modify the global variable
    global_var = "I am a modified global variable"

print(global_var)
print(global_var)
another_function()
modify_global()
print(global_var)
print(global_var)
print(global_var)
print(global_var)


# try:
    # Code that might raise an exception
    # For example: file operations, network requests,
    # or operations that could lead to runtime errors (like division by zero)
# except ExceptionType as e:
    # Code to handle the specific exception (ExceptionType)
    # This block executes if an exception of type ExceptionType occurs in the try block
    # 'e' is an optional variable that holds the exception object
# else:
    # (Optional) Code to execute if no exception occurs in the try block
# finally:
    # (Optional) Code that will always execute, regardless of whether
    # an exception occurred or not.
    # This is often used for cleanup operations, like closing files


try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(f"The result of division is: {result}")
except ValueError:
    print("Error: Invalid input. Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("Division successful, no exceptions occurred.")
finally:
    print("Execution of the try-except block is complete.")









# Exercise
# Write a function that calculates the area of a rectangle.

def rectangle_area(length, width):
    """Calculate and return the area of a rectangle."""
    return length * width

# Example usage
try:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = rectangle_area(length, width)
    print(f"The area of the rectangle is {area}")
except ValueError:
    print("Please enter valid numbers for length and width.")



# Create a simple calculator that uses try/except to catch input or division errors

# def simple_calculator():
#     """A simple calculator that performs +, -, *, / operations with error handling."""
#     try:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#         operator = input("Enter an operator (+, -, *, /): ")

#         if operator == '+':
#             result = num1 + num2
#         elif operator == '-':
#             result = num1 - num2
#         elif operator == '*':
#             result = num1 * num2
#         elif operator == '/':
#             result = num1 / num2  # May raise ZeroDivisionError
#         else:
#             print("Invalid operator.")
#             return

#         print(f"The result is: {result}")

#     except ValueError:
#         print("Error: Please enter valid numbers.")
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allowed.")

# # Example usage
# simple_calculator()




def simple_calculator():
    """A looping simple calculator with error handling and quit option."""
    print("=== Simple Calculator ===")
    print("Type 'q' or 'quit' at any time to exit.\n")

    while True:
        try:
            # Get first number
            num1_input = input("Enter first number: ")
            if num1_input.lower() in ['q', 'quit']:
                print("Exiting calculator... Goodbye!")
                break
            num1 = float(num1_input)

            # Get operator
            operator = input("Enter operator (+, -, *, /): ")
            if operator.lower() in ['q', 'quit']:
                print("Exiting calculator... Goodbye!")
                break

            # Get second number
            num2_input = input("Enter second number: ")
            if num2_input.lower() in ['q', 'quit']:
                print("Exiting calculator... Goodbye!")
                break
            num2 = float(num2_input)

            # Perform calculation
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2  # May raise ZeroDivisionError
            else:
                print("Invalid operator! Please use +, -, *, or /.")
                continue

            print(f"Result: {result}\n")

        except ValueError:
            print("Error: Please enter valid numbers.\n")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.\n")

# Run the calculator
simple_calculator()





