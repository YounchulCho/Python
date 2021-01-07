#   This program has split the string and find the seven numbers.
#   Each number has to be smaller than 70.
#   The answer will not be only one. It is search every possible situation.

from enum import Enum
import copy, sys



# Define Enumeration
class Progress(Enum):
    Stop = 1
    Go = 2



# Running the search for one digit and two digit type
def findNumber(input, count, result):    
    # Check one digit search
    result1 = copy.deepcopy(result)
    oneDigit(input, count, result1)

    # Check two digits search
    result2 = copy.deepcopy(result)
    twoDigit(input, count, result2)
    
    # Memory free for unnecessary array
    del result



def checkProgress(max, digit, length, result):
    if len(result) == max:          # The maximum array of number is 7
        if (length > digit):        # The string is too long
            return Progress.Stop
        elif (length == digit):     # If this is the last one
            print(result)           # Print out the answer
            return Progress.Stop
    elif length < (digit * 2):      # The string is too short, game over
        return Progress.Stop
    else:
        return Progress.Go          # Keep going to next step



#   Check the one digit each time from the string
def oneDigit(inputString, count, result):
    
    # Get the length of string and stop if the string size is 0
    length = len(inputString)
    if (length < 1):
        return

    # Copy the first number to the result
    result.append(inputString[0])
    
    # Get new input string without first one
    newInput = inputString[1:length]
    # Increase the count
    currentCount = count + 1

    # Check vaild or invaild based on the remaining string
    if(checkProgress(7, 1, length, result) == Progress.Go):
        # Copy the result and recursive again
        findNumber(newInput, currentCount, result)

    return




#   Check the two digits number from the string
def twoDigit(inputString, count, result):

    # Get the length of string and stop if the string size is smaller than 2
    length = len(inputString)
    if (length < 2):
        return

    # Get new input string without first two character
    newInput = inputString[0:2]
    # If the value is over 69, pass
    if (int(newInput) > 69):
        return

    # Copy the new value
    result.append(newInput)

    # Get new input string without first one
    newInput = inputString[2:length]
    # Increase the count
    currentCount = count + 1

    if((checkProgress(7, 2, length, result)) == Progress.Go):
        # Call recursive function
        findNumber(newInput, currentCount, result)

    return 



if __name__ == "__main__":
    # inputString = "11223344556677"
    # inputString = "1234567"
    # inputString = "569815571556"
    # inputString = '452837612738'
    # inputString = '7654321'

    while(1):
        print("* Input the numeric value. If you want to stop, typing 'exit'")
        print(": ", end="")
        inputString = input()

        if inputString == "exit":
            break

        if inputString.isnumeric():
            # Create the result and start game
            result = []
            findNumber(inputString, 0, result)
        else:
            print("Input is not a number.")
        

    pass
    
