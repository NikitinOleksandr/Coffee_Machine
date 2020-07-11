summ = 0
sqr_summ = 0
number = int(input())
summ += number
sqr_summ += number ** 2
while summ != 0:
    number = int(input())
    summ += number
    sqr_summ += number ** 2
else:
    print(sqr_summ)



