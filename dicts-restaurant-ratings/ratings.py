"""Restaurant rating lister."""
import sys

#define a function that stores the ratings for restaurants
def stores_ratings(file_name):
    """Put Restaurants in alph order"""

    #open the file and name it data
    data = open(file_name)

    #create an empty dictionary
    dict = {}

    #use a for loop to loop through each in data
    for line in data:

        #create a list of the restaurant and ratings
        #by removing the trailing spaces
        #name_n_rate is the list of restaurants and their ratings
        name_n_rate = line.strip().split(":")

        #adding to the blank dictionary
        #name_n_rate[0] is the first element of the list - the restaurants
        #name_n_rate[1] is the rating of the restaurant
        #int converts the string rating to a number
        dict[name_n_rate[0]] = int(name_n_rate[1])
   
    #sort the dictionary in alphabetical order by the keys
    keys_sorted = sorted(dict)

    #Loop through the dictionary of sorted restaurants
    for key in keys_sorted:

        #use dict[key] to find the rating associated with that restaurant
        value = dict[key]
        
        #print the restaurant and its rating
        print(f"{key} is rated at {value}.")

        


def adding_ratings(file_name):
    """add a restaurant and its rating"""


    data = open(file_name)
    dict = {}
    
    for line in data:
        name_n_rate = line.strip().split(":")
        dict[name_n_rate[0]] = int(name_n_rate[1])
    
    new_restaurant=input("Please enter your favorite retaurant's name: ")
    new_rating=input("Please enter your rating of this restaurant: ")
    
    if dict.get(new_restaurant) == None:
        dict[new_restaurant]=int(new_rating)
    
    else:
        print("Warning: this restaurant already exists! Your rating will be ignored")

    keys_sorted = sorted(dict)
    for key in keys_sorted:
        value = dict[key]
        print(f"{key} is rated at {value}.")


##program starts running here###

input_file = sys.argv[1]

while True:
    print("here are your choices")
    print("seeing all rating ------ 1")
    print("adding new restaurant -- 2")
    print("quit and do nothing ---- 3")


    choice = int(input(">"))

    if choice ==1:
        stores_ratings(input_file)
    elif choice==2:
        adding_ratings(input_file)
    elif choice==3:
        break
    else:
        print("Your choice is invalid.")

