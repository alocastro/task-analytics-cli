from functions import get_choice, get_valid_name, get_valid_number, task_names

# Phase 1: Task Database Creation
priorities = ["high", "medium", "low"]


def build_tasks() -> list:
    """Prompts the user to register tasks and returns a list of task dictionaries."""
    n_tasks = get_valid_number("How many tasks do you want to register? (positive integer): ", minimum_value=1)
    task_list = []

    for i in range(1, n_tasks + 1):
        print(f"\n--- Entering Task {i} ---")
        task_name = task_names("Enter task title: ")
        task_priority = get_choice("Enter priority (high, medium, low): ", priorities)
        task_duration = get_valid_number("Enter estimated time in minutes (>0): ", minimum_value=1)

        task_list.append({
            "ID": i,
            "Name": task_name,
            "Priority": task_priority,
            "Duration": task_duration,
            "Completed": False,
        })

    return task_list


# Phase 2: Data Processing & Output
tasks = build_tasks()

print("\n================ TASK REPORT ================")
total_time = 0
total_tasks = 0

for p in priorities:  # Grouping and displaying tasks by priority order
    print(f"\n{p.upper()} priority tasks:")
    found = False

    for element in tasks:
        if element["Priority"] == p:
            print(f"\t- {element['Name']} ({element['Duration']} min)")
            found = True
            total_tasks += 1
            total_time += element["Duration"]

    if not found:
        print("\tNo tasks")

print("------------------------------------------------")

# Calculate average time safely after processing all tasks
mean_time = (total_time / total_tasks) if total_tasks > 0 else 0.0

print(f"\nTotal estimated time: {total_time} min")
print(f"Average estimated time per task: {mean_time:.2f} min\n")

print("================================================")
