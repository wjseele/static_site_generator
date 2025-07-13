from block_splitter import markdown_to_blocks


def markdown_to_html_node(markdown):
    if not markdown:
        raise ValueError("Didn't receive any input")
    if not isinstance(markdown, str):
        raise ValueError(f"Expected str, got {type(markdown)}")
    markdown_blocks = markdown_to_blocks(markdown)
    for block in markdown_blocks:
        
    pass
