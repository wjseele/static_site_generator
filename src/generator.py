import os
import re
from markdown_to_htmlnode import markdown_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode
import html


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
    source_contents = file_opener(from_path)
    template_contents = file_opener(template_path)
    title = extract_title(source_contents)
    source_html = markdown_to_html_node(source_contents).to_html()
    template_contents = template_contents.replace("{{ Title }}", title)
    template_contents = template_contents.replace("{{ Content }}", source_html)
    template_contents = html.unescape(template_contents)
    file_writer(dest_path, template_contents)
    return


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not dir_path_content or not template_path or not dest_dir_path:
        raise Exception(
            f"I'm missing one of {dir_path_content, template_path, dest_dir_path}"
        )
    print(
        f"Generating page from {dir_path_content} to {dest_dir_path} using {template_path}"
    )
    if not check_path(dest_dir_path):
        create_path(dest_dir_path)
    contents = get_folder_contents(dir_path_content)
    for content in contents:
        source_path = os.path.join(dir_path_content, content)
        destination_path = os.path.join(dest_dir_path, content)
        if os.path.isfile(source_path):
            source_contents = file_opener(source_path)
            template_contents = file_opener(template_path)
            title = extract_title(source_contents)
            source_html = markdown_to_html_node(source_contents).to_html()
            template_contents = template_contents.replace("{{ Title }}", title)
            template_contents = template_contents.replace("{{ Content }}", source_html)
            template_contents = html.unescape(template_contents)
            file_writer(dest_dir_path, template_contents)
        elif os.path.isdir(source_path):
            generate_pages_recursive(source_path, template_path, destination_path)
    return


def get_folder_contents(source):
    contents = os.listdir(source)
    return contents


def check_path(path_to_check):
    return os.path.exists(path_to_check)


def create_path(destination):
    os.mkdir(destination)
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
