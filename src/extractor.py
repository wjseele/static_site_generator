import re

from textnode import TextType


def extract_markdown_images(text):
    if text is None:
        raise ValueError("Didn't get any text")
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_links(text):
    if text is None:
        raise ValueError("Didn't get any text")
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return matches


def split_nodes_image(old_nodes):
    if not old_nodes:
        raise ValueError("No nodes received")
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            images = extract_markdown_images(node)
            if not images:
                new_nodes.append(node)

    return new_nodes


def split_nodes_link(old_nodes):
    pass
