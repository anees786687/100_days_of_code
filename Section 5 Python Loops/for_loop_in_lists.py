# l = ["apple","banana","orange"]

# for i in l:
#     print(i.title())

scores = [180,124,165,173,189,169,146]

# Sum of a list 
# print(f"Sum using sum function {sum(scores)}")


# sum = 0

# for i in scores:
#     sum += i
# print(f"Sum using for loop {sum}")

# Max num in a list

max_num = -1

for i in scores:
    if i > max_num:
        max_num = i

print(max_num)

print(f"max in a list using max function {max(scores)}")