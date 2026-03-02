from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Griff_SQLFAstudy21@localhost:3306/my_first_fastapi_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"  
    
    id = Column(Integer, primary_key=True, index=True) 
    username = Column(String(50)) 

SessionLocal = sessionmaker()
app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/register")
async def register(username: str = Form(...)):
    return {"message": f"こんにちは、{username}さん！FastAPIへようこそ！"}




"""
こうすれば、PythonがHTMLを書き換えれる

@app.post("/register", response_class=HTMLResponse)
async def register(request: Request, username: str = Form(...)): 
    return templates.TemplateResponse(
        "index.html", 
        {
            "request": request,    
            "user_name": username  
        }
    )
"""
