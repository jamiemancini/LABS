"""Restaurant rating lister."""
import sys

# put your code here
def stores_ratings(file_name):
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

stores_ratings(sys.argv[1])