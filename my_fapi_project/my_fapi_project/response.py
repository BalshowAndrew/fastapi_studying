from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/heder/{name}/{value}")
def header(name:str, value:str, response:Response):
    response.headers[name] = value
    return "normal body"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("response:app", reload=True)

    
