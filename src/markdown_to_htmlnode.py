from block_splitter import markdown_to_blocks
from htmlnode import ParentNode, LeafNode
from textnode import TextNode, TextType
from blocknode import block_to_block_type, BlockType
from delimiter import split_nodes_delimiter
from extractor import split_nodes_image, split_nodes_link
from text_to_html import text_node_to_html_node


def markdown_to_html_node(markdown):
    if not markdown:
        raise ValueError("Didn't receive any input")
    if not isinstance(markdown, str):
        raise ValueError(f"Expected str, got {type(markdown)}")
    markdown_blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            html_nodes.append(paragraph_to_htmlnodes(block))
        elif block_type == BlockType.HEADING:
            html_nodes.append(heading_to_htmlnode(block))
        elif block_type == BlockType.CODE:
            html_nodes.append(code_to_htmlnode(block))
        elif block_type == BlockType.QUOTE:
            html_nodes.append(quote_to_htmlnode(block))
        elif block_type == BlockType.UNORDERED_LIST:
            html_nodes.append(unordered_list_to_htmlnode(block))
        elif block_type == BlockType.ORDERED_LIST:
            html_nodes.append(ordered_list_to_htmlnode(block))
    return ParentNode("div", html_nodes)


def content_to_textnodes(block):
    lines = TextNode(block, TextType.TEXT)
    lines = split_nodes_delimiter([lines], "**", TextType.BOLD)
    lines = split_nodes_delimiter(lines, "_", TextType.ITALIC)
    lines = split_nodes_delimiter(lines, "`", TextType.CODE)
    lines = split_nodes_image(lines)
    lines = split_nodes_link(lines)

    new_leaves = []
    for element in lines:
        new_leaves.append(text_node_to_html_node(element))
    return new_leaves


def paragraph_to_htmlnodes(block):
    content = content_to_textnodes(block)
    return ParentNode("p", content)


def heading_to_htmlnode(block):
    heading_level = block.count("#")
    content = content_to_textnodes(block.lstrip("# "))
    return ParentNode(f"h{heading_level}", content)


def code_to_htmlnode(block):
    return ParentNode(
        "pre",
        [LeafNode("code", block.removeprefix("```").removesuffix("```").lstrip("\n"))],
    )


def quote_to_htmlnode(block):
    return ParentNode(
        "blockquote",
        content_to_textnodes(
            "\n".join(line.removeprefix("> ") for line in block.split("\n"))
        ),
    )


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
            ParentNode(
                "li",
                content_to_textnodes(
                    item.removeprefix("-").lstrip("0123456789.").lstrip()
                ),
            )
        )
    return return_list
