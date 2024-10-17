from fastapi import FastAPI
app = FastAPI()

@app.get("/") # "/"를 호출하기 위해
def read_root(): # 함수 사용
    return {"Hello": "World"} # 리턴 값

@app.get("/item")
def read_item(item_id: int, name: str = None, age: int = 0):
    return {"item_id": item_id, "name": name, "age": age}
from fastapi import Form

@app.post("/user")
async def read_user_form(name: str = Form(...), studentcode: str = Form(...), major: str = Form(...)):
    return {"msg": f"{major} {name}님 ({studentcode}) 반갑습니다."}

from fastapi.staticfiles import StaticFiles
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == '__main__': # 바로 실행될 수 있는 코드
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000, log_level="info")