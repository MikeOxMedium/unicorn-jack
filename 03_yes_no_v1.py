

# Functions go here...

# checks users enter yes / no for a given question
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer yes / no")


# Main Routine goes here...
show_instructions = yes_no("Have you played this game before ")

print("You chose {}".format(show_instructions))
print()
having_fun = yes_no("Are you having fun? ")
print(f"you said {having_fun} to having fun")

