from fastapi import FastAPI

from apis.Item.routers import router as item_router

app = FastAPI()
app.include_router(prefix='/items', router=item_router)
