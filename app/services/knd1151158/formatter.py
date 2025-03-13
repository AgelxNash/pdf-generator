from typing import Dict, Any, Tuple
from PIL import ImageDraw, ImageFont


class Formatter:
    def __init__(
            self,
            draw: ImageDraw.ImageDraw,
            font: ImageFont.FreeTypeFont,
            data: Dict[str, Any],
            field_mapping: Dict[str, Dict[str, Tuple[float, float]]]
    ):
        self.draw = draw
        self.font = font
        self.data = data
        self.field_mapping = field_mapping

    @staticmethod
    def pad_text(text: str, length: int, pad_char: str = "-") -> str:
        return text.ljust(length, pad_char)

    def draw_spaced_text(self, text: str, start_x: float, y: float, spacing: float = 39.4) -> None:
        x = start_x
        for char in text:
            self.draw.text((x, y), char, font=self.font, fill="black")
            x += spacing

    def fill_page(self, page_type: str) -> None:
        fields: Dict[str, Tuple[float, float]] = self.field_mapping.get(page_type) or {}
        for key, (x, y) in fields.items():
            value = self.data.get(key, "")
            if key == "summa_rashodov_before_dot":
                value = self.pad_text(value, 13)
            if key == "korr_number":
                value = self.pad_text(value, 3)
            self.draw_spaced_text(value, x, y)
