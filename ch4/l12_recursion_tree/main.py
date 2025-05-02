def list_files(parent_directory, current_filepath=""):

    file_path = []

    for path in parent_directory:
        #create  a new string, can't modify the current_filepath
        new_path = current_filepath + "/" + path

        if parent_directory[path] == None:
            file_path.append(new_path)
        
        else:
            child_directory = list_files(parent_directory[path], new_path)
            file_path.extend(child_directory)

    return file_path
