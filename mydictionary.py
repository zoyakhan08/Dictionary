import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()

    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word.title()]

    elif word.upper() in data:
        return data[word.upper()]

    elif len(get_close_matches(word,data.keys()))>0 :
        print('Did you mean %s instead'%get_close_matches(word,data.keys())[0])
        decide = input('Press y if yes or n for no')

        if decide == 'y':
            return(data[get_close_matches(word,data.keys())[0]])

        elif decide == 'n':
            return('You stepped on a wrong key PUGGER')

        else:
            return('Please enter a correct input')
        
    else:
        return('You stepped on a wrong key PUGGER')


word = input('Enter a word to be searched')
output = translate(word)


if type(output) == list :
    for item in output:
        print(item)
else:
    print(output)