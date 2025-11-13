# Simple To-Do List App

todo_list = []

while True:
    print("\n--- TO-DO LIST APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter a new task: ")
        todo_list.append(task)
        print(f"✅ '{task}' added to your to-do list.")

    elif choice == '2':
        print("\nYour To-Do List:")
        if not todo_list:
            print("No tasks yet!")
        else:
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")

    elif choice == '3':
        if not todo_list:
            print("No tasks to remove!")
        else:
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")
            task_num = int(input("Enter the number of the task to remove: "))
            if 1 <= task_num <= len(todo_list):
                removed = todo_list.pop(task_num - 1)
                print(f"❌ '{removed}' removed.")
            else:
                print("Invalid task number!")

    elif choice == '4':
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice! Please enter 1–4.")







        # Student Dictionary with Average Score

students = {}

n = int(input("How many students? "))

for i in range(n):
    name = input(f"Enter name of student {i + 1}: ")
    score = float(input(f"Enter {name}'s score: "))
    students[name] = score

print("\n--- Student Scores ---")
for name, score in students.items():
    print(f"{name}: {score}")

# Calculate average score
average = sum(students.values()) / len(students)
print(f"\n📊 Average Score: {average:.2f}")