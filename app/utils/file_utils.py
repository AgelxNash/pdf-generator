import re
from typing import Optional

def clean_text(text: Optional[str]) -> str:
    if not text:
        return ""
    return re.sub(r"[^а-яА-ЯёЁ0-9_]", "", text)
