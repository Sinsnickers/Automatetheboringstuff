#English to Pig Latin

print("Enter the English message to translate into pig latin")
message = input()

VOWELS =("a","e","i","o","u","y")

piglatin = [] #A list of words in pig latin
for word in message.split():
    #Separate the non letters @ the beginning of the word
    prefixNonLetters =""
    while(len(word)>0 and not word[0].isalpha()):
        prefixNonLetters+=word[0]
        word = word[1:]

    if len(word)==0:
        piglatin.append(prefixNonLetters)
        continue

    #Separate the non lettes @ the end of the word
    suffixNonLetters = ""
    while(not word[-1].isalpha()):
        suffixNonLetters+=word[-1]
        word = word[:1]

    #remember if the word was uppercase or title case
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() #Make the word lowercase for translation

    #Separate the consonants @ the start of the word
    prefixConsonants=""
    while(len(word)>0 and not word[0] in VOWELS):
        prefixConsonants += word[0]
        word = word[1:]

    #Add the pigLatin ending @ the word
    if prefixConsonants != "":
        word+=prefixConsonants + "ay"
    else:
        word += "yay"

    #Set the word back to uppercase or title case
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    #Add the non letters to the start and the end of the word
    piglatin.append(prefixNonLetters+word+suffixNonLetters)

    #Join the word back together
print(' '.join(piglatin))