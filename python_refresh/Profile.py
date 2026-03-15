# Task: Create a file called profile.py
# Requirements:
# 1. Create variables: name, age, city, job, is_student
# 2. Print a formatted profile using f-strings
# 3. Use the __name__ == "__main__" guard

# Expected output:
# ===== My Profile =====
# Name    : Ravi
# Age     : 21
# City    : Mumbai
# Job     : Python Developer
# Student : True
# ======================

# Task: Create calculator.py
# Requirements:
# 1. Write 4 functions: add(), subtract(), multiply(), divide()
# 2. Each function must have TYPE HINTS
# 3. divide() must handle division by zero — return None if zero
# 4. __name__ == "__main__" block must test all 4 functions

# Expected output:
# add(10, 5)      = 15
# subtract(10, 5) = 5
# multiply(10, 5) = 50
# divide(10, 5)   = 2.0
# divide(10, 0)   = None   ← no crash!

# Task: Create utils.py — a real production-style utility file
# Requirements:
# 1. MODULE DOCSTRING at the top explaining what the file does
# 2. Constants: APP_NAME, VERSION, MAX_RETRIES
# 3. Function: greet_user(name: str, role: str) -> str
#    returns "Welcome, Ravi! Role: Admin"
# 4. Function: get_app_info() -> dict
#    returns {"app": APP_NAME, "version": VERSION}
# 5. Function: is_valid_username(username: str) -> bool
#    returns True if username length is between 3 and 20 characters
# 6. __name__ == "__main__" block that tests all functions
#
# BONUS: Create main.py that IMPORTS utils.py and uses all 3 functions
#        Prove that the __main__ block in utils.py does NOT run on import


# Task: Create types_explorer.py
# Requirements:
# Create ONE variable of each type below and for each:
#   → print the value
#   → print type()
#   → print isinstance() check

# Types to cover:
# int, float, str, bool, None
# + show 3 falsy values using bool()

# Expected output style:
# Value: 25        | Type: <class 'int'>   | Is int? True
# Value: 3.14      | Type: <class 'float'> | Is float? True
# Value: Ravi      | Type: <class 'str'>   | Is str? True
# ...and so on

# Task: Create student.py
# Requirements:
# Store a student's data using the CORRECT data types:
#   name         → str
#   age          → int
#   marks        → float  (out of 100)
#   is_passed    → bool   (True if marks >= 40)
#   grade        → str    (A if >=80, B if >=60, C if >=40, F if <40)
#   middle_name  → None   (optional — student has no middle name)
#
# Print a formatted report card using f-strings
#
# Expected output:
# ========= Report Card =========
# Name        : Ravi
# Age         : 21
# Marks       : 85.5 / 100
# Grade       : A
# Passed      : True
# Middle Name : None
# ===============================
name='subham kumar das'
age =21
city='Thane'
job='software enginerring'
is_student=False

def student_name():
    print(f"my name is {name}")
    print(f"iam age {age}/n im lived {city}")
    print(f"and my job {job}")

if __name__ == "__main__":
   student_name()

   # Task: Create mutable_demo.py
# This assignment proves you TRULY understand mutable vs immutable
#
# Part 1 — SHOW THE BUG:
#   Create list1 = [1, 2, 3]
#   Assign list2 = list1
#   Append 4 to list1
#   Print both — show list2 also changed
#   Print id(list1) == id(list2) → must print True
#
# Part 2 — FIX THE BUG:
#   Create list3 = [1, 2, 3]
#   Assign list4 = list3.copy()
#   Append 4 to list3
#   Print both — show list4 is safe
#   Print id(list3) == id(list4) → must print False
#
# Part 3 — PROVE IMMUTABLE:
#   Create a = "hello"
#   Assign b = a
#   Reassign a = "world"
#   Print both — show b is still "hello"
#   Explain in a comment WHY b didn't change
#
# BONUS: Do the same bug demo with dict
#   d1 = {"name": "Ravi"}
#   d2 = d1
#   d1["age"] = 25
#   Show d2 also got "age" — then fix with .copy()

from utils import greet_user,get_app_info,is_valid_username

greet_user_response = greet_user('subham','software eng')
sample_response=get_app_info()
sample_data =is_valid_username('sdsd')
print(greet_user_response,sample_response,sample_data)
