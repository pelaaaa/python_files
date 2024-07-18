def unzipFiles(path):
    '''
    Unzips every ZIP file in a directory. Takes the path to the directory.
    ZIP files are unzipped into the inital directory.
    '''
    import os
    from zipfile import ZipFile

    zip_list = []
    os.chdir(path)
    dir_list = os.listdir()
    
    print("Files and directories in '", path, "':", dir_list)
    for item in os.listdir():
        if item.endswith(".zip"):
            zip_list.append(item)
        else:
            continue

    for item in zip_list:
        name = item.replace(".zip", "")
        new_dir = os.path.join(path, name)

        try:
            os.mkdir(new_dir)
        except FileExistsError:
            print(f"'{new_dir}' already exists as a directory.")
        
        with ZipFile(item, 'r') as zip_file:
            zip_file.extractall(new_dir)

    print("\nAll ZIP files unzipped.\n")

