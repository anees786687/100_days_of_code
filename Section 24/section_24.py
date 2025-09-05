# file = open('tst.txt')
# content = file.read()
# print(content)
# file.close()

# with open('tst.txt') as file:
#     content = file.read()
#     print(content)


# with open('tst.txt', mode='w') as file:
#     file.write('Something something!')

# with open('tst.txt', mode='a') as file:
#     file.write('Some more of something for something!')

with open('starting_letter.txt') as file:
    content = file.read()

with open('invited_names.txt') as names:
    names_list = names.read().split()

placeholder_pattern = '[name]'
placeholder_index = content.find('[name]')



for name in names_list:
    temp = content
    temp = temp.replace(placeholder_pattern,name)
    with open(f'invites/{name}_invite.txt', mode='w') as invite:
        invite.write(temp)

    
