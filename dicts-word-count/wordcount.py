"""Count words in file."""

#THURS. FEB 8TH LAB
#worked in lab with Yesica to complete this 
#open the text file
poem = open("test.txt")

#create an empty dictionary
counts ={}

#loop through each line of the poem
for line in poem:
    
    #remove the empty spaces
    line = line.rstrip()
    
    #create a list of all the words (by splitting at a blank space " ")
    line = line.split(" ")
    
    #create a for loop to run through each word in the list line
    for word in line:
        
        #changes each word to only lower cases
        word = word.lower()

        #if there is a character that is not a letter (such as a punctuation mark)
        if word.isalpha() is False:

            #remove the last character of the string
            word = word[:-1]

        #each time there is a new word add it to the dictionary
        #OR if it is already in the dictionary add 1 to the counter
        counts[word] = counts.get(word,0) + 1

#this runs through each key in the dictionary
#it prints the key which is the unique word in the poem
#and the value which is the number of times the word is repeated
for word, counter in counts.items():
    print(word, counter)

