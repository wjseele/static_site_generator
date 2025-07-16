import os
import shutil
import sys
from generator import generate_pages_recursive


def main():
    if len(sys.argv) < 2:
        basepath = "/"
    else:
        basepath = sys.argv[1]
    source = os.path.join(os.getcwd(), "static")
    if not check_path(source):
        raise Exception(f"Couldn't find a source path at {source}")
    destination = os.path.join(os.getcwd(), "docs")
    copy_log = copy_source_files_to_destination(source, destination)
    generate_pages_recursive("content", "template.html", "docs", basepath)
    for entry in copy_log:
        print(entry)


def check_path(path):
    return os.path.exists(path)


def clean_path(destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    return


def create_path(destination):
    clean_path(destination)
    os.mkdir(destination)
    return


def get_folder_contents(source):
    contents = os.listdir(source)
    return contents


def copy_source_files_to_destination(source, destination):
    if not check_path(destination):
        create_path(destination)
    contents = get_folder_contents(source)
    copy_log = []
    for content in contents:
        source_path = os.path.join(source, content)
        destination_path = os.path.join(destination, content)
        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
            copy_log.append(f"Copied {source_path} to {destination_path}")
        elif os.path.isdir(source_path):
            copy_log.extend(
                copy_source_files_to_destination(source_path, destination_path)
            )
    return copy_log


if __name__ == "__main__":
    main()
