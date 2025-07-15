import os
import re
from markdown_to_htmlnode import markdown_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode


def extract_title(markdown):
    if not markdown:
        raise Exception("Didn't get any input")
    title = re.findall(r"^\s*# (?!#)(.*)", markdown)
    if not title:
        raise Exception("Couldn't find any headers in the markdown")
    return title[0]


def generate_page(from_path, template_path, dest_path):
    if not from_path or not template_path or not dest_path:
        raise Exception(f"I'm missing one of {from_path, template_path, dest_path}")
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    source = os.path.join(os.getcwd(), from_path)
    template = os.path.join(os.getcwd(), template_path)
    destination = os.path.join(os.getcwd(), dest_path)
    source_contents = file_opener(source)
    template_contents = file_opener(template)
    title = extract_title(source_contents)
    source_html = markdown_to_html_node(source_contents).to_html
    template_contents = template_contents.replace("{{ Title }}", title)
    template_contents = template_contents.replace("{{ Content }}", source_html)
    file_writer(destination, template_contents)
    return


def file_opener(path_to_file):
    if not os.path.isfile(path_to_file):
        raise Exception(f"Couldn't find the file at {path_to_file}")
    with open(path_to_file) as content_file:
        file_contents = content_file.read()
    if not content_file.closed:
        print("File had to be closed explictly")
        content_file.close()
    return file_contents


def file_writer(path_to_file, contents):
    if not os.path.dirname(path_to_file):
        os.makedirs(os.path.dirname(path_to_file))
    with open(path_to_file, "w") as page:
        page.write(contents)
    return
