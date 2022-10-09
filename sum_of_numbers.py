#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Oct 2022
# This program adds two numbers inputted by the user

import math


def main():
    # this function calculates the sum of two numbers inputted by user

    # input
    number_one = int(input("Enter the first number: "))
    number_two = int(input("Enter the second number: "))
    # process
    sum_of_numbers = number_one + number_two

    # output
    print("")
    print("The sum of the two numbers is {0}.".format(sum_of_numbers))

    print("\nDone.")


if __name__ == "__main__":
    main()
