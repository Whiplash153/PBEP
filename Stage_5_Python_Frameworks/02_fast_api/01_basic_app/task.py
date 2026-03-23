from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def read_root():
    return {"message": "Hello from task"}

@app.get("/status")
def status_version():
    return {
        "status": "ok",
        "version": "1.0"
    }

