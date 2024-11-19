from enum import Enum


class TextType(Enum):
    NORMAL_TEXT: str = 'normal'
    BOLD_TEXT: str = 'bold'
    ITALIC_TEXT: str = 'italic'
    CODE_TEXT: str = 'code'
    LINK_TEXT: str = 'link'
    IMAGE_TEXT: str = 'image'


class TextNode():
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text: str = text
        self.text_type: TextType = text_type
        self.url: str = url

    def __eq__(self, other: 'TextNode'):
        text_is_equal = self.text == other.text
        text_type_is_equal = self.text_type == other.text_type
        url_is_equal = self.url == other.url
        if (text_is_equal and text_type_is_equal and url_is_equal):
            return True
        else:
            return False

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'
