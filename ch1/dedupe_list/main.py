def deduplicate_lists(lst1, lst2, reverse=False):
    
    no_dupes = []

    for i in lst2:
        if i not in lst1:
            no_dupes.append(i)
    
    for i in lst1:
        no_dupes.append(i)
    
    if reverse == True:
        return sorted(no_dupes, reverse=True)
        
    
    return sorted(no_dupes)

    

        
    
