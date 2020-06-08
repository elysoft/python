dic = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero",
}
no = input("Enter your phone no: ")
fno = ""
for i in no:
    fno += dic.get(i) + " "
print(f"No : {fno}")
