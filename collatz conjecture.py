

def collatz_conj(starting_number):
    steps = 0
    largest_number = starting_number
    while starting_number > 1:
        if starting_number % 2 != 0:
            starting_number = 3*starting_number + 1
            if largest_number < starting_number:
                largest_number = starting_number
            steps = steps + 1
            print(starting_number)
        if starting_number % 2 == 0:
            starting_number = starting_number / 2
            if largest_number < starting_number:
                largest_number = starting_number
            steps = steps + 1
            print(starting_number)

    print("There were a total of " + str(steps) + " operations.")
    print("The largest number was " + str(largest_number))

collatz_conj(int(input("What number do you wish to start with?")))