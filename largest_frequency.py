'''
Write a python program that accepts a text and displays a string which contains
the word with the largest frequency in the text and the frequency itself separated
by a space.
Rules:
The word should have the largest frequency.In case multiple words have the same
frequency, then choose the word that has the maximum length.
Assumptions:
The text has no special characters other than space.The text would begin with a
word and there will be only a single space between the words.
Perform case insensitive string comparisons wherever necessary.
I am good i am bad i am good
'''
def max_frequency_word(data):
    word=""
    frequency=0
    lower_data=data.lower()
    list=[]
    list=lower_data.split()
    repeat=[]
    a=[]
    i=0
    while(i < len(list)):
        if list.count(list[i]) > 1:
            repeat.append(list[i])
            i=i+1
        else:
            i=i+1
    for i in repeat:
        a=repeat.count(i)
    
    for i in range(0,len(repeat)):
        if repeat.count(repeat[i])==a:
            word=word+repeat[i]
            frequency=a
            break
    print(word,frequency)
data="Good Bad Good Bad Bad"
max_frequency_word(data)
