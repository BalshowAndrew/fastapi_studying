from fastapi import FastAPI

app = FastAPI() # app - это объект верхнего уровня, представляющий веб-приложение

@app.get("/hi")
def greet(who):
    return f"Hello? {who}?"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)
