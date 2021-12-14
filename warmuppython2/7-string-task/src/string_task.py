"""write your code in method"""
def isvowel(letterlist):
    vowel = ['a','e','i','o','u']
    for i in vowel:
        while i in letterlist:
            letterlist.remove(i)
    return letterlist

def get_string():
    #input
    letterlist = []
    string = input()

    # change to lower case letters
    string = string.lower()


    for i in string:
        letterlist.append(i)

    # delete vowel
    letterlist = isvowel(letterlist)

    # add "." in front of consonants and output
    for i in letterlist:
        print(".",end='')
        print(i,end='')
    print('')
    return


