# Welcome message with borders
print("-" * 35 + "\nWelcome to Study Hour Calculator\n"+"-" * 35)
# A loop is made
while True:
    # Input for running the program or closing it
    intro = str(input('Write "Enter" to continue or "Close" to close: '))
    # If the option is "Enter" the program continues
    if intro == "Enter" or intro == "enter":
        # Determines if the time inputted is valid
        try:
            # Inputs for study hours and minutes
            goal_hours = int(input("How many study hours do you plan to have today? "))
            goal_minutes = int(input("With how many minutes (if any)? "))
            print()
            # Converts hours to minutes
            conversion = goal_hours * 60
            # Addition of the conversion and minutes, this is now the goal for study hours
            goal = conversion + goal_minutes
            # Input for classes
            classes = int(input("How many classes do you have today? "))
            print()
            # Accumulator for storing the total minutes
            counter = 0
            # A loop runs until it reaches the number of classes that were inputted
            for i in range(1, classes+1):
                print("Class #" + str(i))
                # Inputs for hours and minutes in each class
                hours = int(input("How many hours? "))
                minutes = int(input("How many minutes? "))
                print()
                # Converts hours to minutes
                hours_converted = hours * 60
                # Adds converted hours and minutes
                total_minutes = hours_converted + minutes
                # The accumulator stores the total minutes
                counter += total_minutes
            # Subtracts the goal and counter
            total = goal - counter
            # Divides the remaining minutes by 60
            hours = total // 60
            subtract = hours * 60
            # To get minutes you subtract the remaining time and hours converted into minutes
            minutes = total - subtract
            # If the remaining time is negative or 0, this means you have no time for studying
            if total <= 0:
                print("You have no spare time.")
            # If it is greater than zero, the available study time gets printed
            else:
                print("You have", hours, "hours and", minutes, "minutes for studying.")
        # If in any moment there is an invalid time inputted, the program goes to Enter and Close message
        except ValueError:
            print("Invalid time")
            continue
    # If the option is Close, the program stops
    elif intro == "Close" or intro == "close":
        print("\nSee you next time!")
        break
    # If someone inputs something other than Enter or Close, the message prints again
    else:
        continue
