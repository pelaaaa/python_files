def fileSurfing(path, file_list):
    '''
    Goes through a directory and subdirectories to find desired file types.
    Returns a list of all found files.

    Arguments:
    -path: the file path to the desired root directory.
    -file_list: list of file types desired. EX: [".pdf", ".shp"]
    '''
    import os

    the_sauce = []

    toppings = [(root, dirs, files) for root, dirs, files in os.walk(path)]

    surf = listSurfing(toppings)
    
    for topping in toppings:
        tpl = list(topping)
        pizza = listSurfing(tpl)
            
        for file_type in file_list:
            for pepperoni in pizza:
                if pepperoni.endswith(file_type):
                    cheese = pizza[0]
                    salami = os.path.join(cheese, pepperoni)

                    if salami not in the_sauce:
                        the_sauce.append(salami)

    print("Found files and directories: ", the_sauce)
    return the_sauce


    


def listSurfing(lst, empty=None):
    if empty is None:
        empty = []

    for item in lst:
        if isinstance(item, list):
            listSurfing(item, empty)
        elif isinstance(item, tuple):
            tpl = list(item)
            listSurfing(tpl, empty)
        else:
            empty.append(item)
            
    return empty


