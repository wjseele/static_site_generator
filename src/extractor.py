import re


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
