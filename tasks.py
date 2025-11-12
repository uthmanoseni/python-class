# 1. Declare variables of different data types
integer_num = 10          # int
float_num = 3.5           # float
text = "25"               # string
boolean_value = True      # bool

# Display initial values and types
print("Initial Values and Types:")
print(f"integer_num = {integer_num}, type = {type(integer_num)}")
print(f"float_num = {float_num}, type = {type(float_num)}")
print(f"text = '{text}', type = {type(text)}")
print(f"boolean_value = {boolean_value}, type = {type(boolean_value)}\n")

# 2. Perform operations between them
sum_result = integer_num + float_num         # int + float
multiply_result = integer_num * boolean_value  # int * bool
concat_result = text + str(integer_num)      # string + string

print("Operations Results:")
print(f"Sum (int + float) = {sum_result}")
print(f"Multiply (int * bool) = {multiply_result}")
print(f"Concatenate (string + string) = {concat_result}\n")

# 3. Demonstrate type conversion
converted_text = int(text)                   # Convert string to int
converted_float = float(integer_num)         # Convert int to float
converted_bool = int(boolean_value)          # Convert bool to int

print("After Type Conversions:")
print(f"Converted text to int: {converted_text} (type = {type(converted_text)})")
print(f"Converted int to float: {converted_float} (type = {type(converted_float)})")
print(f"Converted bool to int: {converted_bool} (type = {type(converted_bool)})\n")

# Perform new operation with converted values
new_sum = converted_text + integer_num + int(float_num)
print(f"New Sum (after conversions): {new_sum}")









# 1. Take two numbers as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\n==============================")
print(" ARITHMETIC OPERATIONS ")
print("==============================")

# 2. Perform all arithmetic operations
print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")

# Handle division carefully (avoid divide by zero)
if num2 != 0:
    print(f"Division: {num1} / {num2} = {num1 / num2}")
    print(f"Modulus: {num1} % {num2} = {num1 % num2}")
else:
    print("Division: Cannot divide by zero")
    print("Modulus: Cannot find remainder with zero")

print(f"Exponentiation: {num1} ** {num2} = {num1 ** num2}")

print("\n==============================")
print(" COMPARISON OPERATIONS ")
print("==============================")

# 3. Compare using all comparison operators
print(f"{num1} == {num2} → {num1 == num2}")
print(f"{num1} != {num2} → {num1 != num2}")
print(f"{num1} > {num2} → {num1 > num2}")
print(f"{num1} < {num2} → {num1 < num2}")
print(f"{num1} >= {num2} → {num1 >= num2}")
print(f"{num1} <= {num2} → {num1 <= num2}")

print("\n==============================")
print(" END OF PROGRAM ")
print("==============================")







import re  # For email validation using regex

print("===== USER REGISTRATION SYSTEM =====")


# 2. Validate each input
errors = []

# 1. Take username, email, and password as input
username = input("Enter username: ").strip()
# Username validation
if not username:
    errors.append("❌ Username cannot be empty.")
elif len(username) < 3:
    errors.append("❌ Username must be at least 3 characters long.")

email = input("Enter email: ").strip()
# Email validation using a simple regex pattern
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
if not email:
    errors.append("❌ Email cannot be empty.")
elif not re.match(email_pattern, email):
    errors.append("❌ Invalid email format. Example: user@example.com")

password = input("Enter password: ").strip()
confirm_password = input("Confirm password: ").strip()


# Password validation
if not password:
    errors.append("❌ Password cannot be empty.")
elif len(password) < 6:
    errors.append("❌ Password must be at least 6 characters long.")

# 3. Confirm password match
if password != confirm_password:
    errors.append("❌ Passwords do not match.")

# 4. Display results
print("\n===================================")
if errors:
    print("⚠ Registration failed due to the following errors:")
    for err in errors:
        print("-", err)
else:
    print("✅ Registration Successful!")
    print(f"Welcome, {username}! 🎉")
    print(f"Your registered email: {email}")
print("===================================")










print("===== TEMPERATURE CONVERTER =====")

# 1. Take temperature value and unit as input
try:
    temp_value = float(input("Enter temperature value: "))
    unit = input("Enter unit (C/F): ").strip().upper()

    # 2. Convert between Celsius and Fahrenheit
    if unit == "C":
        converted = (temp_value * 9/5) + 32
        print(f"\n✅ {temp_value}°C is equal to {converted:.2f}°F")

    elif unit == "F":
        converted = (temp_value - 32) * 5/9
        print(f"\n✅ {temp_value}°F is equal to {converted:.2f}°C")

    else:
        # 3. Handle invalid unit
        print("\n❌ Invalid unit! Please enter 'C' for Celsius or 'F' for Fahrenheit.")

except ValueError:
    # 3. Handle invalid numeric input
    print("\n❌ Invalid input! Please enter a numeric temperature value.")

print("\n===== END OF PROGRAM =====")