from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "OK"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/docs-test")
async def docs_test():
    return {"working": True}