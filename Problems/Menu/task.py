pizza = ["Margarita", "Four Seasons", "Neapoletana", "Vegetarian", "Spicy"]
salad = ["Caesar salad", "Green salad", "Tuna salad", "Fruit salad"]
soup = ["Chicken soup", "Ramen", "Tomato soup", "Mushroom cream soup"]
order = input()
if order == "pizza":
    print(*pizza, sep=", ")
elif order == "salad":
    print(*salad, sep=", ")
elif order == "soup":
    print(*soup, sep=", ")
else:
    print("Sorry, we don't have it in the menu")
