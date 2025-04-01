def remove_emphasis_from_word(word):
    #here we strip words from astrixes
    return word.strip("*")


def remove_emphasis_from_line(line):
    #split lines into words, maps them using the remove-from-word func, then joins it back together
    words = line.split(" ")
    new_words = map(remove_emphasis_from_word, words)
    joined = " ".join(new_words)
    return joined


def remove_emphasis(doc_content):
    #same process as above, splitting the document into lines and maps over so we can remove emphasises from lines. then join
    lines = doc_content.split("\n")
    mapped = map(remove_emphasis_from_line, lines)
    joined = "\n".join(mapped)
    return joined
