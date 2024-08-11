from fastapi import Depends, FastAPI
import uvicorn
from fastapi.security import HTTPBasic,HTTPBasicCredentials

app = FastAPI()

basic = HTTPBasic()

@app.get("/")
def get_user(
    creds: HTTPBasicCredentials = Depends(basic)):
    return {"username":creds.username, "password":creds.password }

