from block_splitter import markdown_to_blocks
from htmlnode import ParentNode, LeafNode
from textnode import TextNode, TextType
from blocknode import block_to_block_type, BlockType, unordered_list_checker
from delimiter import split_nodes_delimiter
from extractor import split_nodes_image, split_nodes_link


def markdown_to_html_node(markdown):
    if not markdown:
        raise ValueError("Didn't receive any input")
    if not isinstance(markdown, str):
        raise ValueError(f"Expected str, got {type(markdown)}")
    markdown_blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in markdown_blocks:
        if block_to_block_type(block) == BlockType.PARAGRAPH:
            html_nodes.append(paragraph_to_htmlnodes(block))
        if block_to_block_type(block) == BlockType.HEADING:
            html_nodes.append(heading_to_htmlnode(block))
        if block_to_block_type(block) == BlockType.CODE:
            html_nodes.append(code_to_htmlnode(block))
        if block_to_block_type(block) == BlockType.QUOTE:
            html_nodes.append(quote_to_htmlnode(block))
        if block_to_block_type(block) == BlockType.UNORDERED_LIST:
            html_nodes.append(unordered_list_to_htmlnode(block))
        if block_to_block_type(block) == BlockType.ORDERED_LIST:
            html_nodes.append(ordered_list_to_htmlnode(block))
    return ParentNode("div", html_nodes)


def paragraph_to_textnodes(block):
    lines = TextNode(" ".join(block.split("\n")), TextType.TEXT)
    lines = split_nodes_delimiter([lines], "**", TextType.BOLD)
    lines = split_nodes_delimiter(lines, "_", TextType.ITALIC)
    lines = split_nodes_delimiter(lines, "`", TextType.CODE)
    lines = split_nodes_image(lines)
    lines = split_nodes_link(lines)
    return lines


def paragraph_to_htmlnodes(block):
    to_html = paragraph_to_textnodes(block)
    texttypes_dict = {
        TextType.TEXT: None,
        TextType.BOLD: "b",
        TextType.ITALIC: "i",
        TextType.CODE: "code",
        TextType.LINK: "a",
        TextType.IMAGE: "img",
    }
    new_leaves = []
    for element in to_html:
        new_leaves.append(
            LeafNode(texttypes_dict[element.text_type], element.text, element.url)
        )
    return ParentNode("p", new_leaves, None)


def heading_to_htmlnode(block):
    heading_level = block.count("#")
    return LeafNode(f"h{heading_level}", block.lstrip("# "))


def code_to_htmlnode(block):
    return ParentNode(
        "pre",
        [LeafNode("code", block.removeprefix("```").removesuffix("```").lstrip())],
    )


def quote_to_htmlnode(block):
    return LeafNode("blockquote", block.removeprefix("> "))


def unordered_list_to_htmlnode(block):
    unordered_list = list_splitter(block)
    return ParentNode("ul", unordered_list)


def ordered_list_to_htmlnode(block):
    ordered_list = list_splitter(block)
    return ParentNode("ol", ordered_list)


def list_splitter(block):
    split_list = block.split("\n")
    return_list = []
    for item in split_list:
        return_list.append(
            LeafNode("li", item.removeprefix("-").lstrip("0123456789.").lstrip())
        )
    return return_list
