import uvicorn
from src.app.app import app

if __name__ == "__main__":
    uvicorn.run("src.app.app:app", port = 8080)
