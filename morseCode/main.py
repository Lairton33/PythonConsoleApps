from cleanData import morse_to_letter,letter_to_morse


def convertMorse(value, mtt=False):

    conversion = ''
    
    try:
        # if Morse To Text(mtt)
        if mtt == False:
            text = value.upper()
            for letter in text:
                conversion += letter_to_morse[letter] + ' '

        else:
            for morse in value.split():
                conversion += morse_to_letter[morse]

        return conversion

    except KeyError:
        raise Exception("Oops! It seems you may have made a typo.")
 
    

print(convertMorse("... --- ...", mtt=True))