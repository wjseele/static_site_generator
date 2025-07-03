from enum import Enum, auto


class TextType(Enum):
    TEXT = auto()
    BOLD = auto()
    ITALIC = auto()
    CODE = auto()
    LINK = auto()
    IMAGE = auto()


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, other):
        if self.__class__ is not other.__class__:
            return NotImplemented
        text_equal = self.text == other.text
        type_equal = self.text_type == other.text_type
        url_equal = self.url == other.url
        return text_equal and type_equal and url_equal

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
