from textnode import TextNode


def ___main___():
    text = TextNode("Some anchor text", "link", "https://www.boot.dev")
    result = text.__repr__()
    print(result)


___main___()
