def remove_chunks_as_substring(text, chunks):
    """
    Created for the purpose of removing a chunk from the text
    before researching the text for chunks with 1 fewer word in them
    :param text: original text
    :param chunks: chunks to be removed (generally chunks of a particular length)
    :return: text without chunk
    """
    for chunk in chunks:
        print(chunk)
        text.replace(chunk, "")
    return text