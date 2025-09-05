import os
clear = lambda: os.system('cls') # use this to clear the screen; 
# a lambda function is made using a system call and passing cls command as a parameter
bids = {}
while(True):
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    bids[name] = bid
    more = input("Are there any other bidders? Type 'yes' or 'no' ").lower()

    if more == "yes":
        clear() # calling the lambda function 
        continue
    else:
        break

# method 1 to get max values
# max = 0
# name = ""
# for names in bids:
#     if bids[names] > max:
#         max = bids[names]
#         name = names



# another way to find the max bit is 
max_bid = max(bids,key= lambda x : bids[x])
print(f"The winner is {name} with a bid of {bids[name]}")
