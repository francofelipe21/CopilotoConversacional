from backend import app
from routers.messages import router as messages_router
from routers.documents import router as documents_router


@app.get("/")
async def root():
    return {"message": "Server working"}

app.include_router(messages_router)
app.include_router(documents_router)
