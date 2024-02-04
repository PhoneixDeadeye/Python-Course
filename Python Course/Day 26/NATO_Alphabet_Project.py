import pandas as pd

data = pd.read_csv(r"C:\Users\Glentech Group\OneDrive\Desktop\Rohan\Python Course\Day 26\nato.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()} 

print(phonetic_dict)

word = input("Enter a word: ").upper()

output_list = [phonetic_dict[letter] for letter in word]

print(output_list)