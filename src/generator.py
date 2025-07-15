import os
import re


def extract_title(markdown):
    if not markdown:
        raise Exception("Didn't get any input")
    title = re.findall(r"(#+ [a-zA-Z]+)", markdown)
    if not title:
        raise Exception("Couldn't find any headers in the markdown")
    if title[0].count("#") != 1:
        raise Exception("Couldn't find an h1 in the markdown")
    return title[0].strip("# ")
