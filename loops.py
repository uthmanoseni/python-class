# Example: Iterating through a list
fruits = ["apple", "banana", "cherry"]
for demolaFridgeFruit in fruits:
    print(demolaFridgeFruit)

# Example: Iterating through a range of numbers
for alex in range(16):  # Iterates from 0 to 4
    print(alex)

# Example: Looping until a condition is met
count = 0
while count < 5:
    print(count)
    count += 1  # Increment the counter to eventually make the condition false

# Example: User input validation
password = ""
while password != "secret":
    password = input("Enter the password: ")
    if password != "secret":
        print("Incorrect password. Try again.")
print("Access granted!")

# Generates numbers from 0 to 4 (stop=5)
for i in range(5):
    print(i) # Output: 0, 1, 2, 3, 4

# Generates numbers from 2 to 7 (start=2, stop=8)
for i in range(2, 8):
    print(i) # Output: 2, 3, 4, 5, 6, 7

# Generates numbers from 1 to 9 with a step of 2 (start=1, stop=10, step=2)
for i in range(1, 100, 10):
    print(i) # Output: 1, 3, 5, 7, 9

for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i) # Output: 0, 1, 2, 3, 4















    import random

print("=== Number Guessing Game ===")

# 1. Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# 2. Ask the user to guess
while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess < 1 or guess > 10:
            print("❌ Please guess a number within the range 1–10.")
            continue

        if guess == secret_number:
            print("🎉 Correct! You guessed the number!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")

# 3. Check if the number is even or odd
if secret_number % 2 == 0:
    print(f"\n✅ The secret number {secret_number} is even.")
else:
    print(f"\n✅ The secret number {secret_number} is odd.")

# 4. Print its square using a loop
print("\n📘 Displaying the square of the number using a loop:")
for i in range(1, 2):  # simple loop to demonstrate the concept
    print(f"The square of {secret_number} is {secret_number ** 2}")

print("\n=== Game Over ===")