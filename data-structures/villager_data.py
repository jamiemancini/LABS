"""Functions to parse a file containing villager data."""

def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    #open the file
    villager_data = open(filename)

    #create an empty set named species
    species=set()

    #create a for loop to iterate through each line
    for line in villager_data:

        #create a list called person that has the information stated for each person
        person = (line.split("|"))

        #add the element at index[1] which is the species to the empty set
        species.add(person[1])

    return species

all_species("villagers.csv")

def get_villagers_by_species(filename, search_string):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    #open the file
    villager_data = open(filename)

    #create an empty list
    villagers = []

    #create a for loop to iterate through each line
    for line in villager_data:

        #create a list called person that has the information stated for each person
        person = (line.split("|"))
        species = person[1]
        name = person[0]

    
        if species == search_string:
            villagers.append(name)
            
    print(sorted(villagers))
    return sorted(villagers)
    
    

get_villagers_by_species("villagers.csv", "Pig")


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code

    return []


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
