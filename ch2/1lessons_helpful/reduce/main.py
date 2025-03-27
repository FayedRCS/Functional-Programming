import functools


def join(doc_so_far, sentence):
    return doc_so_far + ". " + sentence


def join_first_sentences(sentences, n):

    if n == 0:
        return ""

    #Using list slicing to stop itterating after the designered integer is reached.
    joint = functools.reduce(join, sentences[:n])
    return joint + "."
