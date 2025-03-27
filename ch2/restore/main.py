def restore_documents(originals, backups):

    #easy to get tricked by not concatenating both tuple arguments. concatinate them, then map over to uppercase.
    #Then we filter through returning only if True to NOT being a digit
    
    return set(filter(lambda digit: not digit.isdigit(), map(lambda upp: upp.upper(), originals + backups)))


