import pandas as pd

name = input('Enter your name: ')
nato_data = pd.read_csv('./nato_phonetic_alphabet.csv')

code_list = [row.code for letter in name for (_,row) in nato_data.iterrows() if letter.upper() == row.letter]
print(code_list)