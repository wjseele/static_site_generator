from enum import Enum, auto


class BlockType(Enum):
    PARAGRAPH = auto()
    HEADING = auto()
    CODE = auto()
    QUOTE = auto()
    UNORDERED_LIST = auto()
    ORDERED_LIST = auto()


def block_to_block_type(block):
    if not block:
        raise ValueError("Didn't receive any input")
    if not isinstance(block, str):
        raise ValueError("This function only takes a single string")
    headings = ("# ", "## ", "### ", "#### ", "##### ", "###### ")
    if block.startswith(headings):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        return quote_checker(block)
    if block.startswith("- "):
        return unordered_list_checker(block)
    if block.startswith("1. "):
        return ordered_list_checker(block)
    return BlockType.PARAGRAPH


def quote_checker(block):
    lines = block.split("\n")
    for line in lines:
        if not line.startswith(">"):
            return BlockType.PARAGRAPH
    return BlockType.QUOTE


def unordered_list_checker(block):
    lines = block.split("\n")
    for line in lines:
        if not line.startswith("- "):
            return BlockType.PARAGRAPH
    return BlockType.UNORDERED_LIST


def ordered_list_checker(block):
    lines = block.split("\n")
    for i in range(0, len(lines)):
        if not lines[i].startswith(f"{i + 1}. "):
            return BlockType.PARAGRAPH
    return BlockType.ORDERED_LIST
