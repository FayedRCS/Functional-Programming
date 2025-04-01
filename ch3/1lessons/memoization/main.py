def word_count_memo(document, memos):
    
    memos = memos.copy()

    if document in memos:
        return memos[document], memos

    #getting and storing word count, then updating value

    count_value = word_count(document)

    memos[document] = count_value

    return count_value, memos



# Don't edit below this line


def word_count(document):
    count = len(document.split())
    return count