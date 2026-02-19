# Program Name: Assignment2.py
# Course: IT3883 / Section (put your section)
# Student Name: Tosin Olabanji
# Assignment Number: Assignment 2
# Due Date: 2/18/2026
# Purpose: This program reads student names and scores from a file,
# calculates each student's average, and prints the results in
# descending order by average grade.
# Resources Used: Class notes and instructor instructions.


# Create an empty list to store student data
students = []

# Open the input file for reading
with open("Assignment2input.txt", "r") as file:
    # Read each line in the file
    for line in file:
        # Split the line into parts
        parts = line.split()

        # First item is the student name
        name = parts[0]

        # The rest are scores
        scores = parts[1:]

        # Calculate total score
        total = 0
        for score in scores:
            total += int(score)

        # Calculate average
        average = total / len(scores)

        # Add name and average to list
        students.append((name, average))


# Sort the list by average in descending order
students.sort(key=lambda x: x[1], reverse=True)


# Print results formatted to 2 decimal places
for student in students:
    print(student[0], format(student[1], ".2f"))
