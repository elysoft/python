numbers = [2, 2, 4, 6, 3, 4, 6, 1]
print(len(numbers))
for i in numbers:
    nbr = numbers.count(i)
    if nbr > 1:
        numbers.remove(i)
    print(f"i : {i} nbr: {nbr} list {numbers}")

print(numbers)
