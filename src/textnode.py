from enum import Enum, auto


class TextType(Enum):
    PLAIN = auto()
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

    def __eq__(node1, node2):
        text_equal = node1.text == node2.text
        type_equal = node1.text_type == node2.text_type
        url_equal = node1.url == node2.url
        return text_equal and type_equal and url_equal

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
