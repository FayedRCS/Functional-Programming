def remove_invalid_lines(document):


    #start by formatting the document argument into lines

    lines = document.split("\n")

   #filter out any lines that start with a "-"

    filtered_dash = filter(lambda new: not new.startswith("-"), lines)

    return "\n".join(filtered_dash)
    
    
