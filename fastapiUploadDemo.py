# 需要安装：
#   fastapi             0.68.1
#   uvicorn             0.15.0
#   python-multipart    0.0.5
#   aiofiles            0.7.0

#参考：https://blog.csdn.net/lilygg/article/details/114927483
import os

from fastapi import FastAPI, File, UploadFile
from starlette.responses import FileResponse

app = FastAPI()

# http://127.0.0.1:8080/upload
# 上传本地文件到服务端
# UploadFile转为文件对象，可以保存文件到本地
@app.post("/upload")
async def upload(fileb: UploadFile = File(...)):

    # 二进制流读取前端上传到的fileb文件
    contents = await fileb.read()
    print(contents)
    print(fileb.filename)
    # open方法打开新文件
    # 参数一 文件存储路径+文件名称，存储路径目录需要提前创建好，如果没有指定，则默认会保存在本文件的同级目录下
    # 参数二 wb，表示以二进制格式打开文件，用于只写
    with open("./file/" + fileb.filename, "wb") as f:
        # 将获取的fileb文件内容，写入到新文件中
        f.write(contents)

    # 启动服务后，会在本地FastAPI服务器的/file/目录下生成 前端上传的文件
    return ({
        'file_size': len(contents),
        'file_name': fileb.filename,
        'file_content_type': fileb.content_type
    })

# http://127.0.0.1:8080/download/{file_name}
# 下载服务端文件到本地
@app.get("/download/{file_name}")
def download(file_name: str):
    # 获取服务端绝对路径
    basedir = os.path.abspath(os.path.dirname(__file__))
    # 服务端文件绝对路径
    file_path = basedir + "\\file\\" + file_name
    print(file_path)
    # 在浏览器打开文件
    return FileResponse(file_path)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app,
                host="0.0.0.0",
                port=8080,
                workers=1)