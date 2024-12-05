from fastapi import FastAPI
from flask.globals import app_ctx

app1 = FastAPI()
@app1.get('/')
def read_root():
    return {"Hello": "World"}
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app1, host='localhost', port=8000)
    # Compare this snippet from D_12_main.py:
    #     print(sqrt(2))             # 1.4142135623730951, square root
