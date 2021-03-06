# 需要安装：
#   fastapi     0.68.1
#   uvicorn     0.15.0

from fastapi import FastAPI
from vo import Item

app = FastAPI()

# http://localhost:8080/test/a=1/b=2
@app.get('/test/a={a}/b={b}')
def calculateGet(a: int = None, b: int = None):
    c = a + b
    res = {"res": c}
    return res

# http://127.0.0.1:8080/test
@app.post('/test')
def calculatePost(request_data: Item):
    a = request_data.a
    b = request_data.b
    c = a + b
    res = {"res":c}
    return res

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app,
                host="0.0.0.0",
                port=8080,
                workers=1)
