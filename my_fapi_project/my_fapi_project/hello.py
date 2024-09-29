from fastapi import FastAPI

app = FastAPI() # app - это объект верхнего уровня, представляющий веб-приложение

@app.get("/hi/{who}")
def greet(who):
    return f"Hello? World? {who}?"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)
