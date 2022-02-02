import pandas as pd

data = pd.read_csv("morseCode")
letter_to_morse = dict()
morse_to_letter = dict()

for idx in range(len(data)):

    letter_to_morse[data["Letter"][idx]] = data["Morse"][idx].replace('*','.')
    morse_to_letter[data["Morse"][idx].replace('*','.')] = data["Letter"][idx]
