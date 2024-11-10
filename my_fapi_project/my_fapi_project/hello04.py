from fastapi import FastAPI, Header

app = FastAPI()

@app.post("/agent")
def get_agent(user_agent: str = Header()):
    return user_agent



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello04:app", reload=True)

