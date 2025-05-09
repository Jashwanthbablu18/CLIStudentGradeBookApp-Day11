# Day 11 - Student Gradebook App
# Topic: Dictionaries

# This Function to represent introduction of this assignment / Project. Starting with a little welcome message.
def show_intro():
    print("📘 Welcome to Day 11 of Python 30-Day Challenge!")
    print("🔹 Topic: Dictionaries")
    print("🧑‍🎓 Building a Gradebook to manage student scores\n")


# This is a gradebook named dictionary holds name of the student with marks list, Format: { "name": [marks] }
gradebook = { }

# This function displays the menu.
def show_menu():
    print("\n📋 Gradebook Menu:")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. View All Students")
    print("5. Calculate Average")
    print("6. Exit")

# This function adds a student into the gradebook dictionary.
def add_student():

    # This asks user for input the student name, then removes extra spaces and stores it in student variable. 
    student = input("👨‍🎓 Enter student name: ").strip()

    # This asks user for input the marks, then removes extra spaces and stores it in raw_marks variable.
    raw_marks = input("✍️ Enter marks separated by commas (e.g. 85,90,78): ").strip()

    # this tries to add the marks into marks[ ] by separating each value with ',' and then this aligns the marks to the student.
    try:
        marks = [int(mark.strip()) for mark in raw_marks.split(",")]
        gradebook[student] = marks
        print(f"✅ Added {student} with marks: {marks}")

    # If above block fails then it throws this msg.
    except ValueError:
        print("❌ Oops! Make sure all marks are numbers.")

# This function updates the student marks
def update_marks():

    # Takes student name as input to update, removes extra spaces by .strip()
    student = input("🔁 Enter student name to update: ").strip()

    # If the student is present in gradebook dictionary, then below code executes.
    if student in gradebook:

        # Takes new marks as input with comma separated and removes extra spaces by .strip()
        new_input = input("📥 Enter new marks (comma-separated): ").strip()

        # This tries to add updated marks list (new_input) of a student who is present in gradebook.
        try:
            gradebook[student] = [int(score.strip()) for score in new_input.split(",")]
            print(f"✅ Updated marks for {student}: {gradebook[student]}")

        # If the user enters invalid marks this will be displayed
        except ValueError:
            print("❌ Couldn't update. Please enter valid numbers.")

    # If student doesn't found this will be displayed.
    else:
        print("❌ Student not found.")

# This function is used to delete the student
def delete_student():

    # takes target student name as an input
    target = input("🗑️ Enter student name to delete: ").strip()

    # If the targeted student is in the gradebook dictionary, then delete that targeted student from the dictionary.
    if target in gradebook:
        del gradebook[target]
        print(f"✅ Deleted record for {target}")

    # If targeted student doesn't found display this msg.
    else:
        print("❌ Student not found.")

# This function is used to view all the students who are present in the gradebook dictionary
def view_all():

    # If the gradebook dictionary is empty display this msg.
    if not gradebook:
        print("📭 No student records yet.")

    # If the gradebook dictionary has student names with marks then display them by looping over the dictionary
    else:
        print("\n📚 Student Records:")
        for name, scores in gradebook.items():
            print(f"{name}: {scores}")

# This function is used to calculate the average marks of a student
def calculate_average():

    # Takes student name as an input to calculate avg and removes extra spaces.
    student = input("📊 Enter student name for average calculation: ").strip()

    # If the given student is exist, then calculate the avg of that student and display it
    if student in gradebook:
        scores = gradebook[student]

        # if there are marks found for that student then calculate avg
        if scores:
            average = sum(scores) / len(scores)
            print(f"🎯 Average marks for {student}: {average:.2f}")

        # if the student found but no marks are there then display this.
        else:
            print("⚠️ No marks found for this student.")

    # If the given student isn't found the display this.
    else:
        print("❌ Student not found.")


# main
def main():

    # calls show_intro() to display introduction and welcome msg
    show_intro()

    # This loop runs until it breaks(user chooses to exit)
    while True:
        show_menu()

        # Taking user's choice to perform operation
        choice = input("🔢 Choose an option (1-6): ").strip()
        
        # If user choice is 1 then it adds a new student into gradebook dictionary.
        if choice == "1":
            add_student()
        
        # If user choice is 2 then it updates the existing student marks in gradebook dictionary.
        elif choice == "2":
            update_marks()
        
        # If user choice is 3 then it deletes the specified student from gradebook dictionary.
        elif choice == "3":
            delete_student()

        # If user choice is 4 then it displays all students who are in gradebook dictionary.
        elif choice == "4":
            view_all()

        # If user choice is 5 then it calculates average of student in gradebook dictionary.
        elif choice == "5":
            calculate_average()

        # If user choice is 6 then it exits from gradebook app.
        elif choice == "6":
            print("👋 Exiting Gradebook App...")
            break

        # If user chooses invalid option then display this msg.
        else:
            print("❌ Invalid option. Try a number between 1 and 6.")

# starting point
if __name__ == "__main__":
    main()
