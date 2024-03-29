import uvicorn
from fastapi import FastAPI

from apis.Item.routers import router as item_router

app = FastAPI()
app.include_router(prefix='/items', router=item_router)

if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host='127.0.0.1',
        port=8000,
        reload=True,
    )
