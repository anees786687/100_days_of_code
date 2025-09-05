"""
Decide who pays, there are n people. Generate a radom number k between 0 to n - 1, the person at index k pays
"""
import random
friends = ["Alice","Bob", "Charlie", "David", "Emmanuel"]

# Method 1
# r_idx = random.randint(0,len(friends) - 1)

# print(f"The person who pays is {friends[r_idx]}")

# Method 2
print(f"The person who pays is {random.choice(friends)}")
