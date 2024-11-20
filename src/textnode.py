from enum import Enum
from typing import Optional


class TextType(Enum):
    NORMAL_TEXT = 'normal'
    BOLD_TEXT = 'bold'
    ITALIC_TEXT = 'italic'
    CODE_TEXT = 'code'
    LINK_TEXT = 'link'
    IMAGE_TEXT = 'image'


class TextNode:
    def __init__(self,
                 text: str,
                 text_type: TextType,
                 url: Optional[str] = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)

    def __repr__(self) -> str:
        url_display = f", '{self.url}'" if self.url else ''
        return f"TextNode('{self.text}', '{self.text_type.value}'{url_display})"
