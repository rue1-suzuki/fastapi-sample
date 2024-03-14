# FastAPI

[FastAPI](https://fastapi.tiangolo.com/ja/)

Pythonのwebフレームワーク

- 構文がシンプル
- ドキュメントの自動生成
- リクエストの構造が厳密
- ASGIサーバで非同期処理をサポート

## サンプルコードの実行

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## 自動生成されるドキュメント

- [/docs](http://127.0.0.1:8000/docs)
- [/redoc](http://127.0.0.1:8000/redoc)

## データの受け取り

それぞれ専用の受け取り方法があるのでそれを使う。

リクエスト変数から取得する方法はドキュメントが曖昧になり、バリデーションも行われない。

```python
from fastapi import Body, Form, Header, Path, Query

def create(name: str = Body(), price: int = Body(default=1000),):
    pass
```

- ```Body``` リクエストボディ(json)
- ```Form``` リクエストボディ(form)
- ```Header``` リクエストヘッダー
- ```Path``` パスパラメータ
- ```Query``` クエリパラメータ

## ルーティング

```APIRouter```を使用

```python
from fastapi import APIRouter


router = APIRouter(tags=['Item'])
```

```python
from fastapi import FastAPI

from routers.Item import router as item_router


app = FastAPI()
app.include_router(router=item_router, prefix='/items')
```

## DBとの接続

```SQLAlchemy```を使用

DB接続用のsessionなどを```database.py```に集約

テーブル定義は各router内の```models.py```に定義

```models.py```の変更後は```python migrate.py```
