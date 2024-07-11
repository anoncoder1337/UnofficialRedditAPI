import os
import asyncio
import argparse
from fastapi import FastAPI
from dotenv import load_dotenv
import hypercorn.asyncio

# Load environment variables from .env file if it exists
load_dotenv()

app = FastAPI()

REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")

@app.get("/")
async def read_root():
    return {"message": "stub"}

async def start_server(host: str, port: int):
    config = hypercorn.Config()
    config.bind = [f"{host}:{port}"]
    await hypercorn.asyncio.serve(app, config)

def main():
    parser = argparse.ArgumentParser(description="Unofficial Reddit API Server")
    parser.add_argument("-H", "--host", type=str, default="127.0.0.1", help="Host to bind the server to (default: 127.0.0.1)")
    parser.add_argument("-p", "--port", type=int, default=8080, help="Port to bind the server to (default: 8080)")
    args = parser.parse_args()

    if REDDIT_USERNAME and REDDIT_PASSWORD:
        print(f"Starting server on {args.host}:{args.port}")
        asyncio.run(start_server(args.host, args.port))
    else:
        print("REDDIT_USERNAME and REDDIT_PASSWORD must be set in the environment or .env file")

if __name__ == "__main__":
    main()