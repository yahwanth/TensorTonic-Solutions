def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    chunked_list = []
    i = 0
    while i < len(tokens):
        if i + overlap >= len(tokens):       
            break
        chunked_list.append(tokens[i : (i + chunk_size)])
        i = (i + chunk_size) - overlap
    return chunked_list
        