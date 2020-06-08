name = input("What is your name ? ")
name_len = len(name)
if name_len < 3:
    msg = "Name must be at least 3 characters"
elif name_len > 50:
    msg = "Name can be a maximum of 50 characters"
else:
    msg = "Name looks good"
print(msg)
