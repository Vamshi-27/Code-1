command = ""
started = False

while True:
    command = input(">").lower()

    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car Started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car Stopped")
    elif command == "help":
        print("start - to start the car\nstop - to stop the car\nquit - to quit")
    elif command == "quit":
        break
    else:
        print("Sorry, I dont understand the command")