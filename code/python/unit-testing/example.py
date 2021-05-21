from name import formatted_name

print("Please enter the first and last names or enter x to E[x]it.")

while True:
    first_name = input("Please enter first name: ")
    if first_name == "x":
        print("Good bye")
        break

    last_name = input("Please enter last name: ")
    if last_name == "x":
        print("Good bye")
        break

    result = formatted_name(first_name, last_name)
    print("Formatted name is: " + result + ".")
