"""
AUTHOR:         zeng_xiao_yu
GITHUB:         https://github.com/zengxiaolou
EMAIL:          zengevent@gmail.com
TIME:           2020/7/27-16:45
INSTRUCTIONS:   测试api swagger 默认值如何设置
"""
from fastapi import FastAPI, Body
import uvicorn

app = FastAPI()


@app.post("/bar")
async def read_item(
        foo: int = Body(default=2, title='描述', description="fool"),
        age: int = Body(..., le=120, title="年龄", description="2222"),
        name: str = Body(..., regex="^xiao\d+$")
):
    return {"foo": foo, "age": age, "name": name}


if __name__ == '__main__':
    uvicorn.run(app="main:app", host="0.0.0.0", port=8080, reload=True, debug=True)
