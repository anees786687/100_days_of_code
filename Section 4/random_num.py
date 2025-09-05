import random
# float_rand = random.random() # generates a floating pt number between [0.0, 1)
float_rand = random.uniform(1,3) # generates a floating pt number between [a,b]
print(f"{"{:.4f}".format(float_rand)}")