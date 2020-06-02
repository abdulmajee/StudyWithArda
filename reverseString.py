
def main():
    user_input = input("Please Enter the string to be reversed: ") # take in the user string
    reversed_input = ""  # Create and empty string to store the revered characters
    for x in user_input :  # loop through the string and check each character
        reversed_input = x + reversed_input  # append the characters in a reversed order

    print(reversed_input)  # print out the result of the reversed word


if __name__ == '__main__':
    main()