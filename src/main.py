import os
import shutil


def __main__():
    source = "../static"
    destination = "../public"
    create_public(destination)
    copy_log = copy_source_files_to_destination(source, destination)
    print(copy_log)


def check_paths(source, destination):
    return os.path.exists(source) and os.path.exists(destination)


def clean_public(destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
        print(f"Removed {destination}")
    return


def create_public(destination):
    clean_public(destination)
    os.mkdir(destination)
    print(f"Created {destination}")
    return


def get_folder_contents(source):
    contents = os.listdir(source)
    return contents


def copy_source_files_to_destination(source, destination):
    if not check_paths(source, destination):
        raise Exception(
            f"Couldn't find source at {source} and destination at {destination}"
        )
    contents = get_folder_contents(source)
    copy_log = []
    for content in contents:
        source_path = os.path.join(source, content)
        destination_path = os.path.join(destination, content)
        if os.path.isfile:
            shutil.copy(source_path, destination_path)
            print(f"Copied {source_path} to {destination_path}")
            copy_log.append(f"Copied {source_path} to {destination_path}")
        elif os.path.isdir:
            copy_source_files_to_destination(source_path, destination_path)
    return copy_log


__main__()
