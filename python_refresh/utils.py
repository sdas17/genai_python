# utils.py — Production Utility Module
# =====================================
# This module provides reusable utility functions
# for the application. It can be:
#   - Run directly for testing  : python utils.py
#   - Imported as a module      : from utils import greet_user
# """
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

import os
import sys

APP_NAME = "MyApp"
VERSION = "1.0.0"
MAX_RETRIES = 1\

def c():
    """Entry point of the application."""
    print(f"Welcome to {APP_NAME} v{VERSION}")
    print(f"Python version: {sys.version}")
    print(f"Running from: {os.getcwd()}")
if __name__ == "__main__":
    c()

def greet_user(name: str, role: str):
    return f"hiii {name} how can i help you!!!!!  and what {role} is really doing "
def get_app_info():
    return {"app": APP_NAME, "version": VERSION}
def is_valid_username(username: str):
    print(type(username))
    if(len(username)>10):
        return True
    else:
        return False
    

