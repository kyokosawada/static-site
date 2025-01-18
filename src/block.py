def markdown_to_blocks(markdown):
    string_list = markdown.split("\n\n")
    result = []
    for string in string_list:
        stripped = string.strip()
        if stripped:
            result.append(stripped)
    return result
