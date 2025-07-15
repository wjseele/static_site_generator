import os
import re


def extract_title(markdown):
    if not markdown:
        raise Exception("Didn't get any input")
    title = re.findall(r"^\s*# (?!#)(.*)", markdown)
    if not title:
        raise Exception("Couldn't find any headers in the markdown")
    return title[0]
