water = 400
milk = 540
coffee_beans = 120
disposal_cups = 9
money = 550


def remaining_action():
    global money, milk, water, coffee_beans, disposal_cups
    print("")
    print("The coffee machine has:")
    print(str(water) + " of water")
    print(str(milk) + " of milk")
    print(str(coffee_beans) + " of coffee beans")
    print(str(disposal_cups) + " of disposable cups")
    print("$" + str(money) + " of money")
    print("")


def exit_action():
    exit()


def read_command():
    global money, milk, water, coffee_beans, disposal_cups
    print("Write action (buy, fill, take, remaining, exit):")
    user_input = str(input())
    if user_input == "buy":
        buy_action()
    elif user_input == "fill":
        fill_action()
    elif user_input == "take":
        take_action()
    elif user_input == "remaining":
        remaining_action()
    elif user_input == "exit":
        exit_action()


def take_action():
    global money
    print("I gave you $" + str(money))
    money = 0


def buy_action():
    global money, milk, water, coffee_beans, disposal_cups
    print("")
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    input_value = input()
    if input_value.isdigit():
        if int(input_value) == 1:
            if water >= 250 and coffee_beans >= 16 and disposal_cups >= 1:
                print("I have enough resources, making you a coffee!")
                water -= 250
                coffee_beans -= 16
                disposal_cups -= 1
                money += 4
            else:
                print(water)
                if water - 250 < 0:
                    print("Sorry, not enough water!")
                elif coffee_beans - 16 < 0:
                    print("Sorry, not enough coffee beans!")
                elif disposal_cups - 1 < 0:
                    print("Sorry, not enough disposable cups!")

        elif int(input_value) == 2:
            if water >= 350 and milk >= 75 and coffee_beans >= 20 and disposal_cups >= 1:
                print("I have enough resources, making you a coffee!")
                water -= 350
                milk -= 75
                coffee_beans -= 20
                disposal_cups -= 1
                money += 7
            else:
                if water - 350 < 0:
                    print("Sorry, not enough water!")
                elif coffee_beans - 20 < 0:
                    print("Sorry, not enough coffee beans!")
                elif milk - 20 < 0:
                    print("Sorry, not enough milk!")
                elif disposal_cups - 1 < 0:
                    print("Sorry, not enough disposable cups!")

        elif int(input_value) == 3:
            if water >= 200 and milk >= 100 and coffee_beans >= 12 and disposal_cups >= 1:
                print("I have enough resources, making you a coffee!")
                water -= 200
                milk -= 100
                coffee_beans -= 12
                disposal_cups -= 1
                money += 6
            else:
                if water - 200 < 0:
                    print("Sorry, not enough water!")
                elif coffee_beans - 12 < 0:
                    print("Sorry, not enough coffee beans!")
                elif milk - 100 < 0:
                    print("Sorry, not enough milk!")
                elif disposal_cups - 1 < 0:
                    print("Sorry, not enough disposable cups!")

    else:
        if input_value == "back":
            print("")
            read_command()
    print()


def fill_action():
    global money, milk, water, coffee_beans, disposal_cups
    print("Write how many ml of water do you want to add:")
    water += int(input())
    print("Write how many ml of milk do you want to add:")
    milk += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    coffee_beans += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    disposal_cups += int(input())


while True:
    read_command()
