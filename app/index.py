from fastapi import FastAPI
from routes.api import router as pdf_router
from routes.index import router as index_router

app = FastAPI(title="API Для генерации PDF документов")

app.include_router(index_router)
app.include_router(pdf_router, prefix="/api")

# Для локального запуска (если нужно)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("index:app", host="0.0.0.0", port=8000, reload=True)
