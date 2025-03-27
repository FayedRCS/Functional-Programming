valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

# Don't edit above this line


def pair_document_with_format(doc_names, doc_formats):
    
    #Zips each element sharing the same indices together and returns a new iterable => tuple
    full_doc = list(zip(doc_names, doc_formats))


    #filters through the full document, and returns each element in the tuple that shares the same file format. hence the "[1]"
    return list(filter(lambda verify: verify[1] in valid_formats, full_doc))




    
