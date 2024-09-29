from fastapi import FastAPI

app = FastAPI() # app - это объект верхнего уровня, представляющий веб-приложение

@app.get("/hi")
def greet():
    return "Hello? World?"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)
