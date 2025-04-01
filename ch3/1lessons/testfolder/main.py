def word_count_memo(document, memos):
    memo_copy = memos.copy()

    if document in memos:
        return memos[document]

    return None

# Don't edit below this line


def word_count(document):
    count = len(document.split())
    return count
