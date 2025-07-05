from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if delimiter is None or delimiter == "":
        raise Exception("No delimiter specified")
    if text_type is TextType.TEXT:
        raise Exception("Specify a desired text type")
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            block = node.text.split(delimiter)
            if len(block) % 2 == 0:
                raise Exception("Could not find closing delimiter")
            for text in range(len(block)):
                if text == 1:
                    block[text] = TextNode(block[text], text_type)
                else:
                    block[text] = TextNode(block[text], TextType.TEXT)
            new_nodes.extend(block)
    return new_nodes
