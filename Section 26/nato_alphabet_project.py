import pandas as pd

name = input('Enter your name: ')
try:
    if not name.isalpha():
        raise Exception()
except Exception as e:
    print('Only alphabets are allowed! 1')
    while not name.isalpha():
        try:
            name = input('Enter your name: ')
            if not name.isalpha():
                raise Exception()
            else:
                break
        except Exception as e:
            print('Only alphabets are allowed! 2')

    
nato_data = pd.read_csv('./nato_phonetic_alphabet.csv')

code_list = [row.code for letter in name for (_,row) in nato_data.iterrows() if letter.upper() == row.letter]
print(code_list)