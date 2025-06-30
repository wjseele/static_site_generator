from textnode import TextNode, TextType


def __main__():
    text = TextNode("Some anchor text", TextType.LINK, "https://www.boot.dev")
    result = text.__repr__()
    print(result)


__main__()
