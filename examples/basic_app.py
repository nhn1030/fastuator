from fastapi import FastAPI
from fastuator import Fastuator

app = FastAPI()
Fastuator(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
