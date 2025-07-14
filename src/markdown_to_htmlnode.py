from block_splitter import markdown_to_blocks
from htmlnode import ParentNode, LeafNode
from textnode import TextNode, TextType
from blocknode import block_to_block_type, BlockType
from delimiter import split_nodes_delimiter
from extractor import split_nodes_image, split_nodes_link


def markdown_to_html_node(markdown):
    if not markdown:
        raise ValueError("Didn't receive any input")
    if not isinstance(markdown, str):
        raise ValueError(f"Expected str, got {type(markdown)}")
    markdown_blocks = markdown_to_blocks(markdown)
    for block in markdown_blocks:
        if block_to_block_type(block) is BlockType.PARAGRAPH:
            block = paragraph_to_textnodes(block)
            block = paragraph_to_htmlnodes(block)
    # return html_output


def paragraph_to_textnodes(block):
    lines = TextNode(block, TextType.TEXT)
    lines = split_nodes_delimiter(lines, "**", TextType.BOLD)
    lines = split_nodes_delimiter(lines, "_", TextType.ITALIC)
    lines = split_nodes_delimiter(lines, "`", TextType.CODE)
    lines = split_nodes_image(lines)
    lines = split_nodes_link(lines)
    return lines


def paragraph_to_htmlnodes(block):
    pass
