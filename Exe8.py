"""
Name:Sulaiman Khalifa Khalfan Al Yousfi
ID:s133607
Lab:8
Exe:8
Algorithm:
    1)Prompt the user for a word.
    2)While input is not space
        1)Create var final to store all printer data
        2)Create var count to count the
        3)for each character in word
            1)print count and the character
            2)convert the count to string and add count and char to final
            3)increment count.
        4)Print value of final
        5)Prompt the user again
Test:
    Input:
        1)sulaiman
        2)"Space"
    Output:
        Enter word or Enter a space to stop: sulaiman
        0 s
        1 u
        2 l
        3 a
        4 i
        5 m
        6 a
        7 n
        0s1u2l3a4i5m6a7n

        Enter word or Enter a space to stop:
"""
word = input("Enter word or Enter a space to stop: ")
while word != "":
    final = ""
    count = 0
    for i in word:
        print(count, i)
        final += str(count) + i
        count += 1
    print(final, "\n")
    word = input("Enter word or Enter a space to stop: ")