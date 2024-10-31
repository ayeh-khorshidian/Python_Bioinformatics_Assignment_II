# Bioinformatics_Assignment.py

# Task 1: if-elif-else statements
def calculate_weight():
    mass = float(input("Enter the object's mass in kilograms: "))
    weight = mass * 9.8
    print(f"Calculated weight: {weight} Newtons")

    if weight > 1000:
        print("The object is too heavy.")
    elif weight < 10:
        print("The object is too light.")
    else:
        print("The object is just the right weight!")


# Task 2: while loop – input validation
def validate_number():
    while True:
        number = int(input("Enter a number between 1 and 100: "))
        if 1 <= number <= 100:
            print(f"Number is: {number}")
            break
        else:
            print("Number is out of range. Please try again.")


# Task 3: Loops practice
def bug_collector():
    total_bugs = 0
    for day in range(1, 8):  # 7 days
        bugs = int(input(f"Enter the number of bugs collected on day {day}: "))
        total_bugs += bugs
    print(f"Total number of bugs collected: {total_bugs}")


# Task 4: Creating a list
def create_list():
    amino_acids = ["Try", "Asp", "Lys", "Met"]
    print("Complete list of amino acids:", amino_acids)
    print("Amino acids individually:")
    for acid in amino_acids:
        print(acid)


# Task 5: List functions
def list_functions():
    amino_acids = ["Try"
