import asyncio, os

_port = os.getenv("PORT", "20335")
try:
    _port = int(_port)
except ValueError:
    _port = 20335
os.environ["PORT"] = str(_port)
os.environ["WEB_PORT"] = str(_port)

from app import main

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nStopped.")
