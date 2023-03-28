"""
Name:Sulaiman Khalifa Khalfan Al Yousfi
ID:s133607
Algorithm
        1)Prompt the user for a sentence or a word.
        2)strip the line/word to remove all spaces.
        3)split the input.
        4)loop for each in list
            print the flipped word.
Test:
    Input:
        Python is a high-level, interpreted programming language that was first released in 1991 by Guido van Rossum.
    Output:
        Pothyn is a highlleve-, inteeprrted prigrammong lungaage taht was fsrit reeeasld in 1991 by Giudo van Rmssuo.
"""
from random import randint


def main():
    line = input("Enter the sentence/word: ").strip().split(" ")

    for i in line:
        print(wordFlip(i), end=" ")

# The function will check weather the word length is less than 4 if no then returns the word since no flipping can be
# done.
# If the length is 4 and above
#   loops to generate two random numbers in the respective range and check if they are equal or not.
#   Split the word into a list of characters
#   replace the indexes
#   join the indexes to create the word
# @para word String

def wordFlip(word):
    if len(word) < 4:
        return word
    else:
        same = True
        while same:
            r1 = randint(1, len(word) - 2)
            r2 = randint(1, len(word) - 2)
            if r1 != r2:
                same = False
        lst = list(word)
        temp = lst[r1]
        lst[r1] = lst[r2]
        lst[r2] = temp
        return "".join(lst)


main()
