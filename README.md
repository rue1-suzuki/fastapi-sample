# FastAPI

[FastAPI](https://fastapi.tiangolo.com/ja/)

Pythonのwebフレームワーク

- 構文がシンプル
- ドキュメントの自動生成
- リクエストの構造が厳密
- ASGIサーバで非同期処理をサポート

## サンプルコードの実行

開発環境

```bash
pip install -r requirements.txt
python migrate.py
uvicorn main:app --reload
```

本番環境

```bash
pip install -r requirements.txt
python migrate.py
uvicorn main:app --host 0.0.0.0 --port 8000
```

## 自動生成されるドキュメント

- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

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

各api内で```router```を作成

```main.py```で```include_router```

```path```はrouterで定義

```prefix```はinclude_routerに定義

## DBとの接続

```SQLAlchemy```を使用

DB接続用のsessionなどを```database.py```に集約

テーブル定義は各api内の```models.py```に定義

スキーマ(```models.py```)の変更後は```python migrate.py```
