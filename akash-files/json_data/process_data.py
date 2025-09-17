import json 

# Task 1:
try:
    with open ("employees.json") as f:
        content = json.load(f)
        print(content)
    
    employees = content['employees']

except FileNotFoundError:
    print("Error: employees.json not found.please create the file")
    employees = []


# --- Task 2: List All Employee Names ---
print("--- Employee Names ---")
# Your code here: Loop through the 'employees' list and print each employee's 'name'.
for i in employees:
    print(i['name'])

print("\n--- Department Information ---")
# --- Task 3: Count Engineering Employees ---
engineering_count = 0
for i in employees:
    if i['department'] == 'Engineering':
        engineering_count += 1
print(f"The number of employees in Engineering: {engineering_count}")


print("\n--- Skills Information ---")
# --- Task 4: List All Unique Skills ---
all_skills = set() # Using a set automatically handles uniqueness.
# Your code here: Loop through each employee. Then, loop through their 'skills' list
# and add each skill to the 'all_skills' set.
for i in employees:
    for j in i['skills']:
        # print(j)
        all_skills.add(j)
# print(all_skills)
print(f"Unique skills across all employees: {sorted(list(all_skills))}")


    
