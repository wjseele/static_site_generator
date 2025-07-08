import re

from textnode import TextNode, TextType


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
            images = extract_markdown_images(node.text)
            if not images:
                new_nodes.append(node)
            else:
                block = []
                block = node_image_splitter(node.text, block, images)
                new_nodes.extend(block)

    return new_nodes


def node_image_splitter(node, block, images):
    sections = node.split(f"![{images[0][0]}]({images[0][1]})", 1)
    if len(sections[0]) > 0:
        block.append(TextNode(sections[0], TextType.TEXT))
    block.append(TextNode(images[0][0], TextType.IMAGE, images[0][1]))
    if len(images) > 1:
        block = node_image_splitter(sections[1], block, images[1:])
    else:
        if len(sections[1]) > 0:
            block.append(TextNode(sections[1], TextType.TEXT))
            return block
    return block


def split_nodes_link(old_nodes):
    if not old_nodes:
        raise ValueError("No nodes received")
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            links = extract_markdown_links(node.text)
            if not links:
                new_nodes.append(node)
            else:
                block = []
                block = node_link_splitter(node.text, block, links)
                new_nodes.extend(block)

    return new_nodes


def node_link_splitter(node, block, links):
    sections = node.split(f"[{links[0][0]}]({links[0][1]})", 1)
    if len(sections[0]) > 0:
        block.append(TextNode(sections[0], TextType.TEXT))
    block.append(TextNode(links[0][0], TextType.LINK, links[0][1]))
    if len(links) > 1:
        block = node_link_splitter(sections[1], block, links[1:])
    else:
        if len(sections[1]) > 0:
            block.append(TextNode(sections[1], TextType.TEXT))
            return block
    return block
