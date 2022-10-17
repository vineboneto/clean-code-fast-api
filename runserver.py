import os
import sys

DEFAULT_PORT = os.getenv("PORT") or 3333

if __name__ == "__main__":
    if "--install" in sys.argv:
        os.system("pip install -r requirements.txt")
    import uvicorn

    uvicorn.run("app.server:app", host="0.0.0.0", port=DEFAULT_PORT, reload=True)
