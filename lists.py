#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Dec. 21, 2023
# This program calculates the average mark from user inputted marks.


def calc_average(list_of_marks):
    # initialize sum
    sum = 0

    # get sum of marks
    for a_num in list_of_marks:
        sum = sum + a_num

    # calculate average
    average = sum / len(list_of_marks)

    # return value of average
    return average


def main():
    # introduce program user
    print("Hello, this program calculates the average mark")

    # declare list
    mark_list = []

    # loop asking for mark
    while True:
        user_num = input("Please enter a mark 0-100 (-1 to exit): ")

        # check if valid input
        try:
            user_num_int = int(user_num)

            # check if number is within range
            if (user_num_int <= -2) or (user_num_int >= 101):
                # tell user invalid number
                print(
                    "Please enter a number 0-100. {} is not in that range.".format(
                        user_num_int
                    )
                )

            else:
                # append to list
                mark_list.append(user_num_int)

        except Exception:
            print("Please enter a valid mark. {} is not valid.".format(user_num))

        if user_num_int == -1:
            # break out of loop
            break

    # remove -1 from list
    mark_list.pop()

    # call function to calculate average
    mark_average = calc_average(mark_list)

    # display average
    print("The mark average is {}.".format(mark_average))


if __name__ == "__main__":
    main()
