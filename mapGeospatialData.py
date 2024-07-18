def mapGeospatialData(path, interactive=True):
    '''
    Download a ZIP file and map the geospatial data. Function unzips all
    ZIP files in the directory and visualizes the data on a map. Maps can
    be interactive or static.
    Looks for .SHP and .GDB files to map.
    Uses the unzipFiles and fileSurfing modules.

    ARGUMENTS
    -path: file path to the desired root directory.
    -keyword argument "interactive": if set to True, creates interactive maps.
    '''
    from unzipFiles import unzipFiles as unzip
    from fileSurfing import fileSurfing, listSurfing
    import os
    import geopandas as geo
    import matplotlib.pyplot as plt
    import webbrowser

    os.chdir(path)
    unzip(path)
    files = os.listdir()
    print("Files in directory: ", files, "\n")

    file_list = [".shp", ".gdb"]
    m = fileSurfing(path, file_list)

    if interactive:
        print("\nMaps will be interactive\n")
        for item in m:
            for file_type in file_list:
                if item.endswith(file_type):
                    name = item.replace(file_type, "")
                
            lyr = geo.read_file(item)
            html = rf"{name}.html"

            leaflet = lyr.explore()
            leaflet.save(html)

            webbrowser.open(html)
            
    else:
        print("\nMaps will not be interactive.\n")
        for item in m:
            lyr = geo.read_file(item)

            lyr.plot()
            plt.show()

    os.chdir(path)

    for item in os.listdir():
        if ".html" in item:
            os.remove(item)

    print("\nTask complete.")

