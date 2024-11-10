from fastapi import FastAPI

app = FastAPI() # это объект верхнего уровня, представляющий веб-приложение

@app.get("/hi/{who}") # декоратор пути
def greet00(who): # функция пути
    return f"Hello? {who}?"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello00:app", reload=True)
