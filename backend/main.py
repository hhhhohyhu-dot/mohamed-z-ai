from fastapi import FastAPI

print("========== MOHAMED Z AI STARTED ==========")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "WORKING 123"}