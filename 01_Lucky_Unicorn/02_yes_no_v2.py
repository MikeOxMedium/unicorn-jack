show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask the user if they have played before
    show_instructions = input("have you play this game before? ").lower()

    # If they say yes, output 'program continues'
    # If they say no, output 'display instruction'
    # If they answer is invalid, print an error.

    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("program continues")

    elif show_instructions == "no" or show_instructions == "n":
        print("display instructions")

    # If they say no, output 'display instructions'
    else:
        print("Please answer yes / no")
