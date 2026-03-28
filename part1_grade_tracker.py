#  Q: 2 Assignment — Part 1: Python Basics & Control Flow
# Theme: Student Grade Tracker

# Given data
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

def print_task(title):
    print("\n" + "="*50)
    print(title)
    print("="*50 + "\n")

# Task 1 — Data Parsing & Profile Cleaning
# Loop through students
print_task("Task 1 — Data Parsing & Profile Cleaning")
# Requirement 1
for student in raw_students:
    ## Remove space and convert to Title Case
    name = student["name"].strip().title()
    ## Convert from string to integer
    roll = int(student["roll"])
    ## Convert to list
    marks_list = student["marks_str"].split(",")
    ## Convert list elements to integer
    marks = []
    for m in marks_list:
        marks.append(int(m))
  
# Requirement 2
    valid = True
    for word in name.split():
      if not word.isalpha():
        valid = False
    if valid:
      print(name,"✓ Valid name")
    else:
     print(name, "✗ Invalid name")

# Requirement 3
    print(f"""==================================
Student : {name}
Roll No : {roll}
Marks   : {marks}
==================================""",)
    
# Requirement 4
    if roll == 103 :
     print(name.upper())
     print(name.lower())
     
# --------------------------------------------------------------------------------------------------------------------------
# Task 2 — Marks Analysis Using Loops & Conditionals
print_task("Task 2 — Marks Analysis Using Loops & Conditionals")

# 1 Loop together condition & print
# Given data
student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

for i in range(len(subjects)):
  if 90 <= marks[i] <= 100:
    print(subjects[i],marks[i],"A+")
  elif 80 <= marks[i] <= 89:
    print(subjects[i],marks[i],"A")
  elif 70 <= marks[i] <= 79:
    print(subjects[i],marks[i],"B")
  elif 60 <= marks[i] <= 69:
    print(subjects[i],marks[i],"C")
  else:
    print(subjects[i],marks[i],"F")

print()
# 2. Calculate and print:
total_marks = sum(marks)
average_marks = round(total_marks / len(marks),2)
high_score = max(marks)
## Find Index
index = marks.index(high_score)
low_score = min(marks)
index1 = marks.index(low_score)
print(f"Total marks = {total_marks}")
print(f"Average marks = {average_marks}")
print("Highest scoring subject = ", subjects[index],high_score)
print("Lowest scoring subject = ", subjects[index1],low_score)

# --------------------------------------------------------------------------------------------------------------
# 3. Using a while loop, simulate a marks-entry system that allows adding new subjects:

count = 0

subject = input("Enter new subject / done : ").strip()

while subject.lower() != "done":
    # Subject blank check
    if subject == "":
     print("Subject cannot be empty ✗")
     subject = input("\nEnter new subject / done : ").strip()
     continue

    # Duplicate check (case-insensitive)
    if subject.lower().strip() in [s.lower().strip() for s in subjects]:
        print("Subject already exists ✗")
        subject = input("\nEnter new subject / done : ").strip()
        continue
        
    while True:
        mark_input = input("Enter the marks (0-100): ")

        try:
            mark = float(mark_input)
        except ValueError:
            print("Invalid input ✗")
            continue

        if 0 <= mark <= 100:
            break
        else:
            print("Marks must be between 0 and 100 ✗")


    subjects.append(subject.strip())
    marks.append(mark)
    count = count + 1

    subject = input("\nEnter new subject / done : ").strip()
    
# Final calculations
total_marks = sum(marks)
average_marks = round(total_marks / len(marks), 2)

print("\nNew subjects added:", count)
print("Updated subjects:", subjects)
print("Updated marks:", marks)
print("Updated average:", average_marks)



# Task 3 — Class Performance Summary
print_task("Task 3 — Class Performance Summary")

# Given data
class_data = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma", [55, 68, 49, 72, 61]),
    ("Priya Nair", [91, 85, 88, 94, 79]),
    ("Karan Mehta", [40, 55, 38, 62, 50]),
    ("Sneha Pillai", [75, 80, 70, 68, 85]),
]

# Initialize counters
pass_count = 0
fail_count = 0
total_avg_sum = 0

topper_name = ""
topper_avg = 0

print("Name               | Average | Status")
print("----------------------------------------")

# Loop through each student
for name, marks in class_data:
    
    # Step 1: Calculate average
    avg = round(sum(marks) / len(marks), 2)
    
    # Step 2: Decide pass/fail
    if avg >= 60:
        status = "Pass"
        pass_count = pass_count + 1
    else:
        status = "Fail"
        fail_count = fail_count + 1
    
    # Step 3: Track topper
    if avg > topper_avg:
        topper_avg = avg
        topper_name = name
    
    # Step 4: Add to total for class average
    total_avg_sum = total_avg_sum + avg
    
    # Step 5: Print each row,left aligned
    print(f"{name:<18} | {avg:<7} | {status}")

# Step 6: Calculate class average
class_avg = round(total_avg_sum / len(class_data), 2)

# Step 7: Final outputs
print("\nPassed:", pass_count)
print("Failed:", fail_count)
print("Topper:", topper_name, topper_avg)
print("Class Average:", class_avg)



# -----------------------------------------------------------

# Task 4 — String Manipulation Utility
print_task("Task 4 — String Manipulation Utility")

# Given data

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# ---------------------------------------------------
# Step 1: Remove leading and trailing spaces
clean_essay = essay.strip()
print("Step 1 - Clean Essay:\n", clean_essay)
print()

# ---------------------------------------------------
# Step 2: Convert to Title Case
title_case = clean_essay.title()
print("Step 2 - Title Case:\n", title_case)
print()

# ---------------------------------------------------
# Step 3: Count occurrences of "python" (case-insensitive)
# Since clean_essay is already lowercase, we can directly use count()
count_python = clean_essay.count("python")
print("Step 3 - Count of 'python':", count_python)
print()

# ---------------------------------------------------
# Step 4: Replace "python" with "Python 🐍"
replaced_text = clean_essay.replace("python", "Python 🐍")
print("Step 4 - Replace 'python':\n", replaced_text)
print()

# ---------------------------------------------------
# Step 5: Split essay into sentences
# Split using ". " (dot + space)
sentences = clean_essay.split(". ")
print("Step 5 - Sentences List:\n", sentences)
print()

# ---------------------------------------------------
# Step 6: Print each sentence in new line with numbering
print("Step 6 - Numbered Sentences:")
for i, sentence in enumerate(sentences, start=1):
    # Add '.' if sentence does not end with it
    if not sentence.endswith("."):
        sentence = sentence + "."
    
    print(f"{i}. {sentence}")
