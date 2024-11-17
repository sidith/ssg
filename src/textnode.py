from enum import Enum


class TextType(Enum):
    NORMAL_TEXT = 'normal'
    BOLD_TEXT = 'bold'
    ITALIC_TEXT = 'italic'
    CODE_TEXT = 'code'
    LINK_TEXT = 'link'
    IMAGE_TEXT = 'image'


class TextNode():
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text: str = text
        self.text_type: TextType = text_type
        self.url: str = url

    def __eq__(self, other: 'TextNode'):
        if (self.text == other.text and
            self.text_type == other.text_type and
                self.url == other.url):
            return True
        return False

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'
