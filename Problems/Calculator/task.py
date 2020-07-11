first_number = float(input())
second_number = float(input())
operations = str(input())
if second_number == 0 and (operations == "/" or operations == "mod" or operations == "div"):
    print("Division by 0!")
elif operations == "+":
    print(first_number + second_number)
elif operations == "-":
    print(first_number - second_number)
elif operations == "/":
    print(first_number / second_number)
elif operations == "*":
    print(first_number * second_number)
elif operations == "mod":
    print(first_number % second_number)
elif operations == "pow":
    print(first_number ** second_number)
elif operations == "div":
    print(first_number // second_number)
