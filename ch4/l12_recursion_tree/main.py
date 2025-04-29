def list_files(parent_directory, current_filepath=""):

    file_path = []

    for path in parent_directory:
        current_filepath += "/" + path

        if parent_directory[path] == None:
            file_path.append(current_filepath)
        elif current_filepath[path]:
            child_directory = list_files(parent_directory[path], current_filepath)
            file_path.extend(child_directory)

    return file_path



test =  {
            "Documents": {
                "Proposal.docx": None,
                "Report": {"AnnualReport.pdf": None, "Financials.xlsx": None},
            } }


print(list_files(test, ""))