scores = input().split()
C = 0
I = 0
for score in scores:
    if score == "C":
        C += 1
    elif score == "I":
        I += 1
        if I == 3:
            print("Game over")
            print(C)
            break
else:
    print("You won")
    print(C)
