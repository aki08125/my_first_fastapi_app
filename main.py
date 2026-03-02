from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

# 1. FastAPIの本体（アプリ）を作る
app = FastAPI()

# 2. HTMLファイルを置く場所（templatesフォルダ）を登録する
templates = Jinja2Templates(directory="templates")

# --- ここから「窓口（ルート）」の作成 ---

# 【GET窓口】ブラウザで「/」にアクセスしたときに、入力画面を表示する
@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    # index.htmlを表示してください、という命令
    return templates.TemplateResponse("index.html", {"request": request})

# 【POST窓口】「送信」ボタンが押されたときに、名前を受け取って返事をする
@app.post("/register")
async def register(username: str = Form(...)):
    # 届いた名前（username）を使ってメッセージを作る
    return {"message": f"こんにちは、{username}さん！FastAPIへようこそ！"}