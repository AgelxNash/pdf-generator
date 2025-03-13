from fastapi import APIRouter
from fastapi.responses import HTMLResponse
import os

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def get_index() -> HTMLResponse:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Папка app/
    index_path = os.path.join(base_dir, "templates", "index.html")

    if not os.path.exists(index_path):
        return HTMLResponse("<h1>Файл index.html не найден</h1>", status_code=404)

    with open(index_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    return HTMLResponse(content=html_content, status_code=200)
