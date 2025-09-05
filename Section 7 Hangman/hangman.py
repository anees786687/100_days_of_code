import random
word_list = ["aardvark","baboon", "camel"]

#todo 1- randomly choose a word fromt the list and assign it to a variable. Then print it

#todo 2 - Ask the use to guss a letter and assign their answer to a variable called guess. Make guess lowercase

#todo 3 - check if the use guessed is one of the letter in the chose word. Print Right if yes else print Wrong

chosen_word = random.choice(word_list)
dashed_word = "_" * len(chosen_word)
lives = 6

chosen_word_list = list(chosen_word)
dashed_word_list = list(dashed_word)
while lives > 0:

    c = input("Enter a character: ")
    for i in range(0,len(chosen_word_list)):
        if c == chosen_word_list[i]:
            # check if the char that has been inputted is on the current index, if yes then replace the _ at that index and move on
            dashed_word_list[i] = c
    
    if c not in chosen_word_list:
        lives-=1 # if char aint the list then reduce a life
        print(f"You have {lives} left")

    if dashed_word_list.__contains__('_') == False:
        break # if the dahsed work aint got no _ then we break out of the loop
    
    print("".join(str(i) for i in dashed_word_list)) # make a string out of the list

if lives > 0: # if you got lives left means you guessed the word correctly
    print("You Won!")
else:
    print("You Lost!")