from fastapi import FastAPI, Body, Header

app = FastAPI()

@app.get("/hi")
def greet01(who):
    return f"Hello? {who}?"


@app.post("/header")
def get_header(who:str = Header()):
    return f"Hello? {who}?"


@app.post("/body")
def get_body(who:str = Body(embed=True)):
    return f"Hello? {who}?"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello01:app", reload=True)
