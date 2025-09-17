import json

# --- Task 1: Read the JSON Data ---
# Use a 'with' statement to open the file. This is a best practice as it
# automatically closes the file for you.
# 'json.load()' reads the file and converts the JSON data into a Python dictionary.

# try:
#     with open('employees.json', 'r') as file:
#         data = json.load(file)
#         # The JSON's top-level object is a dictionary, and our list is inside the "employees" key.
#         employees = data['employees']
# except FileNotFoundError:
#     print("Error: employees.json not found. Please create the file.")
#     employees = []

try:
   with open ('employees.json','r') as file:
      data = json.load(file)
      # print (data)
      employees = data ['employees']
      # print (employees)

except FileNotFoundError:
      print("Employees.json not found. Please create the file. ")
      employees=[]

# --- Task 2: List All Employee Names ---

print("------Employee Names----")
for i in employees:
    print(i['name'])

# Your code here: Loop through the 'employees' list and print each employee's 'name'.



# --- Task 3: Count Engineering Employees ---
# engineering_count = 0
# Your code here: Loop through the 'employees' list. If an employee's 'department'
# is "Engineering", increment the 'engineering_count'.
print ("\n---Department information---")
engineering_count=0
for i in employees:
    if i ['department']=="Engineering":
        engineering_count +=1

print(f"Number of employees in Engineering : {engineering_count}")



# --- Task 4: List All Unique Skills ---
# all_skills = set() # Using a set automatically handles uniqueness.
# Your code here: Loop through each employee. Then, loop through their 'skills' list
# and add each skill to the 'all_skills' set.
print ("\n--- Skills Informtion ---")
all_skills = set()

for i in employees:
    for skill in i['skills']:
        print(skill)
        all_skills.add(skill)


print(f"Unique skills across all employees: {sorted(list(all_skills))}")
