from fastapi import FastAPI, Header

app = FastAPI()

@app.post("/hi")
def greet03(who:str = Header()):
    return f"Hello? {who}?"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello03:app", reload=True)

