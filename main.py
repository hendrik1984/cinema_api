from fastapi import FastAPI

app = FastAPI(
    title="Cinema Ticketing API",
    description="API for cinema ticketing system",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "data": "Welcome to Cinema Ticketing API",
        "version": "1.0.0"
    }

@app.get('/health')
def health_check():
    return {
        "status": "OK"
    }