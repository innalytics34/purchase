from starlette.middleware.cors import CORSMiddleware
from uvicorn import run
from fastapi import FastAPI, Request, HTTPException, Depends, Cookie
import json
from auth import py_jwt
from login import py_login
from sidebar import py_sidebar
from filter import py_filter
from register import py_register
from team_management import py_team_management
from bookings import py_bookings, Admin_bookings
from admin import py_admin
from judge import py_judge

auth_scheme = py_jwt.JWTBearer()

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "success"}


@app.get("/QCFI/get_encrypt_pwd")
async def get_encrypt_pwd(data: str = '{"pwd": "password"}'):
    try:
        req = json.loads(data)
        response = py_login.get_encrypt_pwd(req)
        return response
    except Exception as e:
        print(str(e))


@app.get("/QCFI/get_decrypt_pwd")
async def get_decrypt_pwd(data: str = '{"pwd": "password"}'):
    try:
        req = json.loads(data)
        response = py_login.get_decrypt_pwd(req)
        return response
    except Exception as e:
        print(str(e))


@app.post("/QCFI/login")
async def login(request: Request):
    try:
        request = await request.json()
        response = py_login.fn_login(request)
        return response
    except Exception as e:
        print(str(e))



if __name__ == "__main__":
    run(app, host="0.0.0.0", port=805)
