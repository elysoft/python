param = ""
prev = ""

while True:
    param = input("> ").upper()

    if param == "HELP":
        print("""
            start - to start the car
            stop - to stop the car
            quit - to exit
        """)
    elif param == "START":
        if param == prev:
            print("Car already started")
        else:
            print("Car started... Ready to go!")
    elif param == "STOP":
        if param == prev:
            print("Car already stopped")
        else:
            print("Car stopped")
    elif param == "QUIT":
        break
    else:
        print("I don't understand that... ")
    prev = param
