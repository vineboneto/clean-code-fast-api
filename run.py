import sys
import os

args = sys.argv

if "--install" in args:
    os.system("pip install -r requirements.txt")

if "--start" in args:
    os.system("python -m uvicorn main:app --reload --port 3333")
