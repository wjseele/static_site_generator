def markdown_to_blocks(markdown):
    if not markdown:
        raise ValueError("Didn't receive any input")
    blocks = markdown.split("\n\n")
    for i in range(0, len(blocks)):
        blocks[i] = blocks[i].strip()
        lines = [line.strip() for line in blocks[i].split("\n")]
        blocks[i] = "\n".join(lines)
    blocks = [block for block in blocks if (block)]
    return blocks
