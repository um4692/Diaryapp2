from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List

app = FastAPI()

# データモデル
class Entry(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime

# データベースの初期エントリー
entries = []

# ホームページ
@app.get('/')
async def home():
    return entries

# 新しいエントリーを作成
@app.post('/new_entry/')
async def new_entry(title: str, content: str):
    entry_id = len(entries) + 1
    created_at = datetime.now()
    entry = Entry(id=entry_id, title=title, content=content, created_at=created_at)
    entries.append(entry)
    return entry

# エントリーを取得
@app.get('/entry/{entry_id}')
async def get_entry(entry_id: int):
    for entry in entries:
        if entry.id == entry_id:
            return entry
    raise HTTPException(status_code=404, detail="Entry not found")

# すべてのエントリーを取得
@app.get('/entries/')
async def get_entries():
    return entries

