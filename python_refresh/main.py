"""
Module docstring — every real file has this.
Describes what this module does.
"""

# ✅ Standard library imports first
import os
import sys

# ✅ Then third-party imports
# import requests  (once installed)

# ✅ Then your own modules
# from utils import helper

# --- Main logic ---
APP_NAME = "MyApp"
VERSION = "1.0.0"
MAX_RETRIES = 1\

# cwd is mean by current work directorry
# version is mean by version

def c():
    """Entry point of the application."""
    print(f"Welcome to {APP_NAME} v{VERSION}")
    print(f"Python version: {sys.version}")
    print(f"Running from: {os.getcwd()}")
if __name__ == "__main__":
    c()


# ── Numeric ──────────────────────────────────────
age = 25              # int
price = 99.99         # float
big_num = 1_000_000   # int with _ separator (readable!)
complex_n = 3 + 4j    # complex (used in data science)

name = "Ravi"                     # str (double quotes)
city = 'Mumbai'                   # str (single quotes — same thing)
multi = """This is a
multiline string"""               # triple quotes

intro = f"My name is {name}, I live in {city}"
calc  = f"2 + 2 = {2 + 2}"       # expressions inside!
fmt   = f"Price: ₹{price:.2f}"   # formatting decimals
print(fmt)

# ── Boolean ──────────────────────────────────────
is_active = True
is_deleted = False
result = None    # represents "no value" — used everywhere

# Truthy / Falsy — critical for conditionals
print(bool(0))        # False
print(bool(""))       # False
print(bool([]))       # False
print(bool(None),'s')     # False
print(bool(1))        # True
print(bool(result))  # True
print(bool([1,2]))    # True

                 # function return, optional params, DB nulls
print(type(age)) 
print(isinstance(age, int))     # True
print(isinstance(age, (int,float)))  # True — checks multiple!









# ── int examples ──────────────────────────────
age       = 25
user_id   = 1001
score     = -10
big_num   = 1_000_000     # ✅ underscore makes it readable
zero      = 0

# ── float examples ────────────────────────────
price     = 99.99
tax_rate  = 0.18          # 18% GST
pi        = 3.14159
negative  = -4.5

# ── Arithmetic operations ─────────────────────
print(10 + 3)    # 13    addition
print(10 - 3)    # 7     subtraction
print(10 * 3)    # 30    multiplication
print(10 / 3)    # 3.333 division  → always gives float
print(10 // 3)   # 3     floor division → removes decimal
print(10 % 3)    # 1     modulo → remainder
print(10 ** 3)   # 1000  power / exponent

# ── Type conversion ───────────────────────────
x = int(3.9)       # → 3     (chops decimal, does NOT round)
y = float(5)       # → 5.0
z = int("42")      # → 42    (string to int)
w = str(100)       # → "100" (int to string)

# ── Checking type ─────────────────────────────
age = 25.00
print(type(age))            # <class 'int'>
print(isinstance(age, int)) # True  ← use this in real code

# ── Creating strings ──────────────────────────
print("#### ── Creating strings ──────────────────────────")
intro   = f"My name is {name}"
details = f"Age: {age}, City: {city}"
math    = f"Next year I'll be {age + 1}"      # expression inside!
price   = f"Total: ₹{99.999:.2f}"             # format 2 decimal places
print(price)
print('# ── Useful string methods ─────────────────────')
text = "  Hello World  "
print(text.strip())
print(text.lower())
print(text.upper())
# strip() remove space
# lower() 
# upper()
# capitalize()
#split()
print(text.capitalize())
print(text.split('World'))
print(text.replace("World","chai_code"))

print("# ── String checks ─────────────────────────────")
email = "ravi@gmail.com"
print("@" in email)          # True  ← check if character exists
print(email.startswith("ravi"))  # True
print(email.endswith(".com"))    # True
print(email.count("a"))          # 2
print('# ── String indexing ───────────────────────────')
name='RAVI'
print(name[0])     # R    (first character)
print(name[-1])    # i    (last character)
print(name[1:3])   # av   (slice: index 1 to 2)
print(name[::-1])  # ivaR (reversed)
print(len(name))   # 4    (length)



# ── Basic booleans ────────────────────────────
is_active   = True
is_deleted  = False
is_premium  = True

# ── Comparison gives bool ─────────────────────
print(10 > 5)      # True
print(10 == 10)    # True
print(10 != 5)     # True
print(10 < 3)      # False

# ── bool() — convert anything to bool ─────────
print(bool(1))       # True
print(bool(0))       # False   ← 0 is always False
print(bool("hello")) # True
print(bool(""))      # False   ← empty string is False
print(bool([1,2,3])) # True
print(bool([]))      # False   ← empty list is False
print(bool(None))    # False   ← None is always False

# ── Falsy values — MEMORIZE THIS LIST ─────────
# These ALL evaluate to False in an if-condition:
# 0, 0.0, "", [], {}, set(), None, False

# ── Truthy — everything else is True ──────────
# 1, "hello", [1], {"a":1}, True, any non-zero number

# ── Real world usage ──────────────────────────
user_logged_in = True
cart_items     = []        # empty list → Falsy

# This is how Django checks things:
if user_logged_in:         # same as: if user_logged_in == True
    print("Show dashboard")

if not cart_items:         # same as: if cart_items == []
    print("Your cart is empty")

print('# ── None examples ─────────────────────────────')

result      = None      # no result yet
user        = None      # no user found
middle_name = None      # optional field — person has no middle name

# ── Functions return None by default ──────────
def do_nothing():
    pass                # no return statement

output = do_nothing()
print(output)           # None
print(type(output))     # <class 'NoneType'>

# ── Checking for None ─────────────────────────
# ✅ ALWAYS use 'is' — never use '=='
result = None

if result is None:          # ✅ correct
    print("No result yet")

if result is not None:      # ✅ correct
    print("We have a result!")


# ── Real Django usage ─────────────────────────
def find_user(user_id):
    # imagine querying database
    if user_id == 1:
        return {"name": "Ravi", "age": 25}
    return None            # user not found

user = find_user(99)

if user is None:
    print("User not found!")   # this runs
else:
    print(f"Found: {user['name']}")

# ── IMMUTABLE — int, str, float, tuple ────────
# Cannot be changed after creation
# Python creates a NEW object when you "change" it

a = "hello"
b = a           # b points to same object
a = "world"     # a now points to NEW object
print(b)        # "hello" — b is NOT affected ✅

# ── MUTABLE — list, dict, set ─────────────────
# CAN be changed in place
# Multiple variables can point to SAME object

list1 = [1, 2, 3]
list2 = list1        # ⚠️ both point to SAME list in memory!
list1.append(4)
print(list2)         # [1, 2, 3, 4] ← list2 CHANGED too! 😱

# ── FIX: Always copy when you want independence ──
list1 = [1, 2, 3]
list2 = list1.copy()    # ✅ now list2 is independent
list1.append(4)
print(list1)            # [1, 2, 3, 4]
print(list2)            # [1, 2, 3]   ← safe!

# ── id() proves it ────────────────────────────
x = [1, 2, 3]
y = x
z = x.copy()

print(id(x) == id(y))   # True  → SAME object in memory
print(id(x) == id(z))   # False → DIFFERENT objects


# pyton course 10  modules total
# python coding baaic
#python data types
#python cibdtionaks
#python loops
#python fuctions
#python list ,set,dic,generatoe
#python generators and decorators
#python oop
#python file exceptions
#Python thread process async


#python level 01 begginer 
#python level 02 integemediate
#python industry


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


