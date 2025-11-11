print('Mango, Orange, Pineapple, Apple, Banana')

def greet(name):
    if name:
        print(f"Hello, {name}!") # This line is indented, belonging to the if block
        print('Mango, Orange, Pineapple, Apple, Banana')
    else:
        print("Hello, stranger!") # This line is also indented, belonging to the else block
    print("Welcome to Python.") # This line is at the same indentation level as the if/else, belonging to the function but outside the conditional blocks

# Declaration and assignment
my_integer = 10
my_string = "Hello"
my_float = 20.5
is_true = True

mike = "Michael Anthony"

print(mike)

my_name = "Ademola Oseni"

print(my_name)

my_age = 15

print(my_age)

address = "lagos"

print(address)

favorite_food = "eba"

print(favorite_food)


age = 30
year = -2024
price = 19.99
pi_value = 3.14159
big_number = 12345678901234567890
scientific_notation = 1.2e3 # Represents 1.2 * 10^3 = 1200.0

name = "Alice"
greeting = 'Hello, World!'
multi_line_string = """This is a string
that spans multiple lines."""
is_student = True
has_permission = False
is_valid = (5 > 12) # Evaluates to false

print(type(name)) # Output: <class 'str'>
print(type(age)) # Output: <class 'int'>
print(type(price)) # Output: <class 'float'>
print(type(is_student)) # Output: <class 'bool'>



# String to Integer
num_str = 34567123767456789 + 45678456789034567890
num_int = int(num_str)
print(num_int + 1) # Output: 124

# Integer to Float
num_int = 10
num_float = float(num_int)
print(num_float) # Output: 10.0

# Integer to String
ages = 70
age_str = str(ages)
print(("I am " + age_str + " years old.") * 3) # Output: I am 25 years old.



name = input("please enter your name: ")
age_str = input("please enter your age: ")
favoriteColor = input("please enter your favorite color: ")


age = int(age_str)
age_in_five_years =age + 5


print("\n--- user Information---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Favorite color: {favoriteColor}")
print(f"In 5 years, {name} will be { age_in_five_years} years old.")


Username = input("please enter your username: ")
Telephone = input("please enter your telephone number: ")
address = input("please enter your addreess: ")
password = input("please enter your password: ")


print("\n---User Information ---")
print(f" Username: {Username}")
print(f"Telephone Number: {telephoneNumber}")
print(f"Address: {address}")
print(f"Password: {password}")
