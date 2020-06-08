weight = input("Weight : ")
kg_lbs = input("(L)bs or (K)g : ")

if kg_lbs.upper() == 'L':
    n_weight = 0.45 * float(weight)
    n_units = "Kg"
elif kg_lbs.upper() == 'K':
    n_weight = 2.20 * float(weight)
    n_units = "pounds"
else:
    msg = "Invalid entry"
print(f'You are {n_weight} {n_units}')