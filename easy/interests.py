def interests(month, amount):
    deposit = 0
    for i in range(month):
        print(deposit, deposit*0.22/12)
        deposit = deposit + amount + deposit*0.22/12

    return deposit


a = interests(24, 1.7)

print(a)