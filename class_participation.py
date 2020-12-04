#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on December 2020
# This program calculates the attendance and decides if
#       a student is eligible to take the exam


def main():
    # this function calculates attendance and compares to minimum required

    print("This program decides if you can partake in the exam")
    print("")

    # input
    num_classes_held = int(input("Enter the number of classes held: "))
    num_classes_attend = int(input("Enter the number of classes you"
                                   " attended: "))
    print("")

    # process

    # calculating attendance
    attendance = (num_classes_attend / num_classes_held) * 100

    # comparing to minimum required attendance for exam
    if attendance >= 75:
        # output
        print("Your attendance is {}%".format(attendance))
        print("You are allowed to take the exam, good luck!")
    elif attendance < 75:
        # output
        print("Your attendance is {}%".format(attendance))
        print("You cannot take the exam, better luck next time!")
    else:
        print("Error, try again.")


if __name__ == "__main__":
    main()
