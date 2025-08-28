from enum import Enum

class TextType(Enum):
    TEXT = "TEXT"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, text_type: TextType = TextType.TEXT , url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url if text_type == TextType.LINK else None

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return NotImplemented
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text},{self.text_type},{self.url})"

    def to_dict(self):
        return {
            "text": self.text,
            "text_type": self.text_type.value
        }