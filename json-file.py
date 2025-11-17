import json

# Sample Python data
data = {
    "name": "Alice",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Science"],
    "telephone": 2347034834396,
}

# Define the filename
filename = "data.json"

# Open the file in write mode ('w') and use json.dump() to write the data
with open(filename, 'w') as file:
    json.dump(data, file, indent=4) # indent for human-readable output

print(f"Data successfully stored in {filename}")

try:
    # Open the file in read mode ('r') and use json.load() to read the data
    with open(filename, 'r') as file:
        loaded_data = json.load(file)

    print(f"Data successfully loaded from {filename}:")
    print(loaded_data)
    print(f"Type of loaded data: {type(loaded_data)}")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except json.JSONDecodeError:
    print(f"Error: Failed to decode JSON from '{filename}'. The file might be malformed.")