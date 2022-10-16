import sys
import os

args = sys.argv

DEFAULT_PORT = 3333

port = next(filter(lambda x: x.startswith("--port"), args), DEFAULT_PORT)

port = port.split("=")[1] if isinstance(port, str) else port

if "--install" in args:
    os.system("pip install -r requirements.txt")

if "--start" in args:
    os.system(f"python -m uvicorn main:app --reload --port {port}")
