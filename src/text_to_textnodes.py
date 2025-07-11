from extractor import split_nodes_image, split_nodes_link
from delimiter import split_nodes_delimiter

from textnode import TextType, TextNode


def text_to_textnodes(text):
    if not text:
        raise ValueError("Didn't receive any text")
    if not isinstance(text, str):
        raise ValueError("This function only takes strings")
    delimiters = {"**": TextType.BOLD, "_": TextType.ITALIC, "`": TextType.CODE}
    split_nodes = split_nodes_image(split_nodes_link([TextNode(text, TextType.TEXT)]))
    for delimiter in delimiters:
        split_nodes = split_nodes_delimiter(
            split_nodes,
            delimiter,
            delimiters[delimiter],
        )
    for node in range(0, len(split_nodes) - 1):
        if not split_nodes[node].text:
            del split_nodes[node]
    return split_nodes
