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
"""
types_explorer.py
==================
Explores all basic Python data types.
Prints value, type, and isinstance check for each.
"""
is_student = True
print(f"Value: {str(is_student):<10} | Type: {str(type(is_student)):<20} | Is bool?  {isinstance(is_student, bool)}")

# ─────────────────────────────────────────────
# 5. None — no value / empty
# ─────────────────────────────────────────────
middle_name = None
print(f"Value: {str(middle_name):<10} | Type: {str(type(middle_name)):<20} | Is None?  {middle_name is None}")

# ─────────────────────────────────────────────
# 6. Three falsy values using bool()
# ─────────────────────────────────────────────
print("\n--- Falsy values ---")
print(f"bool(0)    → {bool(0)}   ← zero integer is always False")
print(f'bool("")   → {bool("")}   ← empty string is always False')
print(f"bool([])   → {bool([])}   ← empty list is always False")
print(f"bool(None) → {bool(None)}   ← None is always False")


# ─────────────────────────────────────────────
if __name__ == "__main__":
    pass 

# mutable # immutable

#immutable 
#int,float,string,tuple,bool
# ── int is immutable ──────────────────────────
a = 10
b = a           # b points to same object
a = 20          # a now points to a BRAND NEW object
print(a)        # 20
print(b)        # 10 ← b is safe! not affected

# PROOF with id()
x = 10
y = x
print(id(x) == id(y))   # True  → same object right now
x = 99
print(id(x) == id(y))   # False → x moved to new object

# ── str is immutable ──────────────────────────
name1 = "Subham"
name2 = name1           # both point to same string
name1 = "Ravi"          # name1 moves to NEW string object
print(name1)            # Ravi
print(name2)            # Subham ← completely safe!

# ── You CANNOT change a string in place ───────
word = "hello"
# word[0] = "H"         # ❌ TypeError: str does not support item assignment
                        # strings are LOCKED — cannot edit individual characters

# ── To "change" a string — create a new one ───
print(word[1:])
word = "H" + word[1:]   # creates brand new string "Hello"
print(word)             # Hello

# ── tuple is immutable ────────────────────────
coords = (10, 20, 30)
# coords[0] = 99        # ❌ TypeError: tuple does not support item assignment
print(coords)           # (10, 20, 30) — locked forever

# mutable 
#list,dict,set
















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