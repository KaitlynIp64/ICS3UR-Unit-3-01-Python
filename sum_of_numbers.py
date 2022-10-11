#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Oct 2022
# This program adds two numbers inputted by the user

import math


def main():
    # this function calculates the sum of two numbers inputted by user

    # input
    number_one = float(input("Enter the first number: "))
    number_two = float(input("Enter the second number: "))

    # process
    sum_of_num = number_one + number_two

    # output
    print("")
    print("{0:,.0f} + {1:,.0f} = {2:,.0f}.".format(number_one, number_two, sum_of_num))

    print("\nDone.")


if __name__ == "__main__":
    main()
